"""
This is the NoRP data handler script of the radio data analysis project.

Created on Wed Mar 15 2023

@author: Yang-Taotao
"""
# Library import
import numpy as np
from data_loader import csv_loader

# NORP data loader
def norp_loader(data_norp_path):
    """
    Parameters
    ----------
    data_norp_path : string
        Path to NORP data folder.

    Returns
    -------
    data_norp_fi : array
        Flux array of NORP data.
    data_norp_freq : array
        Freq array of NORP data.
    data_norp_mvd : array
        Validity array of NORP data.
    data_norp_tim : array
        Time array of NORP data.
    """
    # Load into arrays
    (
        data_norp_fi,  # Flux data at different freq
        data_norp_freq,  # List of recorded freq
        data_norp_mvd,  # Data validit checker, same dimension with flux
        data_norp_tim,  # Milliseconds since the day, days since 1979-01-01
    ) = (
        csv_loader(data_norp_path + "fi.csv"),
        csv_loader(data_norp_path + "freq.csv"),
        csv_loader(data_norp_path + "mvd.csv", dtype=int),
        csv_loader(data_norp_path + "tim.csv", dtype=np.uint64),
    )

    # Return func call
    return (
        data_norp_fi,
        data_norp_freq,
        data_norp_mvd,
        data_norp_tim,
    )


# NORP data filter based on mvd file
def norp_filter(data_norp_mvd, data_norp_tim, data_norp_fi):
    """
    Parameters
    ----------
    data_norp_mvd : array
        Validity array of NORP data.
    data_norp_tim : array
        Time array of NORP data.
    data_norp_fi : array
        Flux array of NORP data.

    Returns
    -------
    data_norp_tim_valid : array
        Valid time array of NORP data.
    data_norp_fi_valid : array
        Valid flux array of NORP data.
    """
    # Generate valid data mask based on boolean readout over single rows
    data_norp_mask = np.all(data_norp_mvd.astype(bool), axis=1)
    # Filter the time and flux data through mask
    data_norp_tim_valid = data_norp_tim[data_norp_mask]
    data_norp_fi_valid = data_norp_fi[data_norp_mask]
    # Return func call
    return (data_norp_tim_valid, data_norp_fi_valid)


# NORP quiet sun flux data calculator
def norp_quiet_sun(data_norp_array):
    """
    Parameters
    ----------
    data_norp_array : array
        Flux array of NORP data.

    Returns
    -------
    data_norp_fi_peak : array
        Filtered quiet sun array of NORP data.
    """
    # Calculate mean flux from all freq specific valid flux values
    data_norp_fi_quiet = np.mean(data_norp_array, axis=0)
    # Take out the quiet sun background from the valid flux values
    data_norp_fi_peak = data_norp_array - data_norp_fi_quiet
    # Return func call
    return data_norp_fi_peak
