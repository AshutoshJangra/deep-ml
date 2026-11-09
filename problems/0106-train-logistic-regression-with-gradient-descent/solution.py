import numpy as np

def train_logreg(X: np.ndarray, y: np.ndarray, learning_rate: float, iterations: int) -> tuple[list[float], ...]:
	"""
	Gradient-descent training algorithm for logistic regression, optimizing parameters with Binary Cross Entropy loss.
	"""
	Xb = np.hstack([np.ones((X.shape[0], 1)), X])
	N, D = Xb.shape

	# Initialise all parameters to zero
	theta = np.zeros(D)
	losses = []

	for _ in range(iterations):
	    # Prediction
		z = Xb@theta
		y_hat = 1.0/(1.0 + np.exp(-z))
		loss = -np.sum(y*np.log(y_hat) + (1-y)* np.log(1-y_hat))
		losses.append(loss)
		# Gradient descent update (no 1/N factor)
		grad = Xb.T @ (y_hat - y)
		theta = theta - learning_rate * grad

	coefficients = [round(float(t), 4) for t in theta]
	losses = [round(float(l), 4) for l in losses]
	return coefficients, losses
	pass