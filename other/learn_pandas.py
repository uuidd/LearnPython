# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
# 0    1.0
# 1    3.0
# 2    5.0
# 3    NaN
# 4    6.0
# 5    8.0
# dtype: float64
dates = pd.date_range("20210102", periods=6)
print(dates)
# DatetimeIndex(['2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05',
#                '2021-01-06', '2021-01-07'],
#               dtype='datetime64[ns]', freq='D')
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)
#                   A         B         C         D
# 2021-01-02  0.251710  0.139930  0.855325  0.115721
# 2021-01-03  0.237030  2.948289 -0.031929 -1.831420
# 2021-01-04 -0.313794  1.065819  1.122440 -0.754281
# 2021-01-05 -0.433097  0.291290  0.931700 -0.604654
# 2021-01-06  1.200101 -0.574507  0.066261  0.741316
# 2021-01-07 -0.149051 -0.905167  0.775307  0.630945
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20210102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo"

    }
)
print(df2)
#    A          B    C    D      E    F
# 0  1.0 2021-01-02  1.0  3   test  foo
# 1  1.0 2021-01-02  1.0  3  train  foo
# 2  1.0 2021-01-02  1.0  3   test  foo
# 3  1.0 2021-01-02  1.0  3  train  foo
print(df2.dtypes)
# A           float64
# B    datetime64[ns]
# C           float32
# D             int32
# E          category
# F            object
# dtype: object
print(df2.to_numpy())
print(df2.to_dict())