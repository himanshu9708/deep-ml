def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """
    dict = {}
    i = 0
    for i in range(len(order)):
        dict[order[i]] = i
        

    res = []
    for val in values:
        if val in dict:
            res.append(dict[val])
        else:
            res.append(-1)        
    
    return res
    pass