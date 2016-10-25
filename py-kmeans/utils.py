import numpy as np


def dataset_ball(center, radius: float, numpoints: int):
    dataset = []
    while len(dataset) < numpoints:
        point=np.array([np.random.uniform(low=(center[i] - radius),high=(center[i] + radius)) for i in range(len(center))])
        if np.linalg.norm((point-center)) < radius:
            dataset.append(point)
    return np.array(dataset)

def label_data(centers,data):
    labelled_data=[]
    for p in data:
        ntab=[np.linalg.norm(p-c) for c in centers]
        labelled_data.append((p,ntab.index(min(ntab))))
    return labelled_data

def plot_labeled_data(centers,data):
    x,color=zip(*label_data(centers,data))
    color=[{0:'#E8755B',1:'#349454'}.get(c) for c in color]
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data_all[:,0],data_all[:,1],data_all[:,2],c=color)
    ax.azim = 180
    ax.elev = 45

def cost_function(centers,data):
    return sum([min([np.linalg.norm(p-c)**2 for c in centers]) for p in data])

def is_same_clustering(center1,center2,data):
    label1=[x[1] for x in label_data(center1,data)]
    label2=[x[1] for x in label_data(center2,data)]
    return label1==label2