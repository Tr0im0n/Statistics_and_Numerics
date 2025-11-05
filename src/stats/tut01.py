
import os
import sys
import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Tuple

df4 = Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, '..', '..')
sys.path.append(project_root)

from config.local_config import LOCAL_DATA_DIRECTORY

date_format_mdY = '%m/%d/%Y'

def setup() -> None:
    os.chdir(LOCAL_DATA_DIRECTORY)
    directory_name = r"FactSet"
    os.chdir(directory_name)
    

def line_plots_df(df: pd.DataFrame) -> None:
    df.plot(kind="line", linewidth=2)
    plt.show()


def show_correlation_matrix(corr_matrix: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8, 6)) # Start with a reasonable size, e.g., (10, 8)
    sns.heatmap(
        corr_matrix, 
        annot=True,     # Annotate the cells with the correlation values
        cmap='coolwarm',# Choose a divergent colormap (good for positive/negative values)
        fmt=".2f",      # Format the annotations to two decimal places
        linewidths=.5,  # Add lines between cells for clarity
        cbar=True,
        ax=ax
    )
    ax.set_aspect("equal")
    ax.set_title('Correlation Matrix Heatmap (Square Cells)')
    plt.show()
    

def show_plot_and_correlation_of_df(df: pd.DataFrame) -> None:
    line_plots_df(df_price_history())
    corr_matrix = df.corr()
    show_correlation_matrix(corr_matrix)


#####################################################################
# Individual functions
#####################################################################


def df_imports_exports_nl() -> df4:
    file_name = r"ImportsExports_NL_2018_2023.xlsx"
    
    df = pd.read_excel(file_name, 
                        parse_dates=True, 
                        skiprows=4, 
                        dtype={'a': str}, 
                        nrows=33,
                        usecols=list(range(103)),
                        index_col=0,
                        date_format=date_format_mdY)

    df_inverted_columns = df.iloc[:, ::-1]
    df_t = df_inverted_columns.T
    
    df_big = df_t.iloc[:, [0, 11, 22]]
    df_imports = df_t.iloc[:, 1:11]
    df_exports = df_t.iloc[:, 12:22]
    df_balance = df_t.iloc[:, 23:33]
    
    return df_big, df_imports, df_exports, df_balance


def show_imports_exports_nl() -> None:
    dfs = df_imports_exports_nl()
    
    fig, axs = plt.subplots(2, 2, sharex=True, figsize=(12, 7))
    (ax1, ax2), (ax3, ax4) = axs
    axs_flat = [ax1, ax2, ax3, ax4]
    
    suptitle = "Import & Exports in The Netherlands 2018-2023"
    fig.suptitle(suptitle)
    ax_titles = ["Totals", "Imports", "Exports", "Balances"]
    
    for df_i, ax, title in zip(dfs, axs_flat, ax_titles):
        df_i.plot(ax=ax, kind="line", linewidth=2)
        ax.set_title(title)

    plt.show() 


def df_imports_exports_be() -> df4:
    file_name = r"ImportsExports_BE_2013_2023.xlsx"
    
    df = pd.read_excel(file_name, 
                        parse_dates=True, 
                        skiprows=[0, 1, 2, 3, 27, 50], 
                        dtype={'a': str}, 
                        nrows=67,
                        usecols=list(range(117)),
                        index_col=0,
                        date_format=date_format_mdY)

    df_inverted_columns = df.iloc[:, ::-1]
    df_t = df_inverted_columns.T
    
    df_big = df_t.iloc[:, [0, 22, 44]]
    df_imports = df_t.iloc[:-1, 1:22]
    df_exports = df_t.iloc[:-1, 23:44]
    df_balance = df_t.iloc[:-1, 45:66]

    return df_big, df_imports, df_exports, df_balance


def show_imports_exports_be() -> None:
    dfs = df_imports_exports_be()
    
    fig, axs = plt.subplots(2, 2, sharex=True, figsize=(12, 7))
    (ax1, ax2), (ax3, ax4) = axs
    axs_flat = [ax1, ax2, ax3, ax4]
    
    suptitle = "Import & Exports in Belgium 2013-2023"
    fig.suptitle(suptitle)
    ax_titles = ["Totals", "Imports", "Exports", "Balances"]
    
    for df_i, ax, title in zip(dfs, axs_flat, ax_titles):
        df_i.plot(ax=ax, kind="line", linewidth=2)
        ax.set_title(title)

    plt.show() 
    
    
