import sys
from pprint import pprint

print(sys.executable)
print(sys.platform)
print(sys.version)
print(sys.argv)
pprint(sys.modules)

print(type(sys.modules), sys.modules)

for k, v in sys.modules.items():
    print(k, type(v), v, dir(v))
x = {'a': 1, 'b': 2}
y = {'b': 10, 'c': 11}
z = {**x, **y}
print(z)

z = x.copy()
z.update(y)
print(x)
print(z)

from PIL import Image
