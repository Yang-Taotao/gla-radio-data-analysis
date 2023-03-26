# Library import
import numpy as np
from data_loader import csv_loader

# RSTN data loader


def rstn_loader(data_apl_path, data_phf_path):
    # Load into arrays
    (
        data_apl_flux,  # Flux of apl - Learmonth data
        data_apl_freq,  # Freq of apl - Learmonth data
        data_apl_tim,   # Time of apl - Learmonth data
        data_phf_flux,  # Flux of apl - Palehua data
        data_phf_freq,  # Freq of apl - Palehua data
        data_phf_tim,   # Time of apl - Palehua data
    ) = (
        csv_loader(data_apl_path + "flux.csv"),
        csv_loader(data_apl_path + "freq.csv"),
        csv_loader(data_apl_path + "tim.csv", dtype=np.uint64),
        csv_loader(data_phf_path + "flux.csv"),
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