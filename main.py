"""
This is the master script of the radio data analysis project.

Created on Wed Mar 15 2023

@author: Yang-Taotao
"""
# %% Custom module import
# Data handler import
from data_handler import loader, validator, quiet_sun, collector

# Data plotter import
from data_plotter import plot_generator, log_avg_plotter

# Data fitter import
from data_fitter import gyro_fitter, plas_fitter

# %% Key data assignment
# Assign norp, apl, and phf file path
data_path = ("./data/norp/", "./data/apl/", "./data/phf/")
# Assign the peaktime of flux recording
norp_peak_time = "2013-10-28 01:59:38"

# %% Data repo
# Deposit data arrays
data_repo = loader(data_path)
# Assign loaded data
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
) = [data_repo[i] for i in range(len(data_repo))]
# Deposit norp validity filtered arrays
norp_tim_valid, norp_fi_valid = validator(norp_mvd, norp_tim, norp_fi)
# Deposit quiet sun result
norp_fi_peak, apl_fi_peak, phf_fi_peak = quiet_sun(
    (norp_fi_valid, apl_fi, phf_fi)
)

# %% Peak time array argument assignment
# Time, Freq, Flux sub function arguemnt repo
arg_time, arg_freq, arg_flux = (
    # arg_time
    (
        norp_tim_valid,
        apl_tim,
        phf_tim,
        norp_peak_time,
    ),
    # arg_freq
    (
        norp_freq,
        apl_freq,
        phf_freq,
    ),
    # arg_flux
    (
        norp_fi_peak,
        apl_fi_peak,
        phf_fi_peak,
    ),
)
# Peak time arguement tally
peak_arg = (arg_time, arg_freq, arg_flux)

# %% Peak time flux array repo
# Assign peak time combined freq and flux array
peak_time_freq, peak_time_flux = collector(*peak_arg)

# %% Curve fitter
# Generate combined fit results
results_gyro, results_plas = (
    gyro_fitter(peak_time_freq, peak_time_flux),
    plas_fitter(peak_time_freq, peak_time_flux),
)

# %% Fit parameter cache
# General combined fit parameter cache
gyro_param, plas_param = results_gyro[0], results_plas[0]

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
    # Peak time combined plotter arguments
    (
        peak_time_freq,
        peak_time_flux,
        norp_peak_time,
        gyro_param, 
        plas_param,
    ),
)

# %% Averaged flux array parser
norp_peak_avg, apl_peak_avg, phf_peak_avg = log_avg_plotter(plt_arg3)

# %% Plot generator argument assignment
# Plot generator argument assignment
plt_arg = (plt_arg1, plt_arg2, plt_arg3, plt_arg4)

# %% Plot generation
plot_generator(plt_arg)
