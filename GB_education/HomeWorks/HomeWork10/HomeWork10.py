# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd
import numpy as np

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

categories = pd.DataFrame({'whoAmI': data['whoAmI'].unique()})

one_hot = pd.DataFrame(np.zeros((len(categories), len(categories))))

for i, categ in enumerate(categories['whoAmI']):
    one_hot.iloc[i][categ] = 1

for i, categ in enumerate(categories['whoAmI']):
    data[categ] = np.where(data['whoAmI'] == categ, 1, 0)

print(data.head(20))
