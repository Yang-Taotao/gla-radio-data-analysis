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
# NORP log log plotter - flux vs freq at each time - 100 index = 10 s
def norp_log_plotter(
    data_norp_tim_valid, data_norp_fi_peak, data_norp_peak_time, data_norp_freq
):
    """
    Parameters
    ----------
    data_norp_tim_valid : array
        DESCRIPTION.
    data_norp_fi_peak : array
        DESCRIPTION.
    data_norp_peak_time : array
        DESCRIPTION.
    data_norp_freq : array
        DESCRIPTION.

    Returns
    -------
    None.
    """
    # Gain peak value time array index
    peak, peak_gap, gap = (
        np.where(data_norp_tim_valid == data_norp_peak_time)[0][0],
        300,
        30,
    )

    # Plot data range limiter at +- 30s
    peak_start, peak_end = (
        max(0, peak - peak_gap),
        min(data_norp_fi_peak.shape[0], peak + peak_gap),
    )

    # Plot with loops
    plot = [
        plt.plot(
            data_norp_freq,
            np.mean(
                data_norp_fi_peak[i : i + gap], axis=0
            ),  # Mean data calculator
            label=data_norp_tim_valid[i],
        )
        # for i in range(0, data_norp_fi_peak.shape[0], 100)
        for i in range(peak_start, peak_end, gap)
    ]

    # Plot axis scale definer
    plt.xscale("log")
    plt.yscale("log")

    # Plot customizations
    plt.xlabel("NoRP frequencies", fontsize=14)
    plt.ylabel("Valid NoRP flux negating quiet sun", fontsize=14)
    plt.title("NORP quiet sun time evolution", fontsize=16)
    plt.legend(fontsize=10)
    plt.show()
    # Return func call
    return plot
