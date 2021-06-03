import numpy as np
from scipy import stats
from matplotlib import pyplot as plt


sample_size = 50000
num_of_test = 100
est = np.empty((num_of_test,))

for i in range(num_of_test):
    sample = np.sqrt(np.square(np.random.uniform(size=sample_size)) + np.square(np.random.uniform(size=sample_size)))
    sample = sample <= 1
    est[i] = np.count_nonzero(sample) * 4

est /= sample_size
np.savetxt("report.txt", np.array(est))
print("Mean=", np.mean(est), "Var=", np.var(est, ddof=1), "Std=", np.std(est), "Mode=", stats.mode(est),\
      "Median=", np.median(est), "Min=", np.min(est), "Max=", np.max(est), "Q1=", np.percentile(est, 25), "Q3=", np.percentile(est, 75))

plt.hist(est, bins=int(np.sqrt(num_of_test)))
plt.savefig("hist")
