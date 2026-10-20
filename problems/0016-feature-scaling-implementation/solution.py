import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	# zscaler
	# standardized - make it into normal distribution - mean of zero - sd of one
	mean = np.mean(data, axis = 0) 
	sd = np.std(data, axis=0)
	sa = (data - mean) / sd

	# min max normalization - compress int [0,1]
	min = np.min(data, axis =0)
	max = np.max(data, axis =0)
	na = (data - min)/(max - min)
	return sa, na
