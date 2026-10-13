import numpy as np

def shuffle_data(X, y, seed=None):

	if seed is not None:
		np.random.seed(seed)
	idxa = np.random.permutation(len(y))


	return X[idxa],y[idxa]
	pass