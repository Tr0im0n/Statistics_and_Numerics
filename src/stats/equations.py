import numpy as np
from scipy.stats import skewnorm

# --- General Notes for curve_fit ---
# 1. These functions assume you are fitting to histogram counts (Y-axis), 
#    and the bin centers are the X-axis.
# 2. All functions include an 'amplitude' parameter, A, which scales the 
#    function output to match your raw counts/density.

def hline(x: np.ndarray | float, amp: float) -> np.ndarray | float:
    return np.full_like(x, amp)

# ----------------------------------------------------
# Function for data_1: Standard Gaussian (Normal) Distribution
# ----------------------------------------------------
# Parameters:
# - x: The independent variable (e.g., histogram bin centers)
# - A: Amplitude (Scaling factor to match the height of your counts)
# - mu: Mean (Center of the distribution)
# - sigma: Standard Deviation (Width of the distribution)
def gaussian(x: np.ndarray | float, amp: float, mean: float, std: float) -> np.ndarray | float:
    """
    Standard Gaussian (Normal) Probability Density Function (PDF), scaled by an amplitude.
    data_1
    """
    if std <= 0:
        return np.zeros_like(x)
    return amp * np.exp(-0.5 * ((x - mean) / std)**2)


def double_gaussian(x: np.ndarray | float, 
        amp1: float, mean1: float, std1: float,
        amp2: float, mean2: float, std2: float,
    ) -> np.ndarray | float:
    """
    data_5
    """
    return gaussian(x, amp1, mean1, std1) + gaussian(x, amp2, mean2, std2)

# ----------------------------------------------------
# Function for data_3 and data_4: Skew-Normal Distribution
# ----------------------------------------------------
# The Skew-Normal distribution is excellent for modeling data that is 
# generally bell-shaped but exhibits asymmetry (skew).
#
# Parameters:
# - x: The independent variable (e.g., histogram bin centers)
# - A: Amplitude (Scaling factor to match the height of your counts)
# - loc: Location parameter (Shift/center of the distribution)
# - scale: Scale parameter (Spread/width of the distribution)
# - alpha: Skewness parameter (How much the distribution is skewed)
def fit_skew_normal(x: np.ndarray, amp: float, loc: float, scale: float, alpha: float) -> np.ndarray:
    """
    Skew-Normal Probability Density Function (PDF), scaled by an amplitude.
    Uses scipy.stats.skewnorm.
    data_3 and data_4
    """
    if scale <= 0:
        # Prevent non-physical results
        return np.zeros_like(x)
    
    # skewnorm.pdf returns a normalized PDF (area=1). We multiply by A to fit counts.
    return amp * skewnorm.pdf(x, alpha, loc=loc, scale=scale)

# ----------------------------------------------------
# Function for data_5: Exponential Decay with Offset
# ----------------------------------------------------
# This is useful for data that shows a sharp initial drop followed by a tail.
#
# Parameters:
# - x: The independent variable (e.g., histogram bin centers)
# - A: Amplitude (The scaling of the decay component)
# - k: Decay Rate (Higher k means faster decay)
# - C: Offset (A constant baseline value)
def exponential_decay(x: np.ndarray, A: float, k: float, C: float) -> np.ndarray:
    """
    Exponential decay function with a constant offset: f(x) = A * exp(-k*x) + C
    data_5
    """
    return A * np.exp(-k * x) + C

# --- Example Usage (Conceptual - requires actual data/counts) ---
"""
# Assuming you have already calculated counts and bin_edges:
# counts, bin_edges = np.histogram(df['data_1'], bins=bins)
# bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# from scipy.optimize import curve_fit

# # 1. Fit Gaussian to data_1
# p0_gaussian = [100, 5.0, 1.0] # Initial guess for [Amplitude, Mean, StdDev]
# params_1, covariance_1 = curve_fit(fit_data_1_gaussian, bin_centers, counts, p0=p0_gaussian)
# print(f"Data 1 Fit Parameters (A, mu, sigma): {params_1}")

# # 2. Fit Skew-Normal to data_3
# p0_skew = [100, 10.0, 2.0, 1.0] # Initial guess for [A, loc, scale, alpha]
# params_3, covariance_3 = curve_fit(fit_data_3_skew_normal, bin_centers, counts, p0=p0_skew)
# print(f"Data 3 Fit Parameters (A, loc, scale, alpha): {params_3}")
"""
