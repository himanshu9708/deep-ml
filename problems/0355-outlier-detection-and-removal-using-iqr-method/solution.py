import numpy as np

def detect_outliers_iqr(data: list[float], k: float = 1.5) -> dict:
    """
    Detect and remove outliers using the IQR method.

    Args:
        data: List of numerical values
        k: IQR multiplier for determining outlier bounds

    Returns:
        Dictionary with cleaned_data, outlier_indices,
        lower_bound, upper_bound
    """

    data = np.asarray(data)

    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)

    # IQR = Q3 - Q1
    iqr = q3 - q1

    lower_bound = q1 - (k * iqr)
    upper_bound = q3 + (k * iqr)

    cleaned_data = []
    outlier_indices = []

    for i in range(len(data)):
        if lower_bound <= data[i] <= upper_bound:
            cleaned_data.append(data[i])
        else:
            outlier_indices.append(i)

    ans = {
        "cleaned_data": cleaned_data,
        "outlier_indices": outlier_indices,
        "lower_bound": lower_bound,
        "upper_bound": upper_bound
    }

    return ans
