peptide_dict = {'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 
'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GCU': 
'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L'}

def rna_to_peptide(R_S,P_D):
    Max = len(R_S) - 3
    P = ''
    i = 0
    while i <= Max:
        a = R_S[i:i+3]
        if P_D[a] == '*':
            break
        else: 
            P = P + P_D[a]
        i += 3
    return P


while True:
    SEQ = input('Enter the sequence to translate: ')
    if SEQ == '/':
        break
    elif 'T' in SEQ:
        SEQ = SEQ.replace('T','U')
    Protein = rna_to_peptide(SEQ,peptide_dict)
    print('Peptide sequence: ', Protein)