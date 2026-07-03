#!/usr/bin/env -S uv run python

"""CLI app for COSMOS course maintenance tasks."""

from pathlib import Path
from subprocess import CalledProcessError, run
from typing import Annotated

import nbformat
import typer

ROOT = Path(__file__).resolve().parent.parent
LABS_DIR = ROOT / "labs"

PASTEL_BLUE = (135, 206, 250)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

DEBUG_MODE = False


def set_debug(value: bool) -> None:
    """Set debug output mode."""
    global DEBUG_MODE
    DEBUG_MODE = value


def echo(message: object = "", **kwargs) -> None:
    """Print a prefixed CLI message."""
    prefix = typer.style("[cosmos] ", fg=PASTEL_BLUE)
    for line in str(message).split("\n"):
        typer.echo(f"{prefix}{line}", **kwargs)


def error(message: object = "", **kwargs) -> None:
    """Print a prefixed error message."""
    prefix = typer.style("[error]", fg=WHITE, bg=RED)
    kwargs.setdefault("err", True)
    for line in str(message).split("\n"):
        typer.echo(f"{prefix} {line}", **kwargs)


def debug_echo(message: object = "", **kwargs) -> None:
    """Print a debug message if debug output is enabled."""
    if not DEBUG_MODE:
        return
    prefix = typer.style("[debug] ", fg=ORANGE)
    for line in str(message).split("\n"):
        typer.echo(f"{prefix}{line}", **kwargs)


def get_valid_labs() -> dict[str, Path]:
    """Return a dict mapping lab names to their lab directory paths."""
    labs: dict[str, Path] = {}
    if not LABS_DIR.exists():
        return labs

    for child in LABS_DIR.iterdir():
        if child.is_dir() and (child / "src" / f"{child.name}.ipynb").exists():
            labs[child.name] = child
    return labs


def validate_lab(value: str) -> str:
    """Validate that a lab exists and has the expected source notebook."""
    valid = get_valid_labs()
    if value not in valid:
        valid_names = sorted(valid.keys())
        valid_list = ", ".join(valid_names) if valid_names else "(none found)"
        raise typer.BadParameter(
            f"'{value}' is not a valid lab.\n\n"
            f"Valid labs are:\n  {valid_list}"
        )
    return value


def assert_notebook_has_been_run(nb_path: Path) -> None:
    """Assert that all non-empty code cells in the notebook have been run."""
    nb = nbformat.read(nb_path, as_version=nbformat.NO_CONVERT)

    for cell in nb["cells"]:
        if (
            cell["cell_type"] == "code"
            and cell["source"] != ""
            and cell["execution_count"] is None
        ):
            error(
                f"{nb_path.name} has unexecuted code cells. "
                "Please run all cells and save the notebook before building."
            )
            raise typer.Exit(code=1)


def otter_assign(source_notebook: Path, output_dir: Path) -> None:
    """Run `otter assign` to generate student-facing lab artifacts."""
    cmd = [
        "uv",
        "run",
        "otter",
        "assign",
        str(source_notebook),
        str(output_dir),
    ]
    debug_echo(f"Running: {' '.join(cmd)}")

    try:
        run(cmd, cwd=ROOT, check=True)
    except CalledProcessError as exc:
        raise typer.Exit(code=exc.returncode) from exc


app = typer.Typer(no_args_is_help=True, rich_markup_mode="markdown")
build_app = typer.Typer(
    no_args_is_help=True, help="Build COSMOS lab notebooks with Otter."
)

DebugOption = Annotated[
    bool,
    typer.Option("--debug", "-d", help="Enable debug output."),
]


@build_app.command()
def lab(
    lab_name: Annotated[
        str,
        typer.Argument(
            callback=validate_lab,
            help="Name of the lab to build (e.g., lab01).",
        ),
    ],
    debug: DebugOption = False,
) -> None:
    """Build a COSMOS lab for release to students."""
    set_debug(debug)

    lab_path = get_valid_labs()[lab_name]
    src_path = lab_path / "src"
    build_path = lab_path / "build"
    notebook_path = src_path / f"{lab_name}.ipynb"
    notebook_name = notebook_path.name

    echo(f"Building {notebook_name} in {lab_path.relative_to(ROOT)}")

    echo(f"Checking that {notebook_name} has been run...")
    assert_notebook_has_been_run(notebook_path)

    echo("Running `otter assign`...")
    otter_assign(source_notebook=notebook_path, output_dir=build_path)

    echo(f"Done! Built {lab_name} in {build_path.relative_to(ROOT)}")


@build_app.callback(invoke_without_command=True)
def default_to_lab(
    ctx: typer.Context,
    lab_name: Annotated[
        str | None,
        typer.Argument(
            callback=lambda v: validate_lab(v) if v is not None else v,
            help="Name of the lab to build (e.g., lab01).",
        ),
    ] = None,
    debug: DebugOption = False,
) -> None:
    """If invoked as `cosmos.py build <lab>`, dispatch to `build lab`."""
    if ctx.invoked_subcommand is not None:
        return
    if lab_name is None:
        raise typer.Exit(code=0)
    lab(lab_name=lab_name, debug=debug)


app.add_typer(build_app, name="build", help="Build lab notebooks with Otter.")


if __name__ == "__main__":
    app()
