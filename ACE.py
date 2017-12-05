# python modual that allows us interact with command line
import os

# Intro to users
print("Welcome to ACE. A tool that utilizes the ClustalW program and compares two dna sequences and two amino acid "
      "sequences. Please download files from NCBI's Homologene; program is limited to handle only 2 sequences in a file at a time."
      "Please make sure you have ClustalW to continue")
#  ask user for file names
print("Please input amino acid text file: ")
aa = raw_input()
print("Please input dna text file")
dna = raw_input()

# Run clustalw on the retrieved files from homologene, save to output file
dna_cmd = "clustalw %s -outfile=dna_align.txt" %(dna)
aa_cmd = "clustalw %s -type=protein -outfile=aa_align.txt" %(aa)
os.system(dna_cmd) # DNA alignment
os.system(aa_cmd) # Protein alignment


# Yara Rose
#  File reading and parsing sequences in file to desire strings
f = open('dna_align.txt', 'r') #open output file from ClustalW
num_lines = 0
# count the number of lines
with f:
    for num_lines, l in enumerate(f):
        pass

i = 0 # initialize counter variable
f = open('dna_align.txt', 'r')
f.readline() # need to skip over first 3 lines
f.readline()
f.readline()
seq1 = '' # initialize sequence 1
seq2 = '' # initialize sequence 2
while i< (num_lines-3):
    # reads a line, and cuts out identification segment, only saves sequence
    line1 = (f.readline())
    split1 = line1.split('.', 1)
    seq1 += split1[1]

    line2 = (f.readline())
    split2 = line2.split('.', 1)
    seq2 += split2[1]

    f.readline()
    f.readline()
    i += 4

seq1 = seq1.replace(' ','')
seq2 = seq2.replace(' ','')

length = len(seq1)

# print both sequences to user
print "%s\n%s" %(seq1, seq2)
samecount = float(0)
diffcount = float(0)

# compares charater at each position to check if same
for a in range(0,length): 
	if seq1[a] == seq2[a] and seq1[a] != "-":
		samecount = samecount + 1
		
	else:
		diffcount = diffcount + 1

# calculate percent same and different and print
samepercent = float(samecount) / float(length)
diffpercent = float(diffcount) / float(length)
print "DNA percent similar: %s\nDNA percent different: %s" %(samepercent, diffpercent)



# same as above but for Proteins

f = open('aa_align.txt', 'r')  # open output file from ClustalW
num_lines = 0
# count the number of lines
with f:
    for num_lines, l in enumerate(f):
        pass

i = 0  # initialize counter variable
f = open('aa_align.txt', 'r')
f.readline()  # need to skip over first 3 lines
f.readline()
f.readline()
seq1 = ''  # initialize sequence 1
seq2 = ''  # initialize sequence 2
while i < (num_lines - 3):
    # reads a line, and cuts out identification segment, only saves sequence
    line1 = (f.readline())
    split1 = line1.split('.', 1)
    seq1 += split1[1]

    line2 = (f.readline())
    split2 = line2.split('.', 1)
    seq2 += split2[1]

    f.readline()
    f.readline()
    i += 4

seq1 = seq1.replace(' ', '')
seq2 = seq2.replace(' ', '')

length = len(seq1)

# print both sequences to user
print
"%s\n%s" % (seq1, seq2)
samecount = float(0)
diffcount = float(0)

# compares charater at each position to check if same
for a in range(0, length):
    if seq1[a] == seq2[a] and seq1[a] != "-":
        samecount = samecount + 1

    else:
        diffcount = diffcount + 1

# calculate percent same and different and print
samepercent = float(samecount) / float(length)
diffpercent = float(diffcount) / float(length)
print
"Amino Acid percent similar: %s\nAmino Acid percent different: %s" % (samepercent, diffpercent)

