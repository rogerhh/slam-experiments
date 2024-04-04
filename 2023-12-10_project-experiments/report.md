Experiment name
===============
Project Experiments

date\_time
----------
2023-12-10\_11-58

Description
-----------
Various experiments needed for the MATH 221 final project. 
Datasets: w10000 and sphere2500. 
Preconditioners: identity, extended diagonal, only A\_hat, bounded diff, sel bounded diff, sel row norm, sel col
0. For identity and extended diag, for each (dataset, preconditioner, LC step), record
  LC step, matrix size, obs rank, condition number before and after, max lambda of E, num PCG iterations
1. For each (dataset, preconditioner, LC step), record
  LC step, matrix size, obs size, selected rows (obs rows included), conditioner number before and after, num PCG iterations, max lambda of E, max lambda of diff

2. For some iteration, record
  svd, num rows vs cg iter (for the sel row ones), lc lookahead vs cg iter (extended diag), num singular value outliers, 100, 75, 50, 25, percentile of abs of delta

Plot:
  identity and extended diagonal
  1) lookahead vs cg iter

  all
  1) matrix size vs condition number
  2) matrix size vs PCG iterations
  
  sel chol
  1) num selected rows vs PCG iteration
  2) num selected rows vs max lambda of E and max lambda of diff

  1) cg tol vs percentiles of delta

Procedure
---------

Results
-------

Interpretation
--------------

Versions
--------

