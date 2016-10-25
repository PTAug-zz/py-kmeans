from utils import *


def lloyd_iteration(centers,data):
    sums=[0]*len(centers)
    nbpoints=[0]*len(centers)
    for p in data:
        ntab=[np.linalg.norm(p-c) for c in centers]
        nearest=ntab.index(min(ntab))
        sums[nearest]+=p
        nbpoints[nearest]+=1
    new_centers = [sums[s]/nbpoints[s] for s in range(len(centers))]
    return new_centers

def kmeans_clustering(centers,data):
	cost_iteration=[cost_function(centers,data)]
    while not is_same_clustering([[0,0,0],[0,20,0]],centers,data):
        centers = lloyd_iteration(centers,data)
        cost_iteration.append(cost_function(centers,data))
    return centers,cost_iteration