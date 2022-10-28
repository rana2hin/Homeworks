# loading required libreries and data
from sklearn.datasets import load_diabetes
import pandas as pd
from statistics import mean
import numpy as np

# ___________No. 1____________________

# defining function


def LocalAvg(Y, X, tgrid, bw):
    lower = tgrid - bw
    upper = tgrid + bw

    # empty array for holding means
    mean_holder = np.array([])

    # calculating the means
    for i in range(len(tgrid)):
        x2 = np.logical_and(X > lower[i], X < upper[i])
        y2 = Y[x2]

        found_y = np.size(y2)

        if found_y:
            mean_holder = np.append(mean_holder, np.mean(y2))
        else:
            mean_holder = np.append(mean_holder, 0)
    return (mean_holder)


# testing with examples
Y = np.array([3, 7, 12, 1, 8, 17])
X = np.array([0, 1, 2, 3, 4, 5])
tgrid = np.array([1.5, 3.5, 10.5])
bw = 1.0
print(LocalAvg(Y=Y, X=X, tgrid=tgrid, bw=bw))

Y = np.array([3, 7, 12, 1, 8, 17, 23, 26])
X = np.arange(8)
tgrid = np.array([1.5, 3.5, 6.0, 11.0])
print(LocalAvg(Y=Y, X=X, tgrid=tgrid, bw=0.1))
print(LocalAvg(Y=Y, X=X, tgrid=tgrid, bw=0.6))
print(LocalAvg(Y=Y, X=X, tgrid=tgrid, bw=1.0))
print(LocalAvg(Y=Y, X=X, tgrid=tgrid, bw=12.0))
print(LocalAvg(Y=Y, X=X, tgrid=np.array([2.0]), bw=1.0))

# _____________No. 2___________________________

# loading diabetes data
diabet = load_diabetes()
num_diabet = diabet.data
outcome = diabet.target
var_names = diabet.feature_names

# (a)
print("Mean Outcome: ", np.mean(outcome))
print("Median Outcome: ", np.median(outcome))
print(
    "100 < outcome < 200: ",
    np.count_nonzero(
        np.logical_and(
            outcome > 100,
            outcome < 200)))

# (b)
data1 = pd.DataFrame(
    data=np.c_[
        diabet['data']],
    columns=diabet['feature_names'])

perc_age = np.percentile(data1.age, [25, 50, 75])

# (c)
age_category = np.array([])
for i in range(len(data1.age)):
    if data1.age[i] < perc_age[0]:
        age_category = np.append(age_category, 0)
    elif data1.age[i] >= perc_age[0] and data1.age[i] < perc_age[1]:
        age_category = np.append(age_category, 1)
    elif data1.age[i] >= perc_age[1] and data1.age[i] < perc_age[2]:
        age_category = np.append(age_category, 2)
    else:
        age_category = np.append(age_category, 3)

# (d)
category_median = np.array([np.median(outcome[age_category == 0]),
                            np.median(outcome[age_category == 1]),
                            np.median(outcome[age_category == 2]),
                            np.median(outcome[age_category == 3])])

# (e)
dict(data1.max(axis=0))

# When I wrote this code, only God and I understood what I did. Now only God knows.
# ______________ THANK YOU ____________________
