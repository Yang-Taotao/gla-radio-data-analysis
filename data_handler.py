"""
This is the data handler script of the radio data analysis project.

Created on Tue Mar 28 2023

@author: Yang-Taotao
"""
# Library import
import numpy as np
from data_reader import csv_loader

# Combined data loader
def loader(data_path):
    """
    Parameters
    ----------
    data_path : tuple
        Tuple of data folder path.

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
    data_apl_flux : array
        Flux array of apl data of RSTN.
    data_apl_freq : array
        Freq array of apl data of RSTN.
    data_apl_tim : array
        Time array of apl data of RSTN.
    data_phf_flux : array
        Flux array of phf data of RSTN.
    data_phf_freq : array
        Freq array of phf data of RSTN.
    data_phf_tim : array
        Time array of phf data of RSTN.
    """
    # Local path variable repo
    flux, freq, mvd, tim = ("flux.csv", "freq.csv", "mvd.csv", "tim.csv")
    # Load data
    (
        data_norp_fi,
        data_norp_freq,
        data_norp_mvd,
        data_norp_tim,
        data_apl_flux,
        data_apl_freq,
        data_apl_tim,
        data_phf_flux,
        data_phf_freq,
        data_phf_tim,
    ) = (
        csv_loader(data_path[0] + flux),
        csv_loader(data_path[0] + freq),
        csv_loader(data_path[0] + mvd, dtype=int),
        csv_loader(data_path[0] + tim, dtype=np.uint64),
        csv_loader(data_path[1] + flux).transpose(),
        csv_loader(data_path[1] + freq),
        csv_loader(data_path[1] + tim, dtype=np.uint64),
        csv_loader(data_path[2] + flux).transpose(),
        csv_loader(data_path[2] + freq),
        csv_loader(data_path[2] + tim, dtype=np.uint64),
    )

    # Return the assignment
    return (
        data_norp_fi,  # Flux data at different freq
        data_norp_freq,  # List of recorded freq
        data_norp_mvd,  # Data validit checker, same dimension with flux
        data_norp_tim,  # Milliseconds since the day, days since 1979-01-01
        data_apl_flux,  # Flux of apl - Learmonth data
        data_apl_freq,  # Freq of apl - Learmonth data
        data_apl_tim,  # Time of apl - Learmonth data
        data_phf_flux,  # Flux of apl - Palehua data
        data_phf_freq,  # Freq of apl - Palehua data
        data_phf_tim,  # Time of apl - Palehua data
    )


# NORP data filter based on mvd file
def filter(data_norp_mvd, data_norp_tim, data_norp_fi):
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
    data_norp_tim_valid, data_norp_fi_valid = (
        data_norp_tim[data_norp_mask],
        data_norp_fi[data_norp_mask],
    )
    # Return filtered result
    return (data_norp_tim_valid, data_norp_fi_valid)


# Quiet sun calculator
def quiet_sun(data_array_tuple):
    """
    Parameters
    ----------
    data_array_tuple : tuple
        Flux array tuple.

    Returns
    -------
    data_array_repo : tuple
        Filtered quiet sun array data tuple.
    """
    # Loop through the arrays to generate quiet sun flux array tuple
    data_array_repo = tuple(
        [array - np.mean(array, axis=0) for array in data_array_tuple]
    )
    # Return quiet sun flux array tuple
    return data_array_repo


# Peak time index identifier
def peak_time(arg):
    """
    Parameters
    ----------
    data_array : array
        Flux array data.

    Returns
    -------
    data_fi_peak : array
        Filtered quiet sun array data.
    """
    # Local variable repo
    data_norp_tim_valid, data_apl_tim, data_phf_tim, data_norp_peak_time = (
        arg[0], arg[1], arg[2], arg[3],
    )
    # Index locator
    idx_norp, idex_apl, idx_phf = (
        np.where(data_norp_tim_valid == data_norp_peak_time)[0][0],
        np.where(data_apl_tim == data_norp_peak_time)[0][0],
        np.where(data_phf_tim == data_norp_peak_time)[0][0],
    )
    # Return index repo
    return idx_norp, idex_apl, idx_phf


# Peak time flux array collector
def collector(data_norp_fi_peak, data_apl_fi_peak, data_phf_fi_peak, arg):
    # Import peak identifier result
    idx_norp, idx_apl, idx_phf = peak_time(arg)
    # Generate new peak time flux array
    data_norp_fi_peak_time, data_apl_fi_peak_time, data_phf_fi_peak_time = (
        data_norp_fi_peak[idx_norp],
        data_apl_fi_peak[idx_apl],
        data_phf_fi_peak[idx_phf],
    )
    # Peak time flux array tuple generator
    data_fi_peak_time = tuple(
        [
            data_norp_fi_peak_time, 
            data_apl_fi_peak_time, 
            data_phf_fi_peak_time,
        ]
    )
    # Peak time flux array generator
    data_fi_peak_time_combined = np.concatenate(data_fi_peak_time)
    print(data_fi_peak_time_combined)
    # Return combined peak time flux array
    return data_fi_peak_time_combined
