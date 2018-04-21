with open('1219935-checksum-file-manifest.txt') as fh:
    #create dictionary
    counts = dict()
    lineCount = 0
    for line in fh:
        lineCount = lineCount + 1
        #split the line at the space, creating a list of the hash & file path 
        values = line.split()
        characters = len(values[1])
#        i = characters - 1
        #slice the last three characters off the file path
        fileExtension = values[1][characters-3::]

        #print a list of the line count and the file extension
        print(str(lineCount)+'. '+fileExtension)
        
        #record the extensions in a dictionary, and increment each time fileExtension repeats
        if fileExtension not in counts:
            counts[fileExtension] = 1
        else:
            counts[fileExtension] = counts[fileExtension] + 1

#print the dictionary
print(counts)
