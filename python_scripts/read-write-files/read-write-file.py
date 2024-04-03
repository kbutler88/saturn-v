#with open('writefile.txt', 'w') as wf:
#    wf.write("Adding text to the file, but I want it to be a little longer")

with open('writefile.txt', 'r') as rf:
    # Read entire file; can be bad if file is too large for memory
    #print(rf.read())
    # Break file into batches to read data
    size_to_read = 7
    f_batch = rf.read(size_to_read)

    # Read file in batches as long as the batch contains data (not end of file)
    while len(f_batch) != 0:
        # "end=" will replace the end of the string with whatever is needed
        print(f_batch, end='*\n')
        f_batch = rf.read(size_to_read)

print('\n\nWriting more stuff to the file\n')

# Append text to file
with open('writefile.txt', 'a') as af:
    af.write("I need more text!\n")

with open('writefile.txt', 'r') as rf:
    size_to_read = 30
    f_batch = rf.read(size_to_read)
    while len(f_batch) != 0:
        # This will read the file out normally to the prompt
        print(f_batch, end='')
        # The tell() function shows to where the file has been read
        print(rf.tell(), end='')
        f_batch = rf.read(size_to_read)
