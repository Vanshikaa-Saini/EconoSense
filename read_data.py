from config import input_path
import pandas as pd

df = pd.read_spss(input_path)

print(df.head())