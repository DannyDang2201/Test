import numpy as np
import pandas as pd
from tqdm import tqdm

csv_2019 = pd.read_csv(r"C:\Users\USER\Downloads\archive\ver2020.csv")
csv_2020 = pd.read_csv(r"C:\Users\USER\Downloads\archive\ver2019.csv")

sum = 0
count = 0
for i in tqdm(range(len(csv_2020))):
    if not np.isnan(csv_2020["Geography"][i]):
        sum += float(csv_2020["Geography"][i])
        count += 1
print("\nGeography score avg: {}".format(sum/count))                                                                          
