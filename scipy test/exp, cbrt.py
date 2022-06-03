from scipy.special import cbrt
from scipy.special import exp10
from scipy.special import comb
from scipy.special import perm

cb = cbrt([27, 64])
exp = exp10([1,10])

print(cb)
print(exp)

com = comb(5, 2, exact = False, repetition=True)
print(com)

per = perm(5, 2, exact = True)
print(per)