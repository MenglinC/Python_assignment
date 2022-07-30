sequences = ["ATGCATGCATGCATCGTAGCTACG",
			 "CCGATCGAGCTGTCTAGCTATCGC",
			 "AAATGCGGACACGTAGCTGTAGCC",
			 "ATGAATACATACAACGAAGCTACG"]

def identity(s1,s2,fraction=True):
	if len(s1)!=len(s2):
		return None
	identity = 0
	for n1,n2 in zip(s1,s2):
		if n1 == n2:
			identity+=1
	if fraction:
		return identity/len(s1)
	else:
		return identity


for seq1 in sequences:
	for seq2 in sequences:
		print("I(%s,%s) = %.2f" % (seq1,seq2,identity(seq1,seq2))) 