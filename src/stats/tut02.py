
import os
import sys
import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Tuple

# df4 = Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, '..', '..')
sys.path.append(project_root)

from config.local_config import LOCAL_DATA_DIRECTORY

date_format_mdY = '%m/%d/%Y'

def setup() -> None:
    os.chdir(LOCAL_DATA_DIRECTORY)
    directory_name = r"FactSet"
    os.chdir(directory_name)









def main() -> None:
    print("Started")
    setup()
    
    
    print("Finished")


if __name__ == "__main__":
    main()
