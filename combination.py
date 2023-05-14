import numpy as np 
from numpy.typing import NDArray

# implement your function to combine two numpy arrays 

def combination(arr1: NDArray, arr2: NDArray, axis=0):
    arr1 = arr1.squeeze()
    arr2 = arr2.squeeze()
    
    if len(arr1.shape) != len(arr2.shape):
        raise ValueError(f"cannot combine arrays along axis {axis}, wrong dimensions")

    return np.concatenate((arr1, arr2), axis=axis)

if __name__ == "__main__":
    pass
