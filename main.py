from dotpy.parser.parser import MyParser

par = MyParser()
with open('dotpy/files_test/intautoma.dot', 'r') as f:
    dot = f.read()
    f.close()

# print(dot)
result = par(dot)
print(type(result))