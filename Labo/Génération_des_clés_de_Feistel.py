def generateFeistelSubkeys(key):
    # Étape 2 : Appliquer la fonction de permutation H
    H = [6, 5, 2, 7, 4, 1, 3, 0]
    permutedKey = [key[H[i]] for i in range(8)]

    # Étape 3 : Diviser la clé en deux blocs de 4 bits
    k1 = permutedKey[:4]
    k2 = permutedKey[4:]

    # Étape 4 : Calculer k1 et k2
    k1_xor_k2 = [k1[i] ^ k2[i] for i in range(4)]
    k1_and_k2 = [k1[i] & k2[i] for i in range(4)]

    # Étape 5 : Appliquer les décalages
    k1Shifted = k1_xor_k2[2:] + k1_xor_k2[:2]
    k2Shifted = k1_and_k2[1:] + k1_and_k2[:1]

    # Étape 6 : Retourner les sous-clés générées
    return k1Shifted, k2Shifted

# Exemple d'utilisation
key = [1, 0, 1, 0, 0, 1, 1, 0]  # Clé de départ de longueur 8
subkey1, subkey2 = generateFeistelSubkeys(key)
print(f"La première sous-clé : {subkey1}")
print(f"La deuxième sous-clé : {subkey2} ")
