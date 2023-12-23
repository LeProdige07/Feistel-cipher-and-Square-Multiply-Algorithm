# Fonction de Permutation

def laPermutation(key, permutation):
    permutedKey = [key[permutation[i]] for i in range(len(permutation))]
    return permutedKey

def generate_feistel_subkeys(key, permutation, leftShiftOrder, rightShiftOrder):
    # Appliquer la permutation donnée
    permutedKey = laPermutation(key, permutation)

    # Diviser la clé en deux blocs de 4 bits
    k1 = permutedKey[:4]
    k2 = permutedKey[4:]

    # Calculer k1 et k2
    k1_xor_k2 = [k1[i] ^ k2[i] for i in range(4)]
    k1_and_k2 = [k1[i] & k2[i] for i in range(4)]

    # Appliquer les décalages
    k1Shifted = k1_xor_k2[leftShiftOrder:] + k1_xor_k2[:leftShiftOrder]
    k2Shifted = k1_and_k2[-rightShiftOrder:] + k1_and_k2[:-rightShiftOrder]

    # Retourner les sous-clés générées
    return k1Shifted, k2Shifted

# Exemple d'utilisation
key = [1, 0, 1, 0, 0, 1, 1, 0]  # Clé de départ de longueur 8
permutation = [6, 5, 2, 7, 4, 1, 3, 0]  # Permutation personnalisée
leftShiftOrder = 2  # Ordre de décalage à gauche
rightShiftOrder = 1  # Ordre de décalage à droite

subkey1, subkey2 = generate_feistel_subkeys(key, permutation, leftShiftOrder, rightShiftOrder)
print(f"Sous-clé 1 : {subkey1}")
print(f"Sous-clé 2 : {subkey2}")
