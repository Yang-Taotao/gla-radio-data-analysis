"""
This is the data handler script of the radio data analysis project.

Created on Tue Mar 28 2023

@author: Yang-Taotao
"""
# Library import
import numpy as np
from data_reader import csv_loader

# Combined data loader
def data_loader(data_norp_path, data_apl_path, data_phf_path):
    """
    Parameters
    ----------
    data_norp_path : string
        Path to NORP data folder.
    data_apl_path : string
        Path to RSTN apl file folder.
    data_phf_path : string
        Path to RSTN phf file folder.

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
        csv_loader(data_norp_path + "fi.csv"),
        csv_loader(data_norp_path + "freq.csv"),
        csv_loader(data_norp_path + "mvd.csv", dtype=int),
        csv_loader(data_norp_path + "tim.csv", dtype=np.uint64),
        csv_loader(data_apl_path + "flux.csv").transpose(),
        csv_loader(data_apl_path + "freq.csv"),
        csv_loader(data_apl_path + "tim.csv", dtype=np.uint64),
        csv_loader(data_phf_path + "flux.csv").transpose(),
        csv_loader(data_phf_path + "freq.csv"),
        csv_loader(data_phf_path + "tim.csv", dtype=np.uint64),
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
def data_filter(data_norp_mvd, data_norp_tim, data_norp_fi):
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
def quiet_sun(data_array):
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
    # Calculate mean flux from all freq specific valid flux values
    data_fi_quiet = np.mean(data_array, axis=0)
    # Take out the quiet sun background from the valid flux values
    data_fi_peak = data_array - data_fi_quiet
    # Return flux result with quiet sun subtracted
    return data_fi_peak
