# Checks similiarities between two hard-coded sequences and output their percent similiarity and difference


seq1 = "asdfasdfasdfasdflkjlkjflkjds"
seq2 = "asfdjasdfasdfsadfl;kjl;kjlkj"
#seq1list =  seq1.split(' ',1)
#seq2list =  seq2.split(' ',1)

length = len(seq1)

print "%s\n%s" %(seq1, seq2)
samecount = float(0)
diffcount = float(0)
print "%s" % (samecount)


for a in range(0,length): 
#	print "%s" % (samecount)
	if seq1[a] == seq2[a]:
		print "same"
		samecount = samecount + 1
	else:
		print "different"
		diffcount = diffcount + 1


samepercent = float(samecount) / float(length)
diffpercent = float(diffcount) / float(length)
print "Percent similar: %s\nPercent different: %s" %(samepercent, diffpercent)

