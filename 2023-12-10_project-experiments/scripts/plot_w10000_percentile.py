import numpy as np
import matplotlib.pyplot as plt

t = [1e-4, 1e-5, 1e-8, 1e-10]
x_100 = [0.5270041003046742,  0.020608842048565515,0.0006320473152748302,0.0006029342690375203]
x_25 = [0.0041330171730572015,0.0003708825539158069,2.403782723358846e-07,2.5763922861103733e-13]
x_50 = [0.021187668522724103,0.00487133781661277,3.7646897964246256e-06,4.283367112068207e-12]
x_75 = [0.09691728986839615,0.010841912963301649,2.1451477241708058e-05,2.0863372868835346e-05]

plt.plot(t, x_100, '-o', label="100th percentile")
plt.plot(t, x_75, '-o', label="75th percentile")
plt.plot(t, x_50, '-o', label="50th percentile")
plt.plot(t, x_25, '-o', label="25th percentile")
plt.xlabel("CG Tolerance")
plt.ylabel("Percentile of abs(Delta)")
plt.xscale("log")
plt.yscale("log")
plt.legend()
plt.savefig("/home/ubuntu/slam-experiments/2023-12-10_project-experiments/output/processed/w10000_extdiag_cg_tol.png")
plt.show()
