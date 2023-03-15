# Library import
import numpy as np
import matplotlib.pyplot as plt
from data_norp_handler import (
    norp_loader,
    norp_filter,
    norp_quiet_sun,
    norp_plotter,
)

# Data repo - norp - norp_event
# Assign norp file path
data_norp_path = "./data/norp_event_131028/"
# Deposit norp arrays
(
    data_norp_day,
    data_norp_fi,
    data_norp_freq,
    data_norp_fv,
    data_norp_mvd,
    data_norp_tim,
) = norp_loader(data_norp_path)
# Deposit filtered arrays
data_norp_tim_valid, data_norp_fi_valid = norp_filter(
    data_norp_mvd, data_norp_tim, data_norp_fi
)
# Deposit quiet sun result
data_norp_fi_peak = norp_quiet_sun(data_norp_fi_valid)
# Assign the peaktime of flux recording
data_norp_peak_time = "01:59:38"
# Plot the NORP data
data_norp_plot = norp_plotter(
    data_norp_tim_valid, data_norp_fi_peak, data_norp_peak_time
)

# Data repo - rstn - apl | phf
# Assign apl and phf file path
data_apl_path, data_phf_path = "./data/apl131028", "./data/phf131027"
