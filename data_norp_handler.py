# Library import
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from data_loader import csv_loader

# Plot style configuration
plt.style.use(["science", "notebook", "no-latex"])

# NORP data loader


def norp_loader(data_norp_path):
    # Load into arrays
    (
        data_norp_day,  # Days since 1979-01-01
        data_norp_fi,   # Flux data at different freq
        data_norp_freq, # List of recorded freq
        data_norp_fv,   # ???
        data_norp_mvd,  # Data validit checker, share dimension with data_norp_fi
        data_norp_tim,  # Milliseconds since the day and days since 1979-01-01
    ) = (
        csv_loader(data_norp_path + "day.csv"),
        csv_loader(data_norp_path + "fi.csv"),
        csv_loader(data_norp_path + "freq.csv"),
        csv_loader(data_norp_path + "fv.csv"),
        csv_loader(data_norp_path + "mvd.csv", dtype=int),
        csv_loader(data_norp_path + "tim.csv", dtype=np.uint64),
    )

    # Return func call
    return (
        data_norp_day,
        data_norp_fi,
        data_norp_freq,
        data_norp_fv,
        data_norp_mvd,
        data_norp_tim,
    )


# NORP data filter based on mvd file


def norp_filter(data_norp_mvd, data_norp_tim, data_norp_fi): 
    # Generate valid data mask based on boolean readout over single rows
    data_norp_mask = np.all(data_norp_mvd.astype(bool), axis=1)
    # Filter the time and flux data through mask
    data_norp_tim_valid = data_norp_tim[data_norp_mask]
    data_norp_fi_valid = data_norp_fi[data_norp_mask]
    # Return func call
    return (data_norp_tim_valid, data_norp_fi_valid)


# NORP quiet sun flux data calculator


def norp_quiet_sun(data_norp_array):
    # Calculate mean flux from all valid flux values
    data_norp_fi_quiet = np.mean(data_norp_array, axis=0)
    # Take out the quiet sun background from the valid flux values
    data_norp_fi_peak = data_norp_array - data_norp_fi_quiet
    # Return func call
    return data_norp_fi_peak


