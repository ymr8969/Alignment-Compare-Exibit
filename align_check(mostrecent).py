# python modual that allows us interact with command line
import os

# user needs to download homologene file
print("Welcome to ACE. A tool that utilizes the clustalw program and compares two dna sequences and two amino acid sequences. Fatsfa files are needed from homologenome.")
#  ask user for file name???
print("Please input amino acid text file: ")
aa = raw_input()
print("Please input dna text file")
dna = raw_input()
# tell user that they can only input 2 sequences at a time

# types string  bellow into command line, tells clustul to take in first file, allign and output 2nd file
# Run clustalw on the generated files from homologene that contains multiple homologous sequences
os.system("clustalw dna -outfile=dna_align.out") # DNA alignment
os.system("clustalw aa -type=protein -outfile=aa_align.out") # Protein alignment

# Parse files (dna and aa) to obtain both sequences and store them in variables
# Checks similiarities between two hard-coded sequences and output their percent similiarity and difference

# yara Rose
# read in file
#ask user for file name

# need to take out
seq1 = "MQGAFGKPQGTVARVHIGQVIMSIRTKLQNKEHVIEALRRAKFKFPGRQKIHISKKWGFTKFNADEFEDMVAEKRLIPDGCGVKYIPSRGPLDKWRALHS"
seq2 = "MRGAFGKPQGTVARVHIGQVIMSIRTKLQNKEHVIEALCRAKFKFPGRQKIHISKKWGFTKFNADEFEDMVAEKRLIPDGCGVKYIPNPGPLDKWRALHS"
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

