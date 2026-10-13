import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	result = []
	l = len(X)
	tb = int(l/batch_size)
	# print(tb)
	start = 0
	
	ls = []
	for i in range(0 , l , batch_size):
		end= start+batch_size
		if y is not None:
			ls.append([X[start:end].tolist() , y[start:end].tolist()])
		else:
			ls.append(X[start:end].tolist())	
		start = end
	
	return ls
	pass