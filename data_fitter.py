"""
This is the data fitter script of the radio data analysis project.

Created on Wed Mar 15 2023

@author: Yang-Taotao
"""
# Library import
import numpy as np
from scipy.optimize import curve_fit

# Radio data curve fit model functions repo
def model_func(arg):
    # Local variable repo
    data_freq, A, B, a, b, c, k = [arg[i] for i in range(len(arg))]
    # Function assignment
    flux_gyro, flux_plas = (
        A * data_freq**a * (1 - np.exp(-B * data_freq**(-b))),
        c * data_freq**k,
    )
    # Function repo
    flux_model = (flux_gyro, flux_plas)
    # Function return
    return flux_model


# General curve fitter
def curve_fitter(model_string, data_x, data_y, arg):
    # Model selector
    if model_string = "gyro":
        model, p0 = (
            model_func(arg)[0],  # Get gyro model
            [1, 1, 1, 1],  # A, B, a, b initial guess
        )
    elif model_string = "plas":
        model, p0 = (
            model_func(arg)[1],  # Get plas model
            [1, 1],  # c, k initial guess
        )
    # Fitter
