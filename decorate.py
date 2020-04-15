import sys
from pprint import pprint

print(sys.executable)
print(sys.platform)
print(sys.version)
print(sys.argv)
pprint(sys.modules)

# print(type(sys.modules), sys.modules)

for k, v in sys.modules.items():
    print(k, type(v), v, dir(v))