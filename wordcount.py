#open file for use in this code using dialog
fhand = open(input('Enter file name here: '))
#prepare the file lines and create the word list
for line in fhand:
    strip_line = line.rstrip('\n')
    print(strip_line)
    if len(strip_line) < 1:
        continue
    else:
        words = strip_line.split()
#count the words in the file by iteration
counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)