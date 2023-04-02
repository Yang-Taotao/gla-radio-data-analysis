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

# %% Fit model definition
# Gyro model definition
def gyro_model(x_val, param_a_cap, param_b_cap, param_a, param_b):
    """
    Parameters
    ----------
    x_val : array
        Gyro model x value array.
    param_a_cap : float
        Fit param A.
    param_b_cap : float
        Fit param B.
    param_a : float
        Fit param a.
    param_b : float
        Fit param b.

    Returns
    -------
    array
        Gyro model.
    """
    # Return gyro model
    return (
        param_a_cap
        * (x_val**param_a)
        * (1 - np.exp(-param_b_cap * (x_val ** (-param_b))))
    )


# Plas model definition
def plas_model(x_val, param_c, param_k):
    """
    Parameters
    ----------
    x_val : array
        Plasma model x value array.
    param_c : float
        Fit param c.
    param_k : float
        Fit param k.

    Returns
    -------
    array
        Plasma model.

    """
    # Return plas model
    return param_c * (x_val**param_k)


# %% Fitted function result label generator
def fit_label(gyro_param, plas_param):
    """
    Parameters
    ----------
    gyro_param : tuple
        Gyro model fit param tuple.
    plas_param : tuple
        Plas model fit param tuple.

    Returns
    -------
    label_gyro : string
        Fitted gyro model expression.
    label_plas : string
        Fitted plas model expression.
    """
    # Cache into singular tuple
    fit_param = np.concatenate([gyro_param, plas_param]).ravel()

    # Local fit cariable unpack
    fit_a_cap, fit_b_cap, fit_a, fit_b, fit_c, fit_k = [
        fit_param[i] for i in range(len(fit_param))
    ]

    # Label generator
    label_gyro, label_plas = (
        # Gyro model
        rf"Gyro model: $y={fit_a_cap:.3g}x^{{{fit_a:.3g}}}"
        rf"[1-\exp({{-({fit_b_cap:.3g})x^{{-{fit_b:.3g}}}}})]$",
        # Plas model
        rf"Plas model: $y={fit_c:.3g}x^{{{fit_k:.3g}}}$",
    )

    # Result return
    return (label_gyro, label_plas)


# %% Gyro fitter
# Gyro fitter function
def gyro_fitter(data_freq, data_flux, cut):
    """
    Parameters
    ----------
    data_freq : array
        Combined freq data array.
    data_flux : array
        Combined flux data array.
    cut : float
        Cut-off point for different fits.

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
    # Generate filtered data
    data_x, data_y = (
        data_freq[data_freq >= cut],
        data_flux[data_freq >= cut],
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
    print()
    print("=" * 30)
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
    print("=" * 30)
    print()

    # Function return
    return (params, cov, chi_sqr, chi_p_val)


# %% Plas fitter
# Plas fitter function
def plas_fitter(data_x, data_y, cut):
    """
    Parameters
    ----------
    data_x : array
        Combined freq data array.
    data_y : array
        Combined flux data array.
    cut : float
        Cut-off point for different fits.

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
    # Generate filtered data
    data_x, data_y = (
        data_x[data_x < cut],
        data_y[data_x < cut],
    )

    # Iniitial parameter guess
    param_guess = [1, 1]  # param_c, param_k

    # Curve fit results
    params, cov = curve_fit(plas_model, data_x, data_y, p0=param_guess)

    # Residuals generator
    # Get fitted model
    fit_model = plas_model(data_x, *params)
    # Residual generator
    fit_resid = data_y - fit_model

    # Chi2 Tester
    # Chi2 calculation and dof generation
    chi_sqr, chi_dof = (
        np.sum((fit_resid)**2 / fit_model),
        len(data_x) - len(params),
    )
    # Chi2 p-value calculation
    chi_p_val = 1 - chi2.cdf(chi_sqr, chi_dof)

    # Results print out
    # Gyro fitter result title
    print()
    print("=" * 30)
    print(f"{'Plas fitter results':<20}")
    print()
    # Print fit parameters
    print(f"{'Plas fitter fitted parameters':<20}")
    print(f"{'c:':<20}{params[0]:>10.3f}")
    print(f"{'k:':<20}{params[1]:>10.3f}")
    print()
    # Print chi2 results
    print(f"{'Chi-square test result':<20}")
    print(f"{'Chi-square:':<20}{chi_sqr:>10.3f}")
    print(f"{'p-value:':<20}{chi_p_val:>10.3f}")
    print("=" * 30)
    print()

    # Function return
    return (params, cov, chi_sqr, chi_p_val)

# %% Gyro fitter
# Gyro fitter function
def denoise_fitter(data_x, data_y):
    """
    Parameters
    ----------
    data_freq : array
        Combined freq data array.
    data_flux : array
        Combined flux data array.
    cut : float
        Cut-off point for different fits.
    title : string
        Additional print out customization. 

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
    print()
    print("=" * 30)
    print(f"{'Denoised gyro fitter results':<20}")
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
    print("=" * 30)
    print()

    # Function return
    return (params, cov, chi_sqr, chi_p_val)


# %% Gyro model denoiser (cut plas model)
def gyro_pass(data_freq, data_flux, cut, plas_param):
    """
    Parameters
    ----------
    data_freq : array
        Peak time freq array.
    data_flux : array
        Peak time flux array.
    cut : float
        Low freq cut-off value.
    plas_param : tuple
        Tuple of plas model fit param.

    Returns
    -------
    data_y_gyro : array
        Denoised flux array for gyro fitting.
    """
    # Cut-off array local repo
    data_x, data_y, data_y_base = (
        data_freq[data_freq < cut],
        data_flux[data_freq < cut],
        data_flux[data_freq >= cut],
    )

    # Get denoised flux array in plas model domain
    data_y_pass = data_y - plas_model(data_x, *plas_param)

    # Get denoised flux data array for gyro fitting
    data_y_gyro = np.concatenate([data_y_pass, data_y_base])

    # Return denoised result
    return data_y_gyro
