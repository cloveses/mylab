# import numpy as np
import pandas as pd

df = pd.DataFrame({'id':['a', 'b', 'c', 'c'], "ch":[24, 76, 35, 35], 'en':[65, None, 87, 87]})
d = df.drop_duplicates().dropna()


def myrun(numbers):
    max_count = 0
    timenext = 1
    ch = ''
    for i in numbers:
        if ch == i:
            timenext += 1
        else:
            if timenext > max_count:
                max_count = timenext
            timenext = 1
        ch = i
    print(max_count)

myrun([6, 6, 7, 1.0, 1.0, 1.0, 1, 4.5, 1])