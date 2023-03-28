"""
This is the data plotter script of the radio data analysis project.

Created on Wed Mar 15 2023

@author: Yang-Taotao
"""
# Library import
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

# Plot style configuration
plt.style.use(["science", "notebook", "grid"])

# Plotters
# NORP plotter
def norp_plotter(
    data_norp_tim_valid, data_norp_fi_peak, data_norp_peak_time, data_norp_freq
):
    # Plot with loops
    [
        plt.plot(
            data_norp_tim_valid,
            data_norp_fi_peak[:, i],
            label=data_norp_freq[i],
        )
        for i in range(data_norp_fi_peak.shape[1])
    ]

    # Plotting for the peak value
    plt.axvline(x=data_norp_peak_time, color="crimson", linestyle="--")

    # Gain peak value x-axis index
    peak = np.where(data_norp_tim_valid == data_norp_peak_time)[0][0]
    x_lim_left, x_lim_right = (
        data_norp_tim_valid[peak - 2000],
        data_norp_tim_valid[peak + 2000],
    )

    # Ticks declutter
    plt.xticks(data_norp_tim_valid[::500], rotation=90, fontsize=10)

    # Plot range limiter
    plt.xlim(x_lim_left, x_lim_right)
    plt.ylim(bottom=0)

    # Plot customizations
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Valid NoRP flux negating quiet sun", fontsize=14)
    plt.title("NoRP quiet sun subtracted flux against time", fontsize=16)
    plt.legend(fontsize=10)
    plt.show()
    # Return func call
    return None


# NORP log log plotter - 100 index = 10 s
def norp_log_plotter(
    data_norp_tim_valid, data_norp_fi_peak, data_norp_peak_time, data_norp_freq
):
    # Gain peak value time array index
    peak, peak_gap, gap = np.where(data_norp_tim_valid == data_norp_peak_time)[0][0], 300, 30

    # Plot data range limiter at /pm 30s
    peak_start, peak_end = (
        max(0, peak - peak_gap),
        min(data_norp_fi_peak.shape[0], peak + peak_gap),
    )
    
    # Plot with loops
    [
        plt.plot(
            data_norp_freq,
            np.mean(data_norp_fi_peak[i:i+gap], axis=0), # Mean data calculator
            label=data_norp_tim_valid[i],
        )
        #for i in range(0, data_norp_fi_peak.shape[0], 100)
        for i in range(peak_start, peak_end, gap) 
    ]
    
    # Plot axis scale definer
    plt.xscale('log')
    plt.yscale('log')

    # Plot customizations
    plt.xlabel("NoRP frequencies", fontsize=14)
    plt.ylabel("Valid NoRP flux negating quiet sun", fontsize=14)
    plt.title("NORP quiet sun time evolution", fontsize=16)
    plt.legend(fontsize=10)
    plt.show()
    # Return func call
    return None


# RSTN plotter - preliminary
def rstn_plotter(
    data_apl_tim,
    data_phf_tim,
    data_apl_flux_peak,
    data_phf_flux_peak,
    data_apl_freq,
    data_phf_freq,
):
    # Plot apl data with loops
    [
        plt.plot(
            data_apl_tim, data_apl_flux_peak[:, i], label=data_apl_freq[i]
        )
        for i in range(data_apl_flux_peak.shape[1])
    ]
    # Plot phf data with loops
    [
        plt.plot(
            data_phf_tim, data_phf_flux_peak[:, i], label=data_phf_freq[i]
        )
        for i in range(data_phf_flux_peak.shape[1])
    ]

    # Ticks declutter
    plt.xticks(data_apl_tim[::2000], rotation=90, fontsize=10)

    # Plot range limiter
    plt.ylim(bottom=0)

    # Plot customizations
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Valid RSTN flux negating quiet sun", fontsize=14)
    plt.title("RSTN quiet sun subtracted flux again time", fontsize=16)
    plt.legend(fontsize=10)
    plt.show()
    # Return func call
    return None


# Combined plotter - preliminary
def combined_plotter(
    data_norp_tim_valid,
    data_norp_fi_peak,
    data_norp_peak_time,
    data_apl_tim,
    data_phf_tim,
    data_apl_flux_peak,
    data_phf_flux_peak,
):
    # Plot with loops
    [
        plt.plot(data_norp_tim_valid, data_norp_fi_peak[:, i])
        for i in range(data_norp_fi_peak.shape[1])
    ]
    [
        plt.plot(data_apl_tim, data_apl_flux_peak[:, i])
        for i in range(data_apl_flux_peak.shape[1])
    ]
    [
        plt.plot(data_phf_tim, data_phf_flux_peak[:, i])
        for i in range(data_phf_flux_peak.shape[1])
    ]

    # Plotting for the peak value
    plt.axvline(x=data_norp_peak_time, color="crimson", linestyle="--")

    # Plot range limiter
    plt.ylim(bottom=0)

    # Plot customizations
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Valid flux negating quiet sun", fontsize=14)
    plt.title("Quiet sun subtracted flux again time", fontsize=16)
    plt.show()
    return None
