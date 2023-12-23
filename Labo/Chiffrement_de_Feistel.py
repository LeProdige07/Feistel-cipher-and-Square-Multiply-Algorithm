# Fonction de Permutation

def laPermutation(bloc , permutation):
    blocPermutter = [bloc[permutation[i]] for i in range(len(permutation))]
    return blocPermutter

def feistelEncrypt(bloc, permutation, s_k1, s_k2):
    # Appliquer la permutation π
    blocPermutter = laPermutation(bloc, permutation)

    # Diviser le bloc en deux blocs de 4 bits
    G0 = blocPermutter[:4]
    D0 = blocPermutter[4:]

    # Premier Round
    P = [2, 0, 1, 3]
    D1 = [G0[P[i]] ^ s_k1[i] for i in range(4)]
    G1 = [D0[i] ^ (G0[i] | s_k1[i]) for i in range(4)]

    # Deuxième Round
    D2 = [G1[P[i]] ^ s_k2[i] for i in range(4)]
    G2 = [D1[i] ^ (G1[i] | s_k2[i]) for i in range(4)]

    # Concaténer G2 et D2
    C = G2 + D2

    # Appliquer l'inverse de la permutation π^(-1)
    inversePermutation = [permutation.index(i) for i in range(len(permutation))]
    blocEncrypter = laPermutation(C, inversePermutation)

    # Retourner le texte chiffré
    return blocEncrypter

# Voici un exemple 
block = [1, 0, 1, 0, 0, 1, 1, 0]  # Bloc de départ de longueur 8 bits
permutation = [4, 6, 0, 2, 7, 3, 1, 5]  # Permutation personnalisée
s_k1 = [1, 0, 1, 1]  # Sous-clé 1 de longueur 4 bits
s_k2 = [0, 1, 1, 0]  # Sous-clé 2 de longueur 4 bits

blocEncrypter = feistelEncrypt(block, permutation, s_k1, s_k2)
print(f"Voici le texte chiffré : {blocEncrypter} ")