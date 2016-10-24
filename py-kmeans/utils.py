import numpy as np


def dataset_ball(center, radius: float, numpoints: int):
    dataset = []
    while len(dataset) < numpoints:
        point=[np.random.uniform(low=(center[i] - radius),high=(center[i] + radius)) for i in range(len(center))]
        if sum(map(lambda x:x*x,[i - j for i, j in zip(point,center)])) < (radius * radius):
            dataset.append(point)
    return np.array(dataset)