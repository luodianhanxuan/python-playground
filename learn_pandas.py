import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4))
print(df)
pieces = [df[:3], df[3:7], df[7:]]
print(pd.concat(pieces))


left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
print(left)
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print(right)

print(pd.merge(left, right, on='key'))

left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
print(left)
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
print(right)
print(pd.merge(left, right, on='key'))

df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print(df)

s = df.iloc[3]
print(s)
df.append(s, ignore_index=True)
print(df)