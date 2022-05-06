# We can replace a part of a string stored inside a variable by first coding the variables name and the instruction "replace()".

special = "Todays special is pasta"
new_special = special.replace("pasta", "pizza")
print(special)
print(new_special)

special = "Todays special is pasta"
special = special.replace("pasta", "pizza")
print(special)

# Splitting and updating strings to trasform DNA sequences into RNA sequences.

sequences = "tatsdttttcc#tatagggtctge#ctattcaatg"
dna_list = sequences.split("#")
print(dna_list)

for dna in dna_list:
    rna = dna.replace("t", "u")
    print(f"DNA: {dna} -> RNA: {rna}")