import numpy as np

# implement the function strange pattern

def strange_pattern(shape):
    array = np.zeros(shape, dtype=bool)
    array[::3, ::3] = True
    array[1::3, 2::3] = True
    array[2::3, 1::3] = True
    return array

if __name__ == "__main__":
    print(strange_pattern((0,0)))
