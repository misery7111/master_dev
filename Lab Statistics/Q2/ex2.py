import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import timeit


test_len = 500 + 1
num_of_test = 15
range_ = 30000
test = np.zeros((num_of_test, test_len), dtype=np.int32)
solution = np.empty((num_of_test,), dtype=np.int32)

# Generate tests
for no_ in range(num_of_test):
    rand_val = np.random.randint(low=1, high=range_, size=(test_len // 2,))
    for j in range(test_len // 2):
        while True:
            m, n = np.random.randint(test_len - 1, size=(2,))
            if m != n and test[no_, m] == 0 and test[no_, n] == 0:
                test[no_, m] = rand_val[j]
                test[no_, n] = rand_val[j]
                break
    for j in range(test_len):
        if test[no_, j] == 0:
            solution[no_] = np.random.randint(low=1, high=range_, size=(1,))
            test[no_, j] = solution[no_]
            break

# Run
def singleNumber1(nums):
    check = {}
    sum = 0
    for x in nums:
        if x in check:
            sum -= x
            del check[x]
        else:
            check[x] = True
            sum += x
    return sum


def singleNumber2(nums):
        res = 0
        for x in nums:
            res ^= x

        return res

runtime = []
num_of_run = 50

for i in range(num_of_run):
    start = timeit.default_timer()
    for t in range(num_of_test):
        singleNumber1(test[t, :])
        # if res != solution[t]:
        #     print("Failed", t, test[t, :], solution[t], res)
        #     exit()

    runtime.append(timeit.default_timer() - start)

print("## Method1")
print("Mean=", np.mean(runtime), "Var=", np.var(runtime, ddof=1), "Std=", np.std(runtime), "Mode=", stats.mode(runtime),\
      "Median=", np.median(runtime), "Min=", np.min(runtime), "Max=", np.max(runtime), "Q1=", np.percentile(runtime, 25), "Q3=", np.percentile(runtime, 75))

plt.hist(runtime, bins=int(np.sqrt(num_of_run)))
plt.savefig("hist1")
np.savetxt("method1.txt", np.array(runtime))

runtime = []
plt.figure()
for i in range(num_of_run):
    start = timeit.default_timer()
    for t in range(num_of_test):
        singleNumber2(test[t, :])

    runtime.append(timeit.default_timer() - start)


print("Mean=", np.mean(runtime), "Var=", np.var(runtime, ddof=1), "Std=", np.std(runtime), "Mode=", stats.mode(runtime),\
      "Median=", np.median(runtime), "Min=", np.min(runtime), "Max=", np.max(runtime), "Q1=", np.percentile(runtime, 25), "Q3=", np.percentile(runtime, 75))

plt.hist(runtime, bins=int(np.sqrt(num_of_run)))
plt.savefig("hist2")
np.savetxt("method2.txt", np.array(runtime))
