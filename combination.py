import numpy as np 
from numpy.typing import NDArray

# implement your function to combine two numpy arrays 

def combination(arr1: NDArray, arr2: NDArray, axis=0):
    arr1 = arr1.squeeze()
    arr2 = arr2.squeeze()
    
    if arr1.shape[:axis] != arr2.shape[:axis] or arr1.shape[axis+1:] != arr2.shape[axis+1:]:
        raise ValueError(f"cannot combine arrays along axis {axis}, wrong dimensions")

    return np.concatenate((arr1, arr2), axis=axis)

if __name__ == "__main__":
    pass
