import numpy as np
import matplotlib.pyplot as plt

steps = [53, 203, 592]
lamb = [0.14777, 0.168369, 0.1512128]

plt.plot(lookahead, lamb, '-o')
plt.xlabel("Step")
plt.ylabel("2-norm of E")
plt.savefig("/home/ubuntu/slam-experiments/2023-12-10_project-experiments/output/processed/sphere_bound_norm.png")
plt.show()
