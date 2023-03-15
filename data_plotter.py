# Library import
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from data_loader import csv_loader

# Plot style configuration
plt.style.use(["science", "notebook", "no-latex"])

# Plotters
# NORP plotter - Pending peak time plot and further customization


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


# RSTN plotter - preliminary