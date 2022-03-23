#open file for use in this code using dialog
fhand = open(input('Enter file name here: '))
#always make the dictionary in front of the working block of code
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    #the get() function searches the existing dictionary for the word. If the word is present, then one iteration is added to the existing value.
    #if the word is not present, get() makes the default value 0 and adds one
    for w in words:
        counts[w] = counts.get(w,0) + 1
        #make sure you use [] when working with dictionaries!!
print(counts)