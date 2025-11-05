
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns
from typing import Tuple

from equations import double_gaussian, fit_skew_normal, gaussian, hline

# df4 = Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, '..', '..')
sys.path.append(project_root)

from config.local_config import LOCAL_DATA_DIRECTORY

os.chdir(LOCAL_DATA_DIRECTORY)
file_name = "unknown_distributions.tsv"

df_unknown_distributions = pd.read_csv(file_name, sep='\t', header=0, index_col=0, dtype=np.float32)

date_format_mdY = '%m/%d/%Y'

def plot_all():
    df_unknown_distributions.plot()
    plt.show()


def plot_histogram(df: pd.DataFrame, col_name: str) -> None:
    plt.hist(df[col_name], bins=10, edgecolor='black', alpha=0.7)
    plt.show()


def histogram_all_sequence(df: pd.DataFrame) -> None:
    for col_name in df.columns:
        plot_histogram(df, col_name)


def histogram_all(df: pd.DataFrame, bins) -> None:
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(10, 6))
    fig.suptitle(f"Histograms with {bins} bins")
    axes_flat = [item for sublist in axes for item in sublist]
    col_names = df.columns
    fit_functions = [hline, gaussian, fit_skew_normal, fit_skew_normal, fit_skew_normal, double_gaussian]
    p0s = [
        [156.25], 
        [450, 0,  1],
        [1000, 0,  1, 0], 
        [1000, 0,  1, 0], 
        [1000, 0,  1, 0], 
        [300, -1, 1, 300, 1, 1]
    ]
    for ax, col_name, fit_function, p0 in zip(axes_flat, col_names, fit_functions, p0s):
        fit_one(ax, col_name, fit_function, p0)

    plt.show()
    

def fit_one(ax, col_name: str, fit_function, p0=None, bins: int = 64):
    df = df_unknown_distributions
    # array = df[col_name].to_numpy()
    # counts, bin_edges = np.histogram(array, bins=bins)
    counts, bin_edges = np.histogram(df[col_name], bins=bins)
    bin_width = bin_edges[1] - bin_edges[0]
    half_width = bin_width * 0.5
    bin_centers = np.array([i + half_width for i in bin_edges[:-1]])
    
    # p = np.polyfit(bin_centers, counts, 0)
    # values = np.polyval(p, bin_centers)
    popt, pcov = scipy.optimize.curve_fit(fit_function, bin_centers, counts, p0)
    print(col_name, popt)
    values = fit_function(bin_centers, *popt)
    
    ax.bar(
            x=bin_centers,
            height=counts,
            width=bin_width,
            align='center',
            edgecolor='black',
            alpha=0.9
    )
    ax.plot(bin_centers, values, color='r')
    ax.set_title(col_name)
    

def fit_all(df: pd.DataFrame, bins) -> None:
    col_names = df.columns

    
    
def main() -> None:
    print("Started")
    # plot_all()
    # plot_histogram(df_unknown_distributions, "data_0")
    # histogram_all_sequence(df_unknown_distributions)
    histogram_all(df_unknown_distributions, 64)
    
    print("Finished")


if __name__ == "__main__":
    main()



"""


def histogram_all(df: pd.DataFrame, bins) -> None:
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(10, 6))
    fig.suptitle(f"Histograms with {bins} bins")
    axes_flat = [item for sublist in axes for item in sublist]
    col_names = df.columns
    fit_functions = [hline, gaussian, fit_skew_normal, fit_skew_normal, fit_skew_normal, double_gaussian]
    p0s = [
        [156.25], 
        [450, 0,  1],
        [1000, 0,  1, 0], 
        [1000, 0,  1, 0], 
        [1000, 0,  1, 0], 
        [300, -1, 1, 300, 1, 1]
    ]
    for ax, col_name, fit_function, p0 in zip(axes_flat, col_names, fit_functions, p0s):
        if col_name == "data_0":
            p0 = [156.25]
            fit_one(ax, col_name, hline, p0)
            continue
        elif col_name == "data_1":
            p0 = [450, 0,  1]
            fit_one(ax, col_name, gaussian, p0)
            continue
        elif col_name == "data_2":
            p0 = [1000, 0,  1, 0]
            fit_one(ax, col_name, fit_skew_normal, p0)
            continue
        elif col_name == "data_3":
            p0 = [1000, 0,  1, 0]
            fit_one(ax, col_name, fit_skew_normal, p0)
            continue
        elif col_name == "data_4":
            p0 = [1000, -1,  1, 6]
            fit_one(ax, col_name, fit_skew_normal, p0)
            continue
        elif col_name == "data_5":
            p0 = [300, -1, 1, 300, 1, 1]
            fit_one(ax, col_name, double_gaussian, p0)
            continue
        counts, bin_edges = np.histogram(df[col_name], bins=bins)
        ax.bar(
            x=bin_edges[:-1],          # x-coordinates of the left sides of the bars
            height=counts,         # heights of the bars
            width=bin_edges[1] - bin_edges[0],       # width of the bars
            align='edge',          # align bars to the left edge of the x-coordinate
            edgecolor='black',
            alpha=0.9
        )
        ax.set_title(col_name)
        mean = df[col_name].mean()
        std = df[col_name].std()
        xs = [mean-std, mean, mean+std]
        ax.vlines(xs, ymin=0, ymax=counts.max(), colors=['b', 'k', 'b'])
    plt.show()



"""

