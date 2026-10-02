import numpy as np

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.
    
    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'
        
    Returns:
        2D numpy array with missing values imputed
    """
    data = data.copy()

    if strategy ==  'mean':
      values = np.nanmean(data, axis=0)


    
    elif  strategy ==  'median':
        values  =  np.nanmedian(data,axis = 0)


    elif strategy == 'mode':
        values = []
        for col in range(data.shape[1]):
            columns = data[:,col]
            columns =  columns[~np.isnan(columns)]   

            unique,counts  = np.unique(columns,return_counts = True)
            mode = unique[np.argmax(counts)]
            values.append(mode)

        values = np.asarray(values)

    rows,cols = np.where(np.isnan(data))
    for row,col in zip(rows,cols):
        data[row,col]  = values[col]

    return data    




      

      



    pass