file_name = 'command.txt'
file = open(file_name, mode='r', encoding='utf8')
for line in file:
    print(line, end='')
file.close()