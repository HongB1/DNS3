if "__file__" in globals():
    import os
    import sys

    file_path = os.path.dirname(__file__)
    sys.path.append(os.path.join(file_path, ".."))
from dezero.util import *

Config.enable_backprop = True
x = Variable(np.ones((100, 100, 100)))
y = square(square(square(x)))
y.backward()

Config.enable_backprop = False
x = Variable(np.ones((100, 100, 100)))
y = square(square(square(x)))
y.backward()

with using_config("enable_backprob", False):
    x = Variable(np.array(2.0))
    y = square(x)

import contextlib


@contextlib.contextmanager
def config_test():
    print("start")
    try:
        yield
    finally:
        print("done")


with config_test():
    print("process..")
