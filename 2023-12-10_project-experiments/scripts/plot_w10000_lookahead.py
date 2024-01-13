import numpy as np
import matplotlib.pyplot as plt

lookahead = [1, 2, 4, 8, 16]
cg_iter = [49, 67, 75, 176, 370]

plt.plot(lookahead, cg_iter, '-o')
plt.xlabel("dT")
plt.ylabel("# of CG iterations")
plt.savefig("/home/ubuntu/slam-experiments/2023-12-10_project-experiments/output/processed/w10000_lookahead.png")
plt.show()
