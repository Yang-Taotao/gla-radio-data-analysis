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
    # Plot with loops
    [
        plt.plot(data_norp_tim_valid, data_norp_fi_peak[:, i])
        for i in range(data_norp_fi_peak.shape[1])
    ]
    # Try plotting for the peak value here, need additional work
    # peak = np.where(data_norp_tim_valid == data_norp_peak_time)
    # plt.axvline(x=peak)
    # Plot customizations
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Valid flux negating quiet sun", fontsize=14)
    plt.title("NoRp quiet sun subtracted flux again time", fontsize=16)
    plt.show()
    # Return func call
    return None


# RSTN plotter - preliminary
def rstn_plotter(data_apl_tim, data_phf_tim, data_apl_flux_peak, data_phf_flux_peak):
    # Plot apl data with loops
    [
        plt.plot(data_apl_tim, data_apl_flux_peak[:, i])
        for i in range(data_apl_flux_peak.shape[1])
    ]
    # Plot phf data with loops
    [
        plt.plot(data_phf_tim, data_phf_flux_peak[:, i])
        for i in range(data_phf_flux_peak.shape[1])
    ]
    # Plot customizations
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Valid flux negating quiet sun", fontsize=14)
    plt.title("RSTN quiet sun subtracted flux again time", fontsize=16)
    plt.show()
    # Return func call
    return None

# Combined plotter - preliminary
# def combined_plotter():
#    return