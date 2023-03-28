# %% Docstrings init
"""
This is the master script of the radio data analysis project.

Created on Wed Mar 15 2023

@author: Yang-Taotao
"""
# %% Library import
# Library import
# Data handler import
from data_norp_handler import norp_loader, norp_quiet_sun, norp_filter
from data_rstn_handler import rstn_loader, rstn_quiet_sun

# Data plotter import
from data_plotter import norp_log_plotter

# Data fitter import
# from data_fitter import (
# gyro_fitter,
# plas_fitter,
# )

# %% Data repo
# Data path repo
# Assign norp, apl, and phf file path
norp_path, apl_path, phf_path = ("./data/norp/", "./data/apl/", "./data/phf/")
# Assign the peaktime of flux recording
norp_peak_time = "2013-10-28 01:59:38"

# Data repo - norp - norp_event
# Deposit norp data arrays
norp_fi, norp_freq, norp_mvd, norp_tim = norp_loader(norp_path)
# Deposit norp validity filtered arrays
norp_tim_valid, norp_fi_valid = norp_filter(norp_mvd, norp_tim, norp_fi)
# Deposit norp quiet sun result
norp_fi_peak = norp_quiet_sun(norp_fi_valid)

# Data repo - rstn - apl | phf
# Deposit rstn arrays
apl_flux, apl_freq, apl_tim, phf_flux, phf_freq, phf_tim = rstn_loader(
    apl_path, phf_path
)
# Deposit rstn quiet sun result
apl_flux_peak, phf_flux_peak = rstn_quiet_sun(apl_flux, phf_flux)

# %% Plotter
# Plot log-log plot of NORP data
norp_log_plotter(norp_tim_valid, norp_fi_peak, norp_peak_time, norp_freq)

# %% Unused plotter resource - legacy plots
# Unused code repository - original plot ideas
# Plot the NORP data
# norp_plotter(norp_tim_valid, norp_fi_peak, norp_peak_time, norp_freq)

# Plot the RSTN data
# rstn_plotter(apl_tim, phf_tim, apl_flux_peak, phf_flux_peak, apl_freq)

# Combined plot
# combined_plotter(
#    norp_tim_valid,
#    norp_fi_peak,
#    norp_peak_time,
#    apl_tim,
#    phf_tim,
#    apl_flux_peak,
#    phf_flux_peak,
# )
