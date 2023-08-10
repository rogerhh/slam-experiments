Experiment name
===============
Condition number (relin only)

date\_time
----------
2023-08-04\_11-37

Description
-----------
Profile the condition number and the # of CG iterations with relin only changes

Procedure
---------
For the steps listed in LC steps, generate the new A, but remove the new rows, so we're only keeping relinearization updates. Print the condition number before and after preconditioning and the number of cg iterations, and the rank of the update. Repeat for lookahead step 1-5.

Results
-------

Interpretation
--------------
Using the old L as the preconditioner for the new relinearized problem is much better conditioned than the relin + observation problem, i.e., we need to find a better way to update the preconditioner L

Versions
--------
`rogerhh/gtsam`: `032b5cb65 (HEAD -> profile-singular-values, origin/profile-singular-values)`

