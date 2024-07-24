#!/usr/bin/python3
from typing import Dict, Any

# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его
# в one hot вид. Сможете ли вы это сделать без get_dummies?
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

for col in data:
    columns = data['whoAmI'].unique()

lastDate = pd.DataFrame()
for col in columns:
    lastDate[col] = data['whoAmI'].apply(lambda x: 1 if x == col else 0)
print(lastDate)
