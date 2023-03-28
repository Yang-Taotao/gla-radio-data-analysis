"""
This is the NoRP data handler script of the radio data analysis project.

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
    data_main : dict
        A dictionary containing the following keys:
            - 'norp_fi': Flux array of NORP data.
            - 'norp_freq': Freq array of NORP data.
            - 'norp_mvd': Validity array of NORP data.
            - 'norp_tim': Time array of NORP data.
            - 'apl_flux': Flux array of apl data of RSTN.
            - 'apl_freq': Freq array of apl data of RSTN.
            - 'apl_tim': Time array of apl data of RSTN.
            - 'phf_flux': Flux array of phf data of RSTN.
            - 'phf_freq': Freq array of phf data of RSTN.
            - 'phf_tim': Time array of phf data of RSTN.
    """
    # Data dict init
    data_main = {}
    # Load data into dict
    (
        data_main['norp_fi'],
        data_main['norp_freq'],
        data_main['norp_mvd'],
        data_main['norp_tim'],
        data_main['apl_flux'],
        data_main['apl_freq'],
        data_main['apl_tim'],
        data_main['phf_flux'],
        data_main['phf_freq'],
        data_main['phf_tim'],
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
    
    # Return the dictionary
    return data_main


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
    data_norp_tim_valid = data_norp_tim[data_norp_mask]
    data_norp_fi_valid = data_norp_fi[data_norp_mask]
    # Return func call
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
    # Return func call
    return data_fi_peak
