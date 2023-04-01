"""
This is the data handler script of the radio data analysis project.

Created on Wed Mar 15 2023

@author: Yang-Taotao
"""
# %% Library import
# Library import
import numpy as np
from data_reader import csv_loader

# %% Data loader
# Combined data loader
def loader(data_path):
    """
    Parameters
    ----------
    data_path : tuple
        Tuple of data folder path.

    Returns
    -------
    result : tuple
        Tuple of loaded data arrays.
    """
    # Local path variable repo
    flux, freq, mvd, tim = ("flux.csv", "freq.csv", "mvd.csv", "tim.csv")

    # Pack data into tuple
    result = (
        csv_loader(data_path[0] + flux),
        csv_loader(data_path[0] + freq),
        csv_loader(data_path[0] + mvd, dtype=int),
        csv_loader(data_path[0] + tim, dtype=np.uint64),
        csv_loader(data_path[1] + flux).transpose(),
        csv_loader(data_path[1] + freq),
        csv_loader(data_path[1] + tim, dtype=np.uint64),
        csv_loader(data_path[2] + flux).transpose(),
        csv_loader(data_path[2] + freq),
        csv_loader(data_path[2] + tim, dtype=np.uint64),
    )

    # Return the assignment
    return result

# %% Data validator
# NORP data filter based on mvd file
def validator(data_norp_mvd, data_norp_tim, data_norp_fi):
    """
    Parameters
    ----------
    data_norp_mvd : array
        Validity array of NORP data.
    data_norp_tim : array
        Time array of NORP data.
    data_norp_fi : array
        Flux array of NORP data.

    Returns
    -------
    data_norp_tim_valid : array
        Valid time array of NORP data.
    data_norp_fi_valid : array
        Valid flux array of NORP data.
    """
    # Generate valid data mask based on boolean readout over single rows
    data_norp_mask = np.all(data_norp_mvd.astype(bool), axis=1)

    # Filter the time and flux data through mask
    data_norp_tim_valid, data_norp_fi_valid = (
        data_norp_tim[data_norp_mask],
        data_norp_fi[data_norp_mask],
    )

    # Return filtered result
    return (data_norp_tim_valid, data_norp_fi_valid)

# %% Quiet sun flux calculator
# Quiet sun calculator
def quiet_sun(data_array_tuple):
    """
    Parameters
    ----------
    data_array_tuple : tuple
        Flux array tuple.

    Returns
    -------
    data_array_repo : tuple
        Filtered quiet sun array data tuple.
    """
    # Loop through the arrays to generate quiet sun flux array tuple
    data_array_repo = tuple(
        array - np.mean(array, axis=0) for array in data_array_tuple
    )

    # Return quiet sun flux array tuple
    return data_array_repo

# %% Peak time array collector
# Peak time array collector
def collector(arg_time, arg_freq, arg_flux):
    """
    Parameters
    ----------
    arg_time : tuple
        Tuple of time and peak time data arrays.
    arg_freq : tuple
        Tuple of freq data arrays.
    arg_flux : tuple
        Tuple of flux data arrays.

    Returns
    -------
    data_fi_combined : array
        Peak time flux array combined.
    data_freq_combined : array
        Peak time freq array combined.
    """
    # Peak time index identifier and freq combiner
    def peak_time(arg_time):
        """
        Parameters
        ----------
        arg : tuple
            Tuple of time data arrays with peak time.

        Returns
        -------
        idx_norp : integer
            Index of NoRP peak time.
        idex_apl : integer
            Index of apl peak time.
        idx_phf : integer
            Index of phf peak time.
        data_freq_peak_time_combined : array
            Combined freq array.
        """
        # Local variable repo
        (
            data_norp_tim_valid,
            data_apl_tim,
            data_phf_tim,
            data_norp_peak_time,
        ) = [arg_time[i] for i in range(len(arg_time))]

        # Index locator
        idx_norp, idx_apl, idx_phf = (
            np.where(data_norp_tim_valid == data_norp_peak_time)[0][0],
            np.where(data_apl_tim == data_norp_peak_time)[0][0],
            np.where(data_phf_tim == data_norp_peak_time)[0][0],
        )

        # Return index repo
        return idx_norp, idx_apl, idx_phf

    # Peak time freq collector
    def peak_freq(arg_freq):
        # Local variable repo
        data_norp_freq, data_apl_freq, data_phf_freq = [
            arg_freq[i] for i in range(len(arg_freq))
        ]

        # Concatenate freq array
        data_freq = tuple(
            [
                data_norp_freq,
                data_apl_freq,
                data_phf_freq,
            ]
        )
        data_freq_combined = np.concatenate(data_freq)

        # Return combined freq array
        return data_freq_combined

    # Peak time flux collector
    def peak_flux(arg_flux):
        # Local variable repo
        data_norp_flux_peak, data_apl_flux_peak, data_phf_flux_peak = [
            arg_flux[i] for i in range(len(arg_flux))
        ]

        # Import peak identifier result
        idx_norp, idx_apl, idx_phf = peak_time(arg_time)

        # Pick peak time flux array out
        data_norp_flux_peak, data_apl_flux_peak, data_phf_flux_peak = (
            data_norp_flux_peak[idx_norp],
            data_apl_flux_peak[idx_apl],
            data_phf_flux_peak[idx_phf],
        )

        # Concatenate freq array
        data_flux = tuple(
            [
                data_norp_flux_peak,
                data_apl_flux_peak,
                data_phf_flux_peak,
            ]
        )
        data_flux_combined = np.concatenate(data_flux)

        # Return combined freq array
        return data_flux_combined

    # Peak time freq, flux array generator
    data_freq_combined, data_flux_combined = peak_freq(arg_freq), peak_flux(arg_flux)

    # Array sorter
    # Get numpy index sort array
    idx_sort = np.argsort(data_freq_combined)
    # Sort array with index
    data_freq_sorted, data_flux_sorted = (
        data_freq_combined[idx_sort],
        data_flux_combined[idx_sort],
    )

    # Array uniqe value filter
    # Get the unique freq values array
    data_freq_final = np.unique(data_freq_sorted)

    # Calculate the mean y values for each unique x value
    data_flux_final = np.zeros(len(data_freq_final))
    for i, xval in enumerate(data_freq_final):
        data_flux_final[i] = np.mean(data_flux_sorted[data_freq_sorted == xval])

    # Return combined peak time flux array
    return data_freq_final, data_flux_final
