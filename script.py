# creating files

#with open('makethisfile.txt', 'w') as f:
#    f.write('this sentence is awesome')

with open('makethisfile.txt', 'w+') as f:
    f.write('updated the sentence')
