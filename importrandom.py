import random
import math

a, b = 0.0, 1.0
N = 107000          # ~ gives Error2 close to 0.0015
random.seed(789)      # fix seed so output is reproducible

# Monte Carlo
s = 0.0
for _ in range(N):
    x = random.uniform(a, b)
    s += math.exp(x)

mc_value = (b - a) * s / N

# Exact
exact_value = math.e - 1

# Error 1
error1 = abs(exact_value - mc_value)

# Error 2 (theoretical)
variance = (math.exp(2) - 1) / 2 - (math.e - 1) ** 2
sigma = math.sqrt(variance)
error2 = sigma / math.sqrt(N)

print("MC value        =", mc_value)
print("Exact value     =", exact_value)
print("Error 1         =", error1)
print("Error 2 (sigma/√N) =", error2)
