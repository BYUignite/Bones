import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.rcParams['font.size'] = 12

τ = np.loadtxt("S_curve_tau.dat")
mixf = τ[:,0]; τ = τ[:,1:]
T = np.loadtxt("S_curve_T.dat")[:,1:]

fig, ax = plt.subplots(1,1, figsize=(6,4))

colors = cm.Blues(np.linspace(0.2, 0.8, 7)) #len(mixf)))
imixf = 0; ax.plot(τ[imixf,:], T[imixf,:], '-', color=colors[imixf], lw=1, label=f"Z={mixf[imixf]:.3f}")
imixf = 1; ax.plot(τ[imixf,:], T[imixf,:], '-', color=colors[imixf], lw=1, label=f"{mixf[imixf]:.3f}")
imixf = 2; ax.plot(τ[imixf,:], T[imixf,:], '-', color=colors[imixf], lw=1, label=f"{mixf[imixf]:.3f}")
imixf = 3; ax.plot(τ[imixf,:], T[imixf,:], '-', color=colors[imixf], lw=1, label=f"{mixf[imixf]:.3f}")
imixf = 4; ax.plot(τ[imixf,:], T[imixf,:], '-', color=colors[imixf], lw=1, label=f"{mixf[imixf]:.3f}")
imixf = 5; ax.plot(τ[imixf,:], T[imixf,:], '-', color=colors[imixf], lw=1, label=f"{mixf[imixf]:.3f}")
imixf = 6; ax.plot(τ[imixf,:], T[imixf,:], '-', color=colors[imixf], lw=1, label=f"{mixf[imixf]:.3f}")

imixf = 7; ax.plot(τ[imixf,2:], T[imixf,2:], '-', color="black",       lw=3, label=f"{mixf[imixf]:.3f}")

colors = cm.Reds(np.linspace(0.2, 0.8, 4)) #len(mixf)))
colors = colors[::-1]
imixf = 8; ax.plot(τ[imixf,:], T[imixf,:], '-', color=colors[imixf-8], lw=1, label=f"{mixf[imixf]:.3f}")
imixf = 9; ax.plot(τ[imixf,:], T[imixf,:], '-', color=colors[imixf-8], lw=1, label=f"{mixf[imixf]:.3f}")
imixf =10; ax.plot(τ[imixf,:], T[imixf,:], '-', color=colors[imixf-8], lw=1, label=f"{mixf[imixf]:.3f}")
imixf =11; ax.plot(τ[imixf,:], T[imixf,:], '-', color=colors[imixf-8], lw=1, label=f"{mixf[imixf]:.3f}")

ax.set_xscale("log")
ax.set_ylim([700,2300])
ax.set_xlim([1E-5, 1E2])
ax.legend(frameon=False, ncols=4, fontsize=8, loc="lower left")
ax.set_ylabel("Temperature (K)")
ax.set_xlabel("τ (s)")

plt.savefig("S_curve.png", dpi=300, bbox_inches="tight")
