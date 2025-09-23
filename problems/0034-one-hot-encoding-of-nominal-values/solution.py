import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
    x = np.asarray(x)
    if np.issubdtype(x.dtype, np.integer):
        if n_col is None:
            n_col = x.max() + 1
        one_hot = np.zeros((x.size, n_col), dtype=float)
        one_hot[np.arange(x.size), x] = 1.0
        return one_hot
    
    # Case 2: Non-integer array (strings, etc.)
    else:
    # Map unique categories to integers
        categories, x_int = np.unique(x, return_inverse=True)
        
        if n_col is None:
            n_col = len(categories)
        
        one_hot = np.zeros((x_int.size, n_col), dtype=float)
        one_hot[np.arange(x_int.size), x_int] = 1.0
    
        return one_hot

	pass