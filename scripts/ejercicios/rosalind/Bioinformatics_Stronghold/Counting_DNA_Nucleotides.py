# DNA seq
# dna = 'AATGGTTTAACACGTAAACGGTCGGAGGTCTGGACTCACTAAGTTGGACACTGCGGGATTGATGCCGCTCAACAACTAAAGGCGCTCAGTACATGAGTAGGAGGTAAGCTACGTCGCAGTGTATATTCGATGCCCCTACCGTCGAAGAGACCGAATTTCTCCTATTCCCTCAAAACTCTACCTCCCGCTATTCGCGGGCGGGGCTCCCCAACCCAAGAGGAGGATCTACCTATAGGTTCCCTTGTTGGGCTACAGAGGCGGAAAACAACTTTCACGCACGCCGTACAAAGGTTTGCGTCTGTACCGGTCTAGTCGTGTAACAAACCAAATGGTCTGACTTATGCAATCTGAAAGTTCTACATAGAACGTACGCGGAACTCAATCTACTCAATAGAGTTATGACTTTAGGAGGGCTACGGTTAATCCTTCCGACGGCGTATACATTGACGTTCCTCCTTATAATAGGCGAGCAGTTTGTCACAAAGCAAAGGACGTTTCTAGTACTGCCTCCGTACCTTTGCACCACCGTTGCGCGCGACGATCATAGGCACGACGGTCAATTGCGAGTTGCGACGGGTACGCAACGGGTCCCCAGCACACTACCACTCGTTGTTCGATCACAGTACAATCTGGACGCGTGTCGGTCGTCCCATCCCAAAATTAATGTTTTTTAACCTGACAAACCTAGCTTGGGAGCACTGAAGCCTCTCCGCGATGTTAGTGAGCAGTAAATCACCTCGTAGCCGTCGGACCTTGTCGCAATGATTGAGTGCAGACGTAAGGGCATCACTTATAGACTGTTTTTGCAAGTTATATATACTGTAAAGTGCATCCATTAAGCTGTCGCCAACTGGCGCACCGATTACGTTTCATACTCGATTGTGATTAATATGATCTTTGCGACCGTACGTGCCGGGACGCAACTTCACTCAACGCCCCCACTCGCACAGCATTAAACTTTTGTTATGTAGCCCGTTGGGTCGCGACGGTGTG'
dna = input("Secuencia de DNA: ")

# Counting A C G T
a = dna.count('A')
c = dna.count('C')
g = dna.count('G')
t = dna.count('T')

print(a,c,g,t)