# Library import
import numpy as np
import matplotlib.pyplot as plt
# Data handler import
from data_norp_handler import (
    norp_loader,
    norp_filter,
    norp_quiet_sun,
)
from data_rstn_handler import (
    rstn_loader,
    rstn_quiet_sun,
)
# Data plotter import
from data_plotter import (
    norp_plotter,
    rstn_plotter,
    # combined_plotter,
)
# Data fitter import
# from data_fitter import (
    # gyro_fitter,
    # plas_fitter,
# )

# Data path repo
# Assign norp, apl, and phf file path
data_norp_path, data_apl_path, data_phf_path = (
    "./data/norp_event_131028/", 
    "./data/apl131028/", 
    "./data/phf131027/",
)

# Data repo - norp - norp_event
# Deposit norp arrays, dat and fv array unused
(
    data_norp_fi,
    data_norp_freq,
    data_norp_mvd,
    data_norp_tim,
) = norp_loader(data_norp_path)
# Deposit norp filtered arrays
data_norp_tim_valid, data_norp_fi_valid = norp_filter(
    data_norp_mvd, data_norp_tim, data_norp_fi
)
# Deposit norp quiet sun result
data_norp_fi_peak = norp_quiet_sun(data_norp_fi_valid)

# Plotter - norp - norp_event
# Assign the peaktime of flux recording
data_norp_peak_time = "2013-10-28 01:59:38"
# Plot the NORP data
data_norp_plot = norp_plotter(
    data_norp_tim_valid, data_norp_fi_peak, data_norp_peak_time, data_norp_freq
)

# Data repo - rstn - apl | phf
# Deposit rstn arrays
(
    data_apl_flux,
    data_apl_freq,
    data_apl_tim,
    data_phf_flux,
    data_phf_freq,
    data_phf_tim,
) = rstn_loader(data_apl_path, data_phf_path)
# Deposit rstn quiet sun result
data_apl_flux_peak, data_phf_flux_peak = rstn_quiet_sun(
    data_apl_flux, data_phf_flux
)

# Plot the RSTN data
#data_rstn_plot = rstn_plotter(
#    data_apl_tim, data_phf_tim, data_apl_flux_peak, data_phf_flux_peak
#)

# Combined plot
