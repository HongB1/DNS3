if "__file__" in globals():
    import os
    import sys

    file_path = os.path.dirname(__file__)
    sys.path.append(os.path.join(file_path, ".."))
from dezero.core_simple import *

x = Variable(np.random.randn(10000))
y = square(square(square(x)))
