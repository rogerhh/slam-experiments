Experiment name
===============
Profile singular values

date\_time
----------
2023-08-04\_11-56

Description
-----------
Profile singular values after preconditioning with different types of preconditioner updaters
1. Identity matrix on the trailing principle submatrix
2. Square root of the diagonal of the new trailing principal submatrix (extended diagonal)
3. Cholesky on the new trailing principal submatrix
4. Incomplete Cholesky on each column that has changed
5. Maybe propagate changes down some important connections (incomplete cholesky update)
More to come...


Procedure
---------

For each type of preconditioner updater, profile:
1. Condition number before and after preconditioning
2. Plot singular value distribution
3. # of CG iterations
4. Rank of relin update and rank of observation update
5. # of new columns in A
Repeat for lookahead step 1-5

Results
-------
Profiled cg iterations for both explicitly constructing AL^-T and using linear operators. Linear operators reduce the # of cg iterations by up to 15%, especially with very ill conditioned matrices

Interpretation
--------------

Versions
--------

