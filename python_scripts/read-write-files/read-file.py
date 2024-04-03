#with open('latin-file1', 'r') as rf:
#    read_size = 80
#    rf_chunk = rf.read(read_size)
#    #while len(rf_chunk) != 0:
#    #    print(rf_chunk, end='  ***\n')
#    #    rf_chunk = rf.read(read_size)
#
#    with open('latin-file2', 'w') as wf:
#        while len(rf_chunk) != 0:
#            rf_chunk+=' ###\n'
#            wf.write(rf_chunk)
#            rf_chunk = rf.read(read_size)

with open('test-file.txt', 'a') as wf:
    wf.write('Just adding some text to my file\n')
