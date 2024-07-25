import pandas as pd

def run_analysis():
    data = pd.read_csv('data/sample.csv')
    mean_value = data['value'].mean()
    return {'mean': mean_value}
