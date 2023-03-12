# 같은 변수 반복 사용

if "__file__" in globals():
    import os
    import sys

    file_path = os.path.dirname(__file__)
    sys.path.append(os.path.join(file_path, ".."))
from dezero.util import *

#
# generations = [2, 0, 1, 4, 2]
# funcs = []
#
# for g in generations:
#     f = Function()
#     f.generation = g
#     funcs.append(f)
# funcs.sort(key=lambda x: x.generation)
# k = [f.generation for f in funcs]
# k

x = Variable(np.array(2.0))
a = square(x)
y = add(square(a), square(a))
y.backward()

print(y.data)
print(x.grad)
