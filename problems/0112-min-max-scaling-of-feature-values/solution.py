import numpy as  np
def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    res = []
    x = np.asarray(x)
    min = np.min(x)
    max  =  np.max(x)
    for i in x:
        val = (i-min)/(max-min);
        res.append(val)

    return res    


    # Your code here
    