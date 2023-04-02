"""
This is the data plotter script of the radio data analysis project.

Created on Wed Mar 15 2023

@author: Yang-Taotao
"""
# %% Library import
# Library import
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

# Custom module import
from data_fitter import gyro_model, plas_model

# %%  Plot style config
# Plot style configuration
plt.style.use(["science", "notebook", "grid"])

# %% NoRP plotter
# NoRP log log plotter - flux vs freq at each time - 100 index = 10 s
def norp_plotter(arg):
    """
    Parameters
    ----------
    arg : tuple
        Plotter argument parameters.

    Returns
    -------
    None.
    """
    # Local variable repo
    (
        data_norp_tim_valid,
        data_norp_fi_peak,
        data_norp_freq,
        data_norp_peak_time,
    ) = [arg[i] for i in range(len(arg))]

    # Plot range limiter
    # Gain peak value time array index
    peak = (
        np.where(data_norp_tim_valid == data_norp_peak_time)[0][0],  # peak
        300,  # peak_gap
        150,  # gap
    )
    # Plot data range limiter at +- 30s --> peak_gap >= 300
    # Structure - (peak_start, peak_end)
    peak_idx = (
        max(0, peak[0] - peak[1]),  # peak_start
        min(data_norp_fi_peak.shape[0], peak[0] + peak[1]),  # peak_end
    )

    # Plot with loops
    plt_0 = [
        plt.plot(
            data_norp_freq,
            np.mean(
                data_norp_fi_peak[i : i + peak[2]], axis=0
            ),  # Mean data calculator
            "+-",
            markersize=10,
            label="NoRP " + data_norp_tim_valid[i],
        )
        for i in range(peak_idx[0], peak_idx[1], peak[2])
    ]

    # Plot axis scale definer
    plt.xscale("log")
    plt.yscale("log")

    # Plot customizations
    plt.xlabel("NoRP frequencies (GHz)", fontsize=14)
    plt.ylabel("Valid NoRP quiet sun filtered flux", fontsize=14)
    plt.title("NoRP quiet sun time evolution", fontsize=16)
    plt.legend(fontsize=10)
    plt.savefig("./media/figure_01_norp.png")
    plt.close()

    # Return function call
    return (plt_0)


# %% RSTN plotter
# RSTN log log plotter - flux vs freq at each time - 200 index = 190 s
def rstn_plotter(arg):
    """
    Parameters
    ----------
    arg : tuple
        Plotter argument parameters.

    Returns
    -------
    None.
    """
    # Local variable repo
    (
        data_apl_tim,
        data_phf_tim,
        data_apl_fi_peak,
        data_phf_fi_peak,
        data_apl_freq,
        data_phf_freq,
        data_norp_peak_time,
    ) = [arg[i] for i in range(len(arg))]

    # Plot range limiter
    # Gain peak value time array index
    peak = (
        np.where(data_apl_tim == data_norp_peak_time)[0][0],  # peak_apl
        np.where(data_phf_tim == data_norp_peak_time)[0][0],  # peak_phf
        60,  # peak_gap
        60,  # gap
    )
    # Plot data range limiter at +- 30s
    peak_idx = (
        max(0, peak[0] - peak[2]),  # peak_apl_start
        min(data_apl_fi_peak.shape[0], peak[0] + peak[2]),  # peak_apl_end
        max(0, peak[1] - peak[2]),  # peak_phf_start
        min(data_phf_fi_peak.shape[0], peak[1] + peak[2]),  # peak_phf_end
    )

    # Plot generation
    # Plot apl with loops
    plt_0 = [
        plt.plot(
            data_apl_freq,
            np.mean(
                data_apl_fi_peak[i : i + peak[3]], axis=0
            ),  # Mean data calculator
            "x-",
            markersize=10,
            label="RSTN_apl " + data_apl_tim[i],
        )
        for i in range(peak_idx[0], peak_idx[1], peak[3])
    ]
    # Plot phf with loops
    plt_1 = [
        plt.plot(
            data_phf_freq,
            np.mean(
                data_phf_fi_peak[i : i + peak[3]], axis=0
            ),  # Mean data calculator
            "o-",
            markerfacecolor="none",
            markersize=10,
            label="RSTN_phf " + data_phf_tim[i],
        )
        for i in range(peak_idx[2], peak_idx[3], peak[3])
    ]

    # Plot axis scale definer
    plt.xscale("log")
    plt.yscale("log")

    # Plot customizations
    plt.xlabel("RSTN frequencies (GHz)", fontsize=14)
    plt.ylabel("Valid RSTN quiet sun filtered flux", fontsize=14)
    plt.title("RSTN quiet sun time evolution", fontsize=16)
    plt.legend(fontsize=10)
    plt.savefig("./media/figure_02_rstn.png")
    plt.close()

    # Return function call
    return (plt_0, plt_1)


