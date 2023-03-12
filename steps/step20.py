if "__file__" in globals():
    import os
    import sys

    file_path = os.path.dirname(__file__)
    sys.path.append(os.path.join(file_path, ".."))
from dezero.util import *

a = Variable(np.array(3.0))
b = Variable(np.array(2.0))
c = Variable(np.array(1.0))

y = add(mul(a, b), c)

y.backward()

print(y)
print(a.grad)
print(b.grad)

# 20.2 연산자 오버로드
a = Variable(np.array(3.0))
b = Variable(np.array(2.0))
y = a * b
print(y)

y = a + b
print(y)
