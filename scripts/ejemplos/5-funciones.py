def get_at_content(dna, sig_figs = 2): # declaramos una variable como argumento
    dna = dna.replace("N","")
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) /length
    return round(at_content, sig_figs) # la usamos

print(get_at_content("ATGC"))
assert get_at_content("ATGC") == 0.5
assert get_at_content("ATGCNNNNNNNNNN") == 0.5
