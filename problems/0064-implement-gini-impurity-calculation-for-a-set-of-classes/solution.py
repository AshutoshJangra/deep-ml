
import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	u, c = np.unique(y, return_counts = True)
	prob = c / len(y)
	return round(1 - np.sum(prob**2),3)