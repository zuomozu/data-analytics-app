import pandas as pd

import os

def run_analysis():
    # Get the absolute path to the current directory
    base_dir = os.path.abspath(os.path.dirname(__file__))
    # Construct the path to the CSV file
    data_path = os.path.join(base_dir, '..', 'data', 'sample.csv')
    
    data = pd.read_csv(data_path)
    mean_value = data['value'].mean()
    return {'mean': mean_value}
