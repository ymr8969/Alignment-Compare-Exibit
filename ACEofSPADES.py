'''
Alignment Compare Exhibit
BIOL130 Final Project
Authors:
@Jamie Mortensen
@Yara Rose
@Kevin Schutt
@Madelyn Schreiner
'''
# python module that allows us interact with command line
import os

# Intro to users - Kevin Schutt
print("""Welcome to ACE. A tool that utilizes the ClustalW program and compares two dna sequences and two amino acid
sequences. Please download files from NCBI's Homologene; program is limited to handle only 2 sequences in a file at a time.
Please make sure you have ClustalW to continue""")
#  ask user for file names - Kevin Schutt
aa = raw_input("Please input amino acid text file: ")
dna = raw_input("Please input dna text file: ")

# Run clustalw on the retrieved files from homologene, save to output file - Jamie Mortensen
dna_cmd = "clustalw %s -outfile=dna_align.txt" % (dna)
aa_cmd = "clustalw %s -type=protein -outfile=aa_align.txt" % (aa)
os.system(dna_cmd)  # DNA alignment
os.system(aa_cmd)  # Protein alignment
print("Clustal alignment done")
# Yara Rose
# File reading and parsing sequences in file to desire strings
f = open('dna_align.txt', 'r')  # open output file from ClustalW
num_lines = 0
# count the number of lines
with f:
    for num_lines, l in enumerate(f):
        pass
i = 0  # initialize counter variable
f = open('dna_align.txt', 'r')
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

# Take lesser length - Jamie Mortensen
if len(seq2) > len(seq1):
	length = len(seq1)
else:
	length = len(seq2)

# print both sequences to user
print "%s\n%s" % (seq1, seq2)

samecount = float(0)
diffcount = float(0)

# compares charater at each: position to check if same
for a in range(0, length):
    if (seq1[a]=="A") or (seq1[a]=="T") or (seq1[a]=="C") or (seq1[a]=="G"): # checks to make sure valid nucleotides - Maddy Schreiner
        if seq1[a] == seq2[a] and seq2[a] != "-": # checks to make sure nucleotide positions are same and not occupied by dash (First part Jamie Mortensen, dash step Kevin Schutt
            samecount = samecount + 1
        else:
             diffcount = diffcount + 1

# calculate percent same and different and print - Jamie Mortensen
samepercent = 100 * float(samecount) / float(length)
diffpercent = 100 * float(diffcount) / float(length)
print "DNA percent similar: %s\nDNA percent different: %s" % (samepercent, diffpercent)

# same as above but for Proteins - same distribution of work
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

if len(seq2) > len(seq1):
	length = len(seq1)
else:
	length = len(seq2)

# print both sequences to user
print "%s\n%s" % (seq1, seq2)
samecount = float(0)
diffcount = float(0)

# compares charater at each position to check if same
for a in range(0, length):
    if not (seq1[a]=='B' and seq1[a]=='J' and seq1[a]=='O' and seq1[a]=='U' and seq1[a]=='X' and seq1[a]=='Z'):
         if seq1[a] == seq2[a] and seq1[a] != "-":
             samecount = samecount + 1

         else:
             diffcount = diffcount + 1

# calculate percent same and different and print
samepercent = 100 * float(samecount) / float(length)
diffpercent = 100 * float(diffcount) / float(length)
print ("Amino Acid percent similar: %s \nAmino Acid percent different: %s" )% (samepercent, diffpercent)

