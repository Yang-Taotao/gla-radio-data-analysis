"""
This is the data plotter legacy script of the radio data analysis project.

Created on Tue Mar 28 2023

@author: Yang-Taotao
"""
# Library import
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
# Custom module import
from data_fitter import gyro_model, plas_model

# Plot style configuration
plt.style.use(["science", "notebook", "grid"])

# Plotters
# NORP plotter - flux vs time at each freq
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


# %% Sepearate combined fit plotter
# Define fit plotter function
def fit_plotter(arg):
    # Local variable repo
    (
        data_norp_freq,
        data_apl_freq,
        data_phf_freq,
        data_peak_flux_norp, 
        data_peak_flux_apl, 
        data_peak_flux_phf,
        norp_gyro_param, 
        norp_plas_param, 
        apl_gyro_param, 
        apl_plas_param, 
        phf_gyro_param, 
        phf_plas_param,
    ) = [arg[i] for i in range(len(arg))]

    # Plot generation
    plt.plot(
        data_norp_freq,
        data_peak_flux_norp,
    )
    plt.plot(
        data_apl_freq,
        data_peak_flux_apl,
    )
    plt.plot(
        data_phf_freq,
        data_peak_flux_phf,
    )
    plt.plot(
        data_norp_freq,
        gyro_model(data_norp_freq, *norp_gyro_param),
    )
    plt.plot(
        data_norp_freq,
        plas_model(data_norp_freq, *norp_plas_param),
    )
    plt.plot(
        data_apl_freq,
        gyro_model(data_apl_freq, *apl_gyro_param),
    )
    plt.plot(
        data_apl_freq,
        plas_model(data_apl_freq, *apl_plas_param),
    )
    plt.plot(
        data_phf_freq,
        gyro_model(data_phf_freq, *phf_gyro_param),
    )
    plt.plot(
        data_phf_freq,
        plas_model(data_phf_freq, *phf_plas_param),
    )

    # Plot axis scale definer
    plt.xscale("log")
    plt.yscale("log")

    # Plot customizations
    plt.xlabel("Frequencies at peak time (GHz)", fontsize=14)
    plt.ylabel("Valid quiet sun filtered flux", fontsize=14)
    plt.title("Quiet sun flux at peak time", fontsize=16)
    plt.legend(fontsize=10)
    plt.savefig("./media/figure_fit.png")
    plt.close()