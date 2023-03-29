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
    data_norp_tim_valid,
    data_norp_fi_peak,
    data_norp_freq,
    data_norp_peak_time,
):
    """
    Parameters
    ----------
    data_norp_tim_valid : array
        Valid time array of NoRP data.
    data_norp_fi_peak : array
        Quiet sun flux array of NoRP data.
    data_norp_freq : array
        Freq array of NoRP data.
    data_norp_peak_time : string
        Peak time string.

    Returns
    -------
    None.
    """
    # Gain peak value time array index
    peak, peak_gap, gap = (
        np.where(data_norp_tim_valid == data_norp_peak_time)[0][0],
        300,
        100,
    )
    # Plot data range limiter at +- 30s
    peak_start, peak_end = (
        max(0, peak - peak_gap),
        min(data_norp_fi_peak.shape[0], peak + peak_gap),
    )

    # Plot with loops
    [
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
    plt.ylabel("Valid NoRP quiet sun filtered flux", fontsize=14)
    plt.title("NoRP quiet sun time evolution", fontsize=16)
    plt.legend(fontsize=10)
    plt.savefig("figure_norp.png")
    plt.show()


# RSTN log log plotter - flux vs freq at each time - 200 index = 190 s
def rstn_log_plotter(
    data_apl_tim,
    data_phf_tim,
    data_apl_fi_peak,
    data_phf_fi_peak,
    data_apl_freq,
    data_phf_freq,
    data_norp_peak_time,
):
    """
    Parameters
    ----------
    data_apl_tim : array
        Time array of apl of RSTN data.
    data_phf_tim : array
        Time array of phf of RSTN data.
    data_apl_fi_peak : array
        Quiet sun flux array of apl of RSTN data.
    data_phf_fi_peak : array
        Quiet sun flux array of apl of RSTN data.
    data_apl_freq : array
        Freq array of apl of RSTN data.
    data_phf_freq : array
        Freq array of apl of RSTN data.
    data_norp_peak_time : string
        Peak time indicator string from NoRP data.

    Returns
    -------
    None.
    """
    # Plot range limiter
    peak_apl, peak_phf, peak_gap, gap = (
        np.where(data_apl_tim == data_norp_peak_time)[0][0],
        np.where(data_phf_tim == data_norp_peak_time)[0][0],
        30,
        15,
    )
    peak_apl_start, peak_apl_end, peak_phf_start, peak_phf_end = (
        max(0, peak_apl - peak_gap),
        min(data_apl_fi_peak.shape[0], peak_apl + peak_gap),
        max(0, peak_phf - peak_gap),
        min(data_phf_fi_peak.shape[0], peak_phf + peak_gap),
    )

    # Plot generation
    # Plot apl with loops
    [
        plt.plot(
            data_apl_freq,
            np.mean(
                data_apl_fi_peak[i : i + gap], axis=0
            ),  # Mean data calculator
            label=data_apl_tim[i],
        )
        # for i in range(0, data_norp_fi_peak.shape[0], 100)
        for i in range(peak_apl_start, peak_apl_end, gap)
    ]
    # Plot phf with loops
    [
        plt.plot(
            data_phf_freq,
            np.mean(
                data_phf_fi_peak[i : i + gap], axis=0
            ),  # Mean data calculator
            label=data_phf_tim[i],
        )
        # for i in range(0, data_norp_fi_peak.shape[0], 100)
        for i in range(peak_phf_start, peak_phf_end, gap)
    ]

    # Plot axis scale definer
    plt.xscale("log")
    plt.yscale("log")

    # Plot customizations
    plt.xlabel("RSTN frequencies", fontsize=14)
    plt.ylabel("Valid RSTN quiet sun filtered flux", fontsize=14)
    plt.title("RSTN quiet sun time evolution", fontsize=16)
    plt.legend(fontsize=10)
    plt.savefig("figure_rstn.png")
    plt.show()


# Combined plotter
def log_plotter(
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
):
    """
    Parameters
    ----------
    data_norp_tim_valid : array
        Valid time array of NoRP data.
    data_apl_tim : array
        Time array of apl of RSTN data.
    data_phf_tim : array
        Time array of phf of RSTN data.
    data_norp_fi_peak : array
        Quiet sun flux array of NoRP data.
    data_apl_fi_peak : array
        Quiet sun flux array of apl of RSTN data.
    data_phf_fi_peak : array
        Quiet sun flux array of apl of RSTN data.
    data_norp_freq : array
        Freq array of NoRP data.
    data_apl_freq : array
        Freq array of apl of RSTN data.
    data_phf_freq : array
        Freq array of apl of RSTN data.
    data_norp_peak_time : string
        Peak time indicator string from NoRP data.

    Returns
    -------
    None.

    """
    # Plot range calculator
    # Plot range limiter
    peak, peak_apl, peak_phf = (
        np.where(data_norp_tim_valid == data_norp_peak_time)[0][0],
        np.where(data_apl_tim == data_norp_peak_time)[0][0],
        np.where(data_phf_tim == data_norp_peak_time)[0][0],
    )
    # Plot interval identifier
    peak_norp_gap, peak_rstn_gap, gap_norp, gap_rstn = (
        300,
        30,
        100,
        10,
    )
    # Plot x-axis range limiter
    (
        peak_start,
        peak_end,
        peak_apl_start,
        peak_apl_end,
        peak_phf_start,
        peak_phf_end,
    ) = (
        max(0, peak - peak_norp_gap),
        min(data_norp_fi_peak.shape[0], peak + peak_norp_gap),
        max(0, peak_apl - peak_rstn_gap),
        min(data_apl_fi_peak.shape[0], peak_apl + peak_rstn_gap),
        max(0, peak_phf - peak_rstn_gap),
        min(data_phf_fi_peak.shape[0], peak_phf + peak_rstn_gap),
    )

    # Plot generation
    # Plot norp with loops
    [
        plt.plot(
            data_norp_freq,
            np.mean(
                data_norp_fi_peak[i : i + gap_norp], axis=0
            ),  # Mean data calculator
            label=data_norp_tim_valid[i],
        )
        # for i in range(0, data_norp_fi_peak.shape[0], 100)
        for i in range(peak_start, peak_end, gap_norp)
    ]
    # Plot apl with loops
    [
        plt.plot(
            data_apl_freq,
            np.mean(
                data_apl_fi_peak[i : i + gap_rstn], axis=0
            ),  # Mean data calculator
            label=data_apl_tim[i],
        )
        # for i in range(0, data_norp_fi_peak.shape[0], 100)
        for i in range(peak_apl_start, peak_apl_end, gap_rstn)
    ]
    # Plot phf with loops
    [
        plt.plot(
            data_phf_freq,
            np.mean(
                data_phf_fi_peak[i : i + gap_rstn], axis=0
            ),  # Mean data calculator
            label=data_phf_tim[i],
        )
        # for i in range(0, data_norp_fi_peak.shape[0], 100)
        for i in range(peak_phf_start, peak_phf_end, gap_rstn)
    ]

    # Plot axis scale definer
    plt.xscale("log")
    plt.yscale("log")

    # Plot customizations
    plt.xlabel("Combined NoRP and RSTN frequencies", fontsize=14)
    plt.ylabel("Valid quiet sun filtered flux", fontsize=14)
    plt.title("Combined quiet sun time evolution", fontsize=16)
    plt.legend(fontsize=10)
    plt.savefig("figure_combined.png")
    plt.show()


# Plot parser
def generator(arg1, arg2, arg3):
    """
    Parameters
    ----------
    arg1 : tuple
        Argument for function 1.
    arg2 : tuple
        Argument for function 2.

    Returns
    -------
    result :
        The function calls.
    """
    # Parse arguments with unpacking
    result = (
        norp_log_plotter(*arg1),
        rstn_log_plotter(*arg2),
        log_plotter(*arg3),
    )
    # Plotter results return
    return result
