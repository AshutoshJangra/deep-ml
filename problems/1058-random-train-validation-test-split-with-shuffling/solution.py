import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    # make a index array
    # shuffle
    # split indices
    # filter on split indices
    ia = np.arange(len(data))

    sia = np.random.default_rng(seed).permutation(data)

    trainidx = int(len(sia) * train_frac)

    validx = trainidx + int(len(sia) * validation_frac)

    return [sia[:trainidx] , sia[trainidx : validx], sia[validx:]]
    pass