# yara Rose
# read in file
#ask user for file name
#file_name = input("What is the name of your FASTA file? ")

#open file with .txt extension
#f = open(file_name + '.out', 'r')



f = open('dna_align.out', 'r') # file from CLUSTALW
num_lines = 0
# count the number of lines
with f:
    for num_lines, l in enumerate(f):
        pass

i = 0
f = open('dna_align.out', 'r') # file from CLUSTALW
f.readline() # need to skip over frist 3 lines
f.readline()
f.readline()
seq1 = ''
seq2 = ''
while i< (num_lines-3):
    # reads a ine, and cuts out identification seqment, only saves sequence
    line1 = (f.readline())
    split1 = line1.split('.', 1)
    #print(split1[1])
    seq1 += split1[1]

    line2 = (f.readline())
    split2 = line2.split('.', 1)
    #print(split2[1])
    seq2 += split2[1]

    f.readline()
    f.readline()
    i += 4

seq1 = seq1.replace(' ','')
seq2 = seq2.replace(' ','')

print(seq1)

