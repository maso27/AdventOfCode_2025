import pyflann
import numpy as np

dataset = np.random.rand(10000, 128)
print(f'dataset: {dataset}')
testset = np.random.rand(1000, 128)
print(f'testest: {testset}')

flann = pyflann.FLANN()
result, dists = flann.nn(dataset,testset,5,algorithm='kmeans',branching=32,iterations=7,checks=16)

print("Indices of Nearest Neighbors:\n", result)
print("Distances to Nearest Neighbors:\n", dists)