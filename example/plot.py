import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.rcParams['font.size'] = 14

τ = np.loadtxt("S_curve_tau.dat")
mixf = τ[:,0]; τ = τ[:,1:]*1000                # ms
T = np.loadtxt("S_curve_T.dat")[:,1:]

fig, ax = plt.subplots(1,2, figsize=(10,4))

colors = cm.Blues(np.linspace(0.3, 1, len(mixf)))
imixf = 0; ax[0].plot(τ[imixf,:], T[imixf,:], color=colors[imixf], label=f"Z={mixf[imixf]:.3f}")
imixf = 1; ax[0].plot(τ[imixf,:], T[imixf,:], color=colors[imixf], label=f"{mixf[imixf]:.3f}")
imixf = 2; ax[0].plot(τ[imixf,:], T[imixf,:], color=colors[imixf], label=f"{mixf[imixf]:.3f}")
imixf = 3; ax[0].plot(τ[imixf,:], T[imixf,:], color=colors[imixf], label=f"{mixf[imixf]:.3f}")
imixf = 4; ax[0].plot(τ[imixf,:], T[imixf,:], color=colors[imixf], label=f"{mixf[imixf]:.3f}")
imixf = 5; ax[0].plot(τ[imixf,:], T[imixf,:], color=colors[imixf], label=f"{mixf[imixf]:.3f}")
imixf = 6; ax[0].plot(τ[imixf,:], T[imixf,:], color=colors[imixf], label=f"{mixf[imixf]:.3f}")
ax[0].set_xscale("log")
ax[0].set_ylim([900,2300])
ax[0].set_xlim([1E-2, 1000])
ax[0].legend(frameon=False, ncols=1, fontsize=8, loc="lower left")
ax[0].set_ylabel("Temperature (K)")
ax[0].set_xlabel("τ (ms)")
ax[0].set_title("Lean")

colors = cm.Reds(np.linspace(0.0, 1.0, len(mixf)))
imixf = 7; ax[1].plot(τ[imixf,:], T[imixf,:], color=colors[8], label=f"Z={mixf[imixf]:.3f}")
imixf = 8; ax[1].plot(τ[imixf,:], T[imixf,:], color=colors[6], label=f"{mixf[imixf]:.3f}")
imixf = 9; ax[1].plot(τ[imixf,:], T[imixf,:], color=colors[4], label=f"{mixf[imixf]:.3f}")
imixf =10; ax[1].plot(τ[imixf,:], T[imixf,:], color=colors[2], label=f"{mixf[imixf]:.3f}")
ax[1].set_xscale("log")
ax[1].set_ylim([900,2300])
ax[1].set_xlim([1E-2, 1000])
ax[1].set_yticks([])
ax[1].legend(frameon=False, ncols=1, fontsize=8, loc="lower left")
ax[1].set_xlabel("τ (ms)")
ax[1].set_title("Rich")

plt.savefig("S_curve.png", dpi=300, bbox_inches="tight")
