"""
This is the data loader script of the radio data analysis project.

Created on Wed Mar 15 2023

@author: Yang-Taotao
"""
# Library import
import datetime as dt
import numpy as np


# CSV data parser
def csv_loader(file_path, dtype=float):
    '''
    Parameters
    ----------
    file_path : string
        Path to file folder.
    dtype : dtype, optional
        The dtype of assigned file. The default is float.

    Returns
    -------
    data : array
        The data readout array.

    '''
    # Initial data load with specified dtype
    data = np.loadtxt(file_path, delimiter=",", dtype=dtype)

    # Time data loader and convertor
    if dtype == np.uint64:
        # Define start point of datetime as day01
        time_base = dt.datetime(1979, 1, 1) - dt.timedelta(days=1)
        # Construct time function for calculating time result
        time_repo = [
            time_base + dt.timedelta(milliseconds=ms + days * 86400000)
            for ms, days in data
        ]
        # Combined datetime data
        data = np.array(
            [dt.strftime("%Y-%m-%d %H:%M:%S") for dt in time_repo]
        )
        # Return converted time data array
        return data
    # Data loader for all other dtype
    return data
