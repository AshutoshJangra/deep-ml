import numpy as np
def precision(y_true, y_pred):
    # formula = tp / tp+fp or correct / total positive
    correct = np.sum( (y_true == 1) & (y_pred == 1))
    total = np.sum( (y_pred == 1))

    if total == 0:
        return 0
    else: return correct/total
	pass
