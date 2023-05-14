import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    if not (isinstance(loc, int) or isinstance(loc, float)):
        print(f"type of loc ist wrong")
        return 
    if not (isinstance(scale, int) or isinstance(scale, float)):
        print(f"type of scale ist wrong")
        return 
    if not (isinstance(lower_bound, int) or isinstance(lower_bound, float)):
        print(f"type of lower_bound ist wrong")
        return 
    if not (isinstance(upper_bound, int) or isinstance(upper_bound, float)):
        print(f"type of upper_bound ist wrong")
        return 
    if upper_bound <= lower_bound:
        print(f"upper_bound is smaller or equal to lower_bound")
        return 

    samples = np.random.normal(loc, scale, 100) 
    ubounded_samples = samples[samples <= upper_bound]
    bounded_samples = ubounded_samples[ubounded_samples >= lower_bound] 
    std = np.std(bounded_samples)
    mean = np.mean(bounded_samples) 
    return (mean, std)

if __name__ == "__main__":
    print(gaussian_analysis(0, 1, 2, 3))

