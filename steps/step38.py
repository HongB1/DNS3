import numpy as np
from dezero import Variable
import dezero.functions as F
#
# # x = Variable(np.array([[1, 2, 3], [4, 5, 6]]))
# # y = F.reshape(x, (6, ))
# # y.backward(retain_grad=True)
# # print(x.grad)
#
# x = Variable(np.random.randn(1, 2, 3))
# y = x.reshape((2, 3))
# # print(y)
# y = x.reshape(2, 3)
# # reshape 함수는 단순히 형상만 변환함. 구체적인 계산은 아무것도 하지 않기 때문에
# # 역전파는 출력 쪽에서 전해지는 기울기에 아무런 손도 대지 않고 입력 쪽으로 흘려보내기만 함
#
# x = Variable(np.array([[1, 2, 3], [4, 5, 6]]))
# y = F.reshape(x, (6,))
# y.backward(retain_grad=True)
# # print(x.grad)
#
# x = np.random.rand(1, 2, 3)
# print('x', x)
# y = x.reshape((2, 3))
# y = x.reshape([2, 3])
# y = x.reshape(2, 3)
#
# print(y)

x = Variable(np.array([[1, 2, 3], [4, 5, 6]]))
print(x)
y = F.transpose(x)
y.backward()
print(x.grad)

x = Variable(np.random.rand(2, 3))
print(x)
print()
y = x.transpose()
print(y)
print()
y = x.T
print(y)