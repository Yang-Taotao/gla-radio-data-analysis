"""
This is the RSTN data handler script of the radio data analysis project.

Created on Wed Mar 15 2023

@author: Yang-Taotao
"""
# Library import
import numpy as np
from data_reader import csv_loader

# RSTN data loader
def rstn_loader(data_apl_path, data_phf_path):
    """
    Parameters
    ----------
    data_apl_path : string
        Path to RSTN apl file folder.
    data_phf_path : string
        Path to RSTN phf file folder.

    Returns
    -------
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
    # Load into arrays
    (
        data_apl_flux,  # Flux of apl - Learmonth data
        data_apl_freq,  # Freq of apl - Learmonth data
        data_apl_tim,  # Time of apl - Learmonth data
        data_phf_flux,  # Flux of apl - Palehua data
        data_phf_freq,  # Freq of apl - Palehua data
        data_phf_tim,  # Time of apl - Palehua data
    ) = (
        csv_loader(data_apl_path + "flux.csv").transpose(),  # Dimension fix
        csv_loader(data_apl_path + "freq.csv"),
        csv_loader(data_apl_path + "tim.csv", dtype=np.uint64),
        csv_loader(data_phf_path + "flux.csv").transpose(),  # Dimension fix
        csv_loader(data_phf_path + "freq.csv"),
        csv_loader(data_phf_path + "tim.csv", dtype=np.uint64),
    )
    # Return func call
    return (
        data_apl_flux,
        data_apl_freq,
        data_apl_tim,
        data_phf_flux,
        data_phf_freq,
        data_phf_tim,
    )


# RSTN quiet sun flux data calculator
def rstn_quiet_sun(data_apl_flux, data_phf_flux):
    """
    Parameters
    ----------
    data_apl_flux : array
        Flux array of apl data of RSTN.
    data_phf_flux : array
        Flux array of phf data of RSTN.

    Returns
    -------
    data_apl_flux_peak : array
        Quiet sun flux array of apl data of RSTN.
    data_phf_flux_peak : array
        Quiet sun flux array of phf data of RSTN.
    """
    # Calculate mean flux from all freq specific valid flux values
    data_apl_flux_quiet, data_phf_flux_quiet = (
        np.mean(data_apl_flux, axis=0),
        np.mean(data_phf_flux, axis=0),
    )
    # Take out the quiet sun background from the valid flux values
    data_apl_flux_peak, data_phf_flux_peak = (
        data_apl_flux - data_apl_flux_quiet,
        data_phf_flux - data_phf_flux_quiet,
    )
    # Return func call
    return (data_apl_flux_peak, data_phf_flux_peak)
