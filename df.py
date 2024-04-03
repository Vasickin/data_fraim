import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

one_hot_encoded = pd.concat([pd.Series(1, index=data.index, name='whoAmI_'+i) if i == data['whoAmI'].iloc[j] else pd.Series(0, index=data.index, name='whoAmI_'+i) for j, i in enumerate(set(data['whoAmI']))], axis=1)