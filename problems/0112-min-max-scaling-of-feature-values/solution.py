import numpy as np
def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here\
    min = np.min(x, axis=0)
    max = np.max(x, axis=0)
    range = max - min 
    range = np.where(range ==0 , 1 , range)
    
    return np.round((x - min) / range, 4)
    pass