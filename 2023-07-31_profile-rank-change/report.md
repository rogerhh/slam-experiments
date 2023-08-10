Experiment name
==============
profile-rank-change

date\_time
----------
2023-07-31\_22-39

Description
-----------
Profile the rank of matrix A from relinearization and new connections at each timestep for the w10000 and sphere dataset. Also profile the depth of the change (i.e. the farthest back a new connection reaches).

Procedure
---------
In CholeskyEliminationTree::markAffected(...), record and print out the affectedKeys and observedKeys variables. Also take the difference between the largest and smallest observedKeys for depth.

Results
-------
The results are stored in `output/sphere_rank_change.out` and `output/w10000_rank_change.out`.

Interpretation
--------------

Versions
--------
`rogerhh/gtsam`: `287dc2032 (HEAD -> profile-rank-change, origin/profile-rank-change)`