def df_imports_exports_ge() -> df4:
    file_name = r"ImportsExports_GE_2013_2023.xlsx"
    
    df = pd.read_excel(file_name, 
                        parse_dates=True, 
                        skiprows=[0, 1, 2, 3, 31], 
                        dtype={'a': str}, 
                        nrows=53,
                        usecols=list(range(121)),
                        index_col=0,
                        date_format=date_format_mdY)

    df_inverted_columns = df.iloc[:, ::-1]
    df_t = df_inverted_columns.T
    
    big_cols = [0, 26]
    
    df_big = df_t.iloc[:, big_cols]
    df_imports = df_t.iloc[:-1, 1:26]
    df_exports = df_t.iloc[:-1, 27:52]
    # df_balance = df_t.iloc[:-1, 45:66]
    df_balance = df_imports - df_exports
    
    return df_big, df_imports, df_exports, df_balance
    
    
def show_imports_exports_ge() -> None:
    dfs = df_imports_exports_ge()
    
    fig, axs = plt.subplots(2, 2, sharex=True, figsize=(12, 7))
    (ax1, ax2), (ax3, ax4) = axs
    axs_flat = [ax1, ax2, ax3, ax4]
    
    suptitle = "Import & Exports in Germany 2013-2023"
    fig.suptitle(suptitle)
    ax_titles = ["Totals", "Imports", "Exports", "Balances"]
    
    for df_i, ax, title in zip(dfs, axs_flat, ax_titles):
        df_i.plot(ax=ax, kind="line", linewidth=2)
        ax.set_title(title)

    plt.show() 


def correlation_imports_exports_nl() -> None:
    dfs = df_imports_exports_nl()
    corr_matrix = dfs[1].corr()
    show_correlation_matrix(corr_matrix)

    
def df_price_history() -> pd.DataFrame:
    file_name = r"PriceHistory_SelectedMaterials.xlsx"
    
    df = pd.read_excel(file_name, 
                        parse_dates=True, 
                        skiprows=[0, 1], 
                        dtype={'a': str}, 
                        nrows=5037,
                        usecols=list(range(8)),
                        index_col=0,
                        date_format=date_format_mdY)
    
    df_inverted = df.iloc[::-1]
    df_inverted.index = df.index[::-1]
    return df_inverted


def df_retail_sales_nl() -> pd.DataFrame:
    file_name = r"RetailSales_NL_2013_2023.xlsx"
    
    df = pd.read_excel(
        file_name, 
        parse_dates=True, 
        skiprows=4, 
        dtype={'a': str}, 
        nrows=18,
        # usecols=list(range(8)),
        index_col=0,
        date_format=date_format_mdY,
        na_values=['-', "'-"]
    )
    
    df_inverted = df.iloc[:, ::-1]
    
    return df_inverted.T


def df_retail_sales_ge() -> pd.DataFrame:
    file_name = r"RetailSales_GE_2013_2023.xlsx"
    df = pd.read_excel(
        file_name, 
        parse_dates=True, 
        skiprows=4, 
        dtype={'a': str}, 
        nrows=38,
        # usecols=list(range(8)),
        index_col=0,
        date_format=date_format_mdY
    )
    
    df_inverted = df.iloc[:, ::-1]
    
    return df_inverted.T
    

def df_retail_sales_be() -> pd.DataFrame:
    file_name = r"RetailSales_BE_2013_2023.xlsx"
    df = pd.read_excel(
        file_name, 
        parse_dates=True, 
        skiprows=4, 
        dtype={'a': str}, 
        nrows=15,
        # usecols=list(range(8)),
        index_col=0,
        date_format=date_format_mdY,
        na_values=['-', "'-"]
    )
    
    df_inverted = df.iloc[:, ::-1]
    
    return df_inverted.T



def main() -> None:
    print("Started")
    setup()
    # show_imports_exports_nl()     # Import more chemicals and related products
    # show_imports_exports_be()
    # show_imports_exports_ge()
    # correlation_imports_exports_nl()
    # show_plot_and_correlation_of_df(df_price_history())
    # show_plot_and_correlation_of_df(df_retail_sales_nl())
    # show_plot_and_correlation_of_df(df_retail_sales_ge())
    show_plot_and_correlation_of_df(df_retail_sales_be())
    print("Finished")


if __name__ == "__main__":
    main()

