# Library import
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from data_loader import csv_loader

# NORP data loader
plt.style.use(["science", "notebook", "no-latex"])

def norp_loader(data_norp_path):
    # Date of observation data recording
    data_norp_day = csv_loader(data_norp_path + "day.csv")
    # Stokes I param (total flux) for each freq
    data_norp_fi = csv_loader(data_norp_path + "fi.csv")
    # List of observed freq
    data_norp_freq = csv_loader(data_norp_path + "freq.csv")
    # ?????
    data_norp_fv = csv_loader(data_norp_path + "fv.csv")
    # List of boolean val that checks if observations are valid
    data_norp_mvd = csv_loader(data_norp_path + "mvd.csv", dtype=int)
    # Specify time for recordings
    data_norp_tim = csv_loader(data_norp_path + "tim.csv", dtype=np.uint64)
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


def norp_filter(data_norp_path):
    # Read data into arrays
    data_norp_mvd = csv_loader(data_norp_path + "mvd.csv", dtype=int)
    data_norp_tim = csv_loader(data_norp_path + "tim.csv", dtype=np.uint64)
    data_norp_fi = csv_loader(data_norp_path + "fi.csv")
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


# NORP plotter


def norp_plotter(data_norp_tim_valid, data_norp_fi_peak, data_norp_peak_time):
    # Load the filtered time and flux data, as well as the defined peak time
    time_array, data_array, data_norp_peak_time = (
        data_norp_tim_valid,
        data_norp_fi_peak,
        data_norp_peak_time,
    )
    # Plot with loops
    [
        plt.plot(time_array[:, 0], data_array[:, i])
        for i in range(data_array.shape[1])
    ]
    # Try plotting for the peak value here, need additional work
    # peak = np.where(time_array == data_norp_peak_time)
    # plt.axvline(x=peak)
    # Plot customizations
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Valid flux negating quiet sun", fontsize=14)
    plt.title("Quiet sun subtracted flux again time", fontsize=16)
    plt.show()
    # Return func call
    return None
