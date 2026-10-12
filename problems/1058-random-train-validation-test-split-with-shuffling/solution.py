import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    # Your code here
    n = len(data)
    shuffled_indices = np.random.default_rng(seed).permutation(n)
    train_end = int(train_frac * n)
    validation_end = int(validation_frac * n) + train_end
    train_indices = shuffled_indices[:train_end]
    validation_indices = shuffled_indices[train_end:validation_end]
    test_indices = shuffled_indices[validation_end:]
    train_data = data[train_indices]
    validation_data = data[validation_indices]
    test_data = data[test_indices]
    return train_data, validation_data, test_data
    pass