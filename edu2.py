var = input('type smth: ')
fw = open('doc/file.txt', 'a')
fw.write('Hello world\n')
fw.write(var)
fw.close()

#a - writing new data to file, and add new data to the end of file
#w - replace existing data with new ones

fw = open('doc/file.txt', 'w')
fw.write(var)
fw.close()

fr = open('doc/file.txt', 'r')
text = fr.read()
fr.close()
print(text)

#r read data

#modules
def some():
    print('Hello world')

