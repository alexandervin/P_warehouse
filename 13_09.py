f = open('file.txt', 'r', encoding='utf-8')
text = f.read(30)
f.close()
print(text)