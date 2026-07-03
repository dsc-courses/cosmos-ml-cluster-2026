instructions when copying a lecture from DSC 10:

- lectures live in lectures/. when creating a new lecture, i will tell you which DSC 10 lectures to copy from. the original DSC 10 lectures are in /Users/sam/repos/dsc10/dsc10-2026-wi-private/lectures.
- couple things to note about copying lectures over:
  - DSC 10 uses a package called babypandas, but COSMOS (this course) uses pandas instead. babypandas is just a subset of pandas, so just changing the import statement and changing `bpd` to `pd` should be enough.
  - all references to DSC 10 should be changed to COSMOS
  - don't copy rise.css, but do copy datasets and images
  - sometimes cells will error deliberately. these cells should already have the `raises-exception` cell tag so you don't need to do anything extra.
  - in the cell that sets up imports, include a snippet like this one so that the datasets are loaded when running in google colab:
    ```
    path = 'lectures/lec01' # change this to the lecture
    if not Path("data").exists():
        !wget -q -O /content/course.zip https://github.com/dsc-courses/cosmos-ml-cluster-2026/archive/refs/heads/main.zip
        !unzip -q -o /content/course.zip "cosmos-ml-cluster-2026-main/{path}/data/*" -d /content/course-assets
        !cp -R /content/course-assets/cosmos-ml-cluster-2026-main/{path}/data .
    ```
  - finally, execute the notebook in the project env using `uv` to make sure that the code runs.
- after verifying that the code runs, output a summary of all the changes made so i can review.

instructions when copying a lab or homework from DSC 10:

- DSC 10 assignments have a src/ and a build/ folder. copy the src/ folder over and keep all the solutions, ignore the build/ folder. (i have a separate script to regenerate the student-facing version in the build/ folder.)
- remove due dates
- remove instructions (e.g. slip days, hidden test cases, etc.)
- remove all mentions to Gradescope, so sentences like "You should complete this entire lab so that all tests pass and submit it to Gradescope by 11:59PM on the due date." should just be reworded to "You should complete this entire lab so that all tests pass".
- there are no homeworks in COSMOS, only labs, so if i ask you to import a DSC 10 homework, make sure that mentions of "homework" are replaced with "lab".
- in the cell that sets up imports, the first line should run !pip install otter-grader==6.1.6, but only if the notebook is open in Google Colab (not locally).
- in the cell that sets up imports, include a snippet like this one so that the datasets are loaded when running in google colab:
  ```
  path = 'labs/lab01' # change this to the lab
  if not Path("data").exists():
      !wget -q -O /content/course.zip https://github.com/dsc-courses/cosmos-ml-cluster-2026/archive/refs/heads/main.zip
      !unzip -q -o /content/course.zip "cosmos-ml-cluster-2026-main/{path}/data/*" -d /content/course-assets
      !cp -R /content/course-assets/cosmos-ml-cluster-2026-main/{path}/data .
  ```
- at the end of the lab, there's a place to cite AI tools. we can just remove this.
- remove the entire cell with the instructions for submission, since students don't need to submit anything in this class. but keep the grader.check_all() cell for convenience.
- change `bpd` imports to `pd`. change babypandas mentions in the question text to `pandas`.
- DSC 10 homeworks have hidden test cases, but i just want all test cases to be visible for students, so remove `# HIDDEN` comments or any other metadata so that all the test cases are public.
