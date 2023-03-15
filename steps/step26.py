import numpy as np
from dezero import Variable
# from dezero.utils import get_dot_graph
from dezero.util import _dot_var, _dot_func, plot_dot_graph

# x0 = Variable(np.array(1.0))
# x1 = Variable(np.array(1.0))
# y = x0 + x1
#
# x0.name = 'x0'
# x1.name = 'x1'
# y.name = 'y'
#
# txt = get_dot_graph(y, verbose=False)
# print(txt)
#
# # dot 파일로 저장
# with open('sample.dot', 'w') as o:
#     o.write(txt)
x = Variable(np.random.randn(2, 3))
x.name = 'x'
print(_dot_var(x))
print(_dot_var(x, verbose=True))

x0 = Variable(np.array(1.0))
x1 = Variable(np.array(1.0))
y = x0 + x1
txt = _dot_func(y.creator)
print(txt)

def goldstein(x, y):
    z = (1 + )