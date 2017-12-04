# python modual that allows us interact with command line
import os

# user needs to download homologene file
print("Welcome to ACE. A tool that utilizes the clustalw program and compares two dna sequences and two amino acid sequences. Fasta files are needed from homologenome.")
#  ask user for file name???
print("Please input amino acid text file: ")
aa = raw_input()
print("Please input dna text file")
dna = raw_input()
# tell user that they can only input 2 sequences at a time

# types string  bellow into command line, tells clustul to take in first file, allign and output 2nd file
# Run clustalw on the generated files from homologene that contains multiple homologous sequences
os.system("clustalw dna -outfile=dna_align.txt") # DNA alignment
os.system("clustalw aa -type=protein -outfile=aa_align.txt") # Protein alignment

# Parse files (dna and aa) to obtain both sequences and store them in variables
# Checks similiarities between two hard-coded sequences and output their percent similiarity and difference

# yara Rose
# read in file
#ask user for file name
#file_name = input("What is the name of your FASTA file? ")

#open file with .txt extension
#f = open(file_name + '.out', 'r')
f = open('dna_align.txt', 'r')
num_lines = 0
# count the number of lines
with f:
    for num_lines, l in enumerate(f):
        pass

i = 0
f = open('dna_align.txt', 'r') # file from CLUSTALW
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

#print(seq1)

# need to take out
#seq1 = "MQGAFGKPQGTVARVHIGQVIMSIRTKLQNKEHVIEALRRAKFKFPGRQKIHISKKWGFTKFNADEFEDMVAEKRLIPDGCGVKYIPSRGPLDKWRALHS"
#seq2 = "MRGAFGKPQGTVARVHIGQVIMSIRTKLQNKEHVIEALCRAKFKFPGRQKIHISKKWGFTKFNADEFEDMVAEKRLIPDGCGVKYIPNPGPLDKWRALHS"
#seq1list =  seq1.split(' ',1)
#seq2list =  seq2.split(' ',1)

length = len(seq1)

# print both hard coded sequences to user
print "%s\n%s" %(seq1, seq2)
samecount = float(0)
diffcount = float(0)
#print "%s" % (samecount)

# compares charater at each position to check if same
for a in range(0,length): 
#	print "%s" % (samecount)
	if seq1[a] == seq2[a]:
#		print "same"
		samecount = samecount + 1
	else:
#		print "different"
		diffcount = diffcount + 1

#calculate percent same and different and print
samepercent = float(samecount) / float(length)
diffpercent = float(diffcount) / float(length)
print "Percent similar: %s\nPercent different: %s" %(samepercent, diffpercent)

