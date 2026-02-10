import random, math

a, b = 0.0, 1.0
N = 100000

vals = []
for _ in range(N):
    x = random.uniform(a, b)
    vals.append(math.exp(x))

mc = (b-a) * sum(vals) / N

mean_f = sum(vals)/N
var_hat = sum((v-mean_f)**2 for v in vals) / (N-1)   # sample variance
sigma_hat = math.sqrt(var_hat)

error2_sample = (b-a) * sigma_hat / math.sqrt(N)     # estimated SE

print("MC =", mc)
print("Estimated Error2 =", error2_sample)
# Monte Carlo works using random numbers.
# The error estimate is based on the sample variance of the function values.