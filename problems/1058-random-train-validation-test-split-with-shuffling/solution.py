import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    # make a index array
    # shuffle - never shuffle the original data 
    # split indices
    # filter on split indices
    n = len(data)
    si = np.random.default_rng(seed).permutation(n)

    train_end = int(n * train_frac)
    val_end = train_end + int(n * validation_frac)

    ta = si[ : train_end]
    va = si [ train_end : val_end]
    tta = si [ val_end :]

    return [ data[ta], data[va], data[tta]]
    pass