# %% Combined plotter
# Combined plotter
def log_plotter(arg):
    """
    Parameters
    ----------
    arg : tuple
        Plotter argument parameters.

    Returns
    -------
    None.
    """
    # Local variable repo
    (
        data_norp_tim_valid,
        data_apl_tim,
        data_phf_tim,
        data_norp_fi_peak,
        data_apl_fi_peak,
        data_phf_fi_peak,
        data_norp_freq,
        data_apl_freq,
        data_phf_freq,
        data_norp_peak_time,
    ) = [arg[i] for i in range(len(arg))]

    # Plot range limiter
    # Gain peak value time array index
    peak = (
        np.where(data_norp_tim_valid == data_norp_peak_time)[0][0],  # peak
        np.where(data_apl_tim == data_norp_peak_time)[0][0],  # peak_apl
        np.where(data_phf_tim == data_norp_peak_time)[0][0],  # peak_phf
        300,  # peak_norp_gap
        60,  # peak_rstn_gap
        150,  # gap_norp
        60,  # gap_rstn
    )
    # Plot data range limiter at +- 30s
    peak_idx = (
        max(0, peak[0] - peak[3]),  # peak_start
        min(data_norp_fi_peak.shape[0], peak[0] + peak[3]),  # peak_end
        max(0, peak[1] - peak[4]),  # peak_apl_start
        min(data_apl_fi_peak.shape[0], peak[1] + peak[4]),  # peak_apl_end
        max(0, peak[2] - peak[4]),  # peak_phf_start
        min(data_phf_fi_peak.shape[0], peak[2] + peak[4]),  # peak_phf_end
    )

    # Plot generation
    # Plot norp with loops
    plt_0 = [
        plt.plot(
            data_norp_freq,
            np.mean(
                data_norp_fi_peak[i : i + peak[5]], axis=0
            ),  # Mean data calculator
            "+-",
            markersize=10,
            label="NoRP " + data_norp_tim_valid[i],
        )
        for i in range(peak_idx[0], peak_idx[1], peak[5])
    ]
    # Plot apl with loops
    plt_1 = [
        plt.plot(
            data_apl_freq,
            np.mean(
                data_apl_fi_peak[i : i + peak[6]], axis=0
            ),  # Mean data calculator
            "x-",
            markersize=10,
            label="RSTN_apl " + data_apl_tim[i],
        )
        for i in range(peak_idx[2], peak_idx[3], peak[6])
    ]
    # Plot phf with loops
    plt_2 = [
        plt.plot(
            data_phf_freq,
            np.mean(
                data_phf_fi_peak[i : i + peak[6]], axis=0
            ),  # Mean data calculator
            "o-",
            markerfacecolor="none",
            markersize=10,
            label="RSTN_phf " + data_phf_tim[i],
        )
        for i in range(peak_idx[4], peak_idx[5], peak[6])
    ]

    # Plot axis scale definer
    plt.xscale("log")
    plt.yscale("log")

    # Plot customizations
    plt.xlabel("Combined NoRP and RSTN frequencies (GHz)", fontsize=14)
    plt.ylabel("Quiet sun filtered flux (SFU)", fontsize=14)
    plt.title("Combined quiet sun time evolution", fontsize=16)
    plt.legend(fontsize=10)
    plt.savefig("./media/figure_03_combined.png")
    plt.close()

    # Return function call
    return (plt_0, plt_1, plt_2)


