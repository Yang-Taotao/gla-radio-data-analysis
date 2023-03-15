# Library import
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from data_loader import csv_loader

# Plot style configuration
plt.style.use(["science", "notebook", "no-latex"])

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