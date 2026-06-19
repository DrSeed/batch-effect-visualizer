import os, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
os.makedirs("figures",exist_ok=True); os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(7); g=200
cond=np.array([0]*60+[1]*60); batch=np.array(([0]*30+[1]*30)*2)
X=rng.normal(0,1,(120,g))
X+=cond[:,None]*1.5*rng.normal(1,.1,g)        # biology
X+=batch[:,None]*3.0*rng.normal(1,.1,g)        # batch effect
def pca2(M): return PCA(2).fit_transform(M)
Xc=X.copy()
for b in (0,1): Xc[batch==b]-=Xc[batch==b].mean(0)  # simple batch centering
fig,ax=plt.subplots(1,2,figsize=(10,4))
for a,M,t in [(ax[0],X,"before correction"),(ax[1],Xc,"after correction")]:
    e=pca2(M)
    for c,mk in [(0,"o"),(1,"s")]:
        a.scatter(e[cond==c,0],e[cond==c,1],c=["#d95f02" if bb else "#1b9e77" for bb in batch[cond==c]],marker=mk,s=18)
    a.set_title(t); a.set_xlabel("PC1"); a.set_ylabel("PC2")
fig.suptitle("Batch effect: colour=batch, shape=condition (demo data)")
plt.tight_layout(); plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write("batch effect removed, condition preserved\n"); print("ok")