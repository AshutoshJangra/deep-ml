import numpy as np

def shuffle_data(X, y, seed=None):
	n = len(y)
	idxa = np.arange(0,n)
	if seed is not None:
		np.random.seed(seed)
	idxa = np.random.permutation(idxa)

	X = X[idxa]
	y = y[idxa]
	return X,y
	pass