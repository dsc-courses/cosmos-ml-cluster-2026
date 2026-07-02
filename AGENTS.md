instructions when copying a lecture from DSC 10:

- lectures live in lectures/. when creating a new lecture, i will tell you which DSC 10 lectures to copy from. the original DSC 10 lectures are in /Users/sam/repos/dsc10/dsc10-2026-wi-private/lectures.
- couple things to note about copying lectures over:
  - DSC 10 uses a package called babypandas, but COSMOS (this course) uses pandas instead. babypandas is just a subset of pandas, so just changing the import statement and changing `bpd` to `pd` should be enough.
  - all references to DSC 10 should be changed to COSMOS
  - sometimes cells will error deliberately. these cells should already have the `raises-exception` cell tag so you don't need to do anything extra.
  - finally, execute the notebook in the project env using `uv` to make sure that the code runs.
- after verifying that the code runs, output a summary of all the changes made so i can review.