# %% Combined peak time plotter
# Combined peak time plotter
def log_avg_plotter(arg):
    """
    Parameters
    ----------
    arg : tuple
        Plotter argument parameters.

    Returns
    -------
    None.
    """
    # Local variable repo
    (
        data_norp_tim_valid,
        data_apl_tim,
        data_phf_tim,
        data_norp_fi_peak,
        data_apl_fi_peak,
        data_phf_fi_peak,
        data_norp_freq,
        data_apl_freq,
        data_phf_freq,
        data_norp_peak_time,
    ) = [arg[i] for i in range(len(arg))]

    # Plot range limiter
    # Gain peak value time array index
    peak = (
        np.where(data_norp_tim_valid == data_norp_peak_time)[0][0],  # peak
        np.where(data_apl_tim == data_norp_peak_time)[0][0],  # peak_apl
        np.where(data_phf_tim == data_norp_peak_time)[0][0],  # peak_phf
        300,  # peak_norp_gap
        60,  # peak_rstn_gap
        150,  # gap_norp
        60,  # gap_rstn
    )
    # Plot data range limiter at +- 30s
    peak_idx = (
        max(0, peak[0] - peak[3]),  # peak_start
        min(data_norp_fi_peak.shape[0], peak[0] + peak[3]),  # peak_end
        max(0, peak[1] - peak[4]),  # peak_apl_start
        min(data_apl_fi_peak.shape[0], peak[1] + peak[4]),  # peak_apl_end
        max(0, peak[2] - peak[4]),  # peak_phf_start
        min(data_phf_fi_peak.shape[0], peak[2] + peak[4]),  # peak_phf_end
    )

    # Generate peak time averaged data array
    data_norp_peak_avg, data_apl_peak_avg, data_phf_peak_avg = (
        data_norp_fi_peak[peak_idx[0] : peak_idx[1], :],
        data_apl_fi_peak[peak_idx[2] : peak_idx[3], :],
        data_phf_fi_peak[peak_idx[4] : peak_idx[5], :],
    )

    # Plot generation
    # Plot norp with loops
    plt.plot(
        data_norp_freq,
        np.mean(data_norp_peak_avg, axis=0),
        "+-",
        markersize=10,
        label="NoRP " + data_norp_tim_valid[peak[0]],
    )
    # Plot apl with loops
    plt.plot(
        data_apl_freq,
        np.mean(data_apl_peak_avg, axis=0),
        "x-",
        markersize=10,
        label="RSTN_apl " + data_apl_tim[peak[1]],
    )
    # Plot phf with loops
    plt.plot(
        data_phf_freq,
        np.mean(data_phf_peak_avg, axis=0),
        "o-",
        markerfacecolor="none",
        markersize=10,
        label="RSTN_phf " + data_phf_tim[peak[2]],
    )

    # Plot axis scale definer
    plt.xscale("log")
    plt.yscale("log")

    # Plot customizations
    plt.xlabel("Combined NoRP and RSTN frequencies (GHz)", fontsize=14)
    plt.ylabel("Valid quiet sun filtered flux", fontsize=14)
    plt.title("Combined quiet sun at peak time", fontsize=16)
    plt.legend(fontsize=10)
    plt.savefig("./media/figure_03_peak_average_combined.png")
    plt.close()

    # Return averaged flux array at peak time
    return (data_norp_peak_avg, data_apl_peak_avg, data_phf_peak_avg)


# %% Peak plotter
# Peak time plotter
def peak_plotter(arg):
    """
    Parameters
    ----------
    arg : tuple
        Peak plotter argument with freq, flux, and peak time.

    Returns
    -------
    None.

    """
    # Local variable repo
    (
        data_peak_freq, 
        data_peak_flux, 
        data_norp_peak_time, 
        gyro_param, 
        plas_param,
     ) = [arg[i] for i in range(len(arg))]
    
    # Fitted function repo
    data_gyro, data_plas = (
        gyro_model(data_peak_freq, *gyro_param),
        plas_model(data_peak_freq, *plas_param),
    )

    # Plot generation
    plt_0 = plt.plot(
        data_peak_freq,
        data_peak_flux,
        ".",
        markersize=10,
        markeredgecolor="black",
        label=data_norp_peak_time,
    )
    # Gyro fit curve
    plt_1 = plt.plot(
        data_peak_freq,
        data_gyro,
        "+--",
        markersize=10,
        markeredgecolor="red",
        label=data_gyro,
    )
    # Plas fit curve
    plt_2 = plt.plot(
        data_peak_freq,
        data_plas,
        "x--",
        markersize=10,
        markeredgecolor="blue",
        label=data_plas,
    )

    # Plot axis scale definer
    plt.xscale("log")
    plt.yscale("log")

    # Plot customizations
    plt.xlabel("Combined frequencies at peak time (GHz)", fontsize=14)
    plt.ylabel("Valid quiet sun filtered flux (SFU)", fontsize=14)
    plt.title("Combined quiet sun flux at peak time with curve fit", fontsize=16)
    plt.legend(fontsize=10)
    plt.savefig("./media/figure_03_peak_time.png")
    plt.close()

    # Return function call
    return (plt_0, plt_1, plt_2)


# %% Plot generator
# Define generator function
def plot_generator(arg):
    """
    Parameters
    ----------
    arg : array
        Plot generator argument with sub plotter arguments.

    Returns
    -------
    results : None
        A collection of plots.
    """
    # Local variable repo
    arg_norp, arg_rstn, arg_combine, arg_peak = [
        arg[i] for i in range(len(arg))
    ]

    # Result compilation
    results = (
        norp_plotter(arg_norp),
        rstn_plotter(arg_rstn),
        log_plotter(arg_combine),
        log_avg_plotter(arg_combine),
        peak_plotter(arg_peak),
    )

    # Return function call
    return results
