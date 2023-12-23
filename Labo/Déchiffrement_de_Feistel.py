# Fonction de Permutation

def laPermutation(bloc, permutation):
    blocPermutter = [bloc[permutation[i]] for i in range(len(permutation))]
    return blocPermutter

def feistelDecrypt(bloc, permutation, s_k1, s_k2):
    # Appliquer la permutation π
    blocPermutter = laPermutation(bloc, permutation)

    # Diviser le bloc en deux blocs de 4 bits
    G2 = blocPermutter[:4]
    D2 = blocPermutter[4:]

    # Premier Tour
    P = [2, 0, 1, 3]
    G1 = [P.index((D2[i] ^ s_k2[i])) for i in range(4)]
    D1 = [G2[i] ^ (G1[i] | s_k2[i]) for i in range(4)]

    # Deuxième Tour
    G0 = [P.index((D1[i] ^ s_k1[i])) for i in range(4)]
    D0 = [G1[i] ^ (G0[i] | s_k1[i]) for i in range(4)]

    # Concaténer G0 et D0
    N = G0 + D0

    # Appliquer l'inverse de la permutation π^(-1)
    inversePermutation = [permutation.index(i) for i in range(len(permutation))]
    decryptedBloc = laPermutation(N, inversePermutation)

    # Retourner le texte clair
    return decryptedBloc

# Voici un exemple
bloc = [1, 1, 0, 0, 0, 1, 1, 1]  # Bloc chiffré de longueur 8 bits
permutation = [4, 6, 0, 2, 7, 3, 1, 5]  # Permutation personnalisée
s_k1 = [1, 0, 1, 1]  # Sous-clé 1 de longueur 4 bits
s_k2 = [0, 1, 1, 0]  # Sous-clé 2 de longueur 4 bits

decryptedBloc = feistelDecrypt(bloc, permutation, s_k1, s_k2)
print(f"Le Texte clair est le suivant {decryptedBloc}")
