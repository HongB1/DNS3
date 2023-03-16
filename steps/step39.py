import numpy as np
from dezero import Variable
from dezero import Function
from dezero import *
import dezero.functions as F


x = Variable(np.array([1, 2, 3, 4, 5, 6]))
# x = np.array([1, 2, 3, 4, 5, 6])
y = F.sum(x)
print(y)
# pri