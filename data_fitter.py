"""
This is the data fitter script of the radio data analysis project.

Created on Wed Mar 15 2023

@author: Yang-Taotao
"""
# %% Library import
# Library import
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2

# %% Gyro fitter
# Gyro fitter function
def gyro_fitter(data_x, data_y):
    """
    Parameters
    ----------
    data_x : array
        Combined freq data array.
    data_y : array
        Combined flux data array.

    Returns
    -------
    params : array
        Fit parameters array.
    cov : float
        Covariance matrix of the fit.
    chi_sqr :float
        Chi-squared value of the fit.
    chi_p_val : float
        The p-value from the chi-sqaured test.
    """
    # Gyro model definition
    def gyro_model(x_val, param_a_cap, param_b_cap, param_a, param_b):
        # Return gyro model
        return (
            param_a_cap
            * x_val**param_a
            * (1 - np.exp(-param_b_cap * x_val ** (-param_b)))
        )

    # Iniitial parameter guess
    param_guess = [1, 1, 1, 1]  # param_A, param_B, param_a, param_b

    # Curve fit results
    params, cov = curve_fit(gyro_model, data_x, data_y, p0=param_guess)

    # Residuals generator
    # Get fitted model
    fit_model = gyro_model(data_x, *params)
    # Residual generator
    fit_resid = data_y - fit_model

    # Chi2 Tester
    # Chi2 calculation and dof generation
    chi_sqr, chi_dof = (
        np.sum(fit_resid**2 / fit_model),
        len(data_x) - len(params),
    )
    # Chi2 p-value calculation
    chi_p_val = 1 - chi2.cdf(chi_sqr, chi_dof)

    # Results print out
    # Gyro fitter result title
    print(f"{'Gyro fitter results':<20}")
    print()
    # Print fit parameters
    print(f"{'Gyro fitter fitted parameters':<20}")
    print(f"{'A:':<20}{params[0]:>10.3f}")
    print(f"{'B:':<20}{params[1]:>10.3f}")
    print(f"{'a:':<20}{params[2]:>10.3f}")
    print(f"{'b:':<20}{params[3]:>10.3f}")
    print()
    # Print chi2 results
    print(f"{'Chi-square test result':<20}")
    print(f"{'Chi-square:':<20}{chi_sqr:>10.3f}")
    print(f"{'p-value:':<20}{chi_p_val:>10.3f}")

    # Function return
    return (params, cov, chi_sqr, chi_p_val)
