# 같은 변수 반복 사용

if "__file__" in globals():
    import os
    import sys

    file_path = os.path.dirname(__file__)
    sys.path.append(os.path.join(file_path, ".."))
from dezero.core_simple import *

x = Variable(np.array(3.0))

y = add(x, x)
y.backward()
print(x.grad)


x.cleargrad()
y = add(add(x, x), x)
# print('y', y.data)

y.backward()
print("x.grad", x.grad)
