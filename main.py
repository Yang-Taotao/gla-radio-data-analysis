"""
This is the master script of the radio data analysis project.

Created on Wed Mar 15 2023

@author: Yang-Taotao
"""
# %% Custom module import
# Data handler import
from data_handler import loader, validator, quiet_sun, collector

# Data plotter import
from data_plotter import plot_generator

# Data fitter import
# from data_fitter import

# %% Key data assignment
# Assign norp, apl, and phf file path
data_path = ("./data/norp/", "./data/apl/", "./data/phf/")
# Assign the peaktime of flux recording
norp_peak_time = "2013-10-28 01:59:38"

# %% Data repo
# Deposit data arrays
(
    norp_fi,
    norp_freq,
    norp_mvd,
    norp_tim,
    apl_fi,
    apl_freq,
    apl_tim,
    phf_fi,
    phf_freq,
    phf_tim,
) = loader(data_path)
# Deposit norp validity filtered arrays
norp_tim_valid, norp_fi_valid = validator(norp_mvd, norp_tim, norp_fi)
# Deposit quiet sun result
norp_fi_peak, apl_fi_peak, phf_fi_peak = quiet_sun(
    (norp_fi_valid, apl_fi, phf_fi)
)

# %% Peak time array argument assignment
peak_arg = (
    norp_tim_valid, 
    apl_tim, 
    phf_tim, 
    norp_peak_time, 
    norp_freq, 
    apl_freq, 
    phf_freq,
    norp_fi_peak, 
    apl_fi_peak, 
    phf_fi_peak, 
)

# %% Peak time flux array repo
peak_time_freq, peak_time_flux = (
    collector(peak_arg)[0],
    collector(peak_arg)[1],
)

# %% Plotter argument assignment
# Plot arguments assignment
plt_arg1, plt_arg2, plt_arg3, plt_arg4 = (
    # NoRP plotter arguments
    (norp_tim_valid, norp_fi_peak, norp_freq, norp_peak_time),
    # RSTN plotter arguments
    (
        apl_tim,
        phf_tim,
        apl_fi_peak,
        phf_fi_peak,
        apl_freq,
        phf_freq,
        norp_peak_time,
    ),
    # Combined plotter arguments
    (
        norp_tim_valid,
        apl_tim,
        phf_tim,
        norp_fi_peak,
        apl_fi_peak,
        phf_fi_peak,
        norp_freq,
        apl_freq,
        phf_freq,
        norp_peak_time,
    ),
    # Peak time plotter arguments
    (peak_time_freq, peak_time_flux),
)

# %% Plot generation
# Generate plot with function calls
plot_generator(plt_arg1, plt_arg2, plt_arg3, plt_arg4)

