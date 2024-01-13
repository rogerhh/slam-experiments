import numpy as np
import matplotlib.pyplot as plt

sphere_steps = [53, 203, 592]
sphere_lamb = [0.14777, 0.168369, 0.1512128]

w_steps = [60, 355, 421, 783, 931]
w_lamb = [0.027798, 0.31715, 0.025069, 0.0244377, 0.0327408]

plt.plot(sphere_steps, sphere_lamb, '-o', label="sphere_boundnorm")
plt.plot(w_steps, w_lamb, '-o', label="w10000_boundnorm")
plt.plot([20, 950], [0.9, 0.9], '--r', label="rho=0.9")
plt.xlabel("Step")
plt.ylabel("2-norm of E")
plt.legend()
plt.savefig("/home/ubuntu/slam-experiments/2023-12-10_project-experiments/output/processed/sphere_bound_norm.png")
plt.show()
