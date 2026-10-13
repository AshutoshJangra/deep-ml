import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	# zscaler

	mean = np.mean(data, axis=0)
	std = np.std(data, axis=0)
	std = np.where(std == 0, 1, std)
	standardized_data = (data - mean )/ std
	standardized_data = np.round(standardized_data, 4)


	min = np.min(data, axis = 0)
	max = np.max(data, axis=0)
	range = max - min
	range = np.where(range ==0 , 1, range)
	normalized_data = (data - min)/range
	return standardized_data, normalized_data