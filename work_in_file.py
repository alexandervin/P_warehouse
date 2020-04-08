# file_name = 'command.txt'
# file = open(file_name, mode='r', encoding='utf8')
# for line in file:
#     print(line, end='')
# file.close()

import io

file_name = 'command.txt'
file = open(file_name, mode='r', encoding='utf8')

file_content = file.read(100)
print(file_content)

new_position = file.seek(10, io.SEEK_SET)

file_content = file.read(100)
print((file_content))