def create_substitution_matrix(alphabet,match,mismatch):
	n = len(alphabet)
	submat = {}
	for i in range(n):
		for j in range(n):
			if alphabet[i]==alphabet[j]:
				submat[alphabet[i]+alphabet[j]] = match
			else:
				submat[alphabet[i]+alphabet[j]] = mismatch
	return submat
	
alphabet = ["A","T","G","C"]
submat_dna = create_substitution_matrix(alphabet,5,-4)
print("submat for dna alphabet:")
print(submat_dna)

alphabet = ["A","R","N","D","C","Q","E"]
submat_aa = create_substitution_matrix(alphabet,5,-4)
print("submat for aa alphabet:")
print(submat_aa)
