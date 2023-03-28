# %% Docstrings init
"""
This is the master script of the radio data analysis project.

Created on Wed Mar 15 2023

@author: Yang-Taotao
"""
# %% Library import
# Library import
# Data handler import
from data_handler import data_loader, data_filter, quiet_sun

# Data plotter import
from data_plotter import generator

# Data fitter import
# from data_fitter import gyro_fitter, plas_fitter

# %% Data repo
# Data path repo
# Assign norp, apl, and phf file path
norp_path, apl_path, phf_path = ("./data/norp/", "./data/apl/", "./data/phf/")
# Assign the peaktime of flux recording
norp_peak_time = "2013-10-28 01:59:38"

# Data repo
# Deposit data arrays
(
    norp_fi,
    norp_freq,
    norp_mvd,
    norp_tim,
    apl_flux,
    apl_freq,
    apl_tim,
    phf_flux,
    phf_freq,
    phf_tim,
) = data_loader(norp_path, apl_path, phf_path)
# Deposit norp validity filtered arrays
norp_tim_valid, norp_fi_valid = data_filter(norp_mvd, norp_tim, norp_fi)
# Deposit quiet sun result
norp_fi_peak, apl_fi_peak, phf_fi_peak = (
    quiet_sun(norp_fi_valid),
    quiet_sun(apl_flux),
    quiet_sun(phf_flux),
)

# %% Plotter
# Plot log-log plot of NORP data
# norp_log_plotter(norp_tim_valid, norp_fi_peak, norp_freq, norp_peak_time)
# rstn_log_plotter(apl_tim, phf_tim, apl_fi_peak, phf_fi_peak, apl_freq, phf_freq, norp_peak_time)
arg1, arg2 = (
    (norp_tim_valid, norp_fi_peak, norp_freq, norp_peak_time),
    (
        apl_tim,
        phf_tim,
        apl_fi_peak,
        phf_fi_peak,
        apl_freq,
        phf_freq,
        norp_peak_time,
    ),
)
generator(arg1, arg2)
