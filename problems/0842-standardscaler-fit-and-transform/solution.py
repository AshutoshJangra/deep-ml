import numpy as np

class Standard_scalerc:
    def __init__(self):
        self.mean_ = None
        self.std_ = None
        self.is_fitted_ = False
    
    def fit(self, X):
        self.mean_ = np.mean(X, axis=0)
        self.std_ = np.std(X, axis=0)
        self.std_ = np.where(self.std_ == 0 , 1, self.std_)

        self.is_fitted_ = True
        return self
    
    def transform(self, Xs):
        if not self.is_fitted_:
            raise RuntimeError("scaler should be fit first")
        return (Xs - self.mean_)/ self.std_
    
    def fit_transform(self,X, Xs):
        return self.fit(X).transform(Xs)

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """
    Fit a standard scaler on X_train and transform X_test.
    Returns the standardized X_test as a numpy array.
    """
    scaler = Standard_scalerc()
    return scaler.fit_transform(X_train, X_test)
    pass
