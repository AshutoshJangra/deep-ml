import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
    t = np.transpose(X)
    tm = np.matmul(t, X)
    tm_inv = np.linalg.inv(tm)
    w = np.matmul(tm_inv, np.matmul(t, y))

    w=np.round(w, 4)
	return w
    