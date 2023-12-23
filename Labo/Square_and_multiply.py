def squareAndMultiply(x, b, n):
    # Conversion de l'exposant b en binaire
    binaryExponent = bin(b)[2:]

    # Initialisation du résultat à 1
    resultat = 1

    # Parcours du binaire de droite à gauche
    for bit in binaryExponent[::-1]:
        # Étape du carré
        resultat = (resultat * resultat) % n

        # Si le bit est égal à 1, effectuer une multiplication de plus
        if bit == '1':
            resultat = (resultat * x) % n

    return resultat

# Demande à l'utilisateur d'entrer les valeurs de x, b et n
x = int(input("Veuillez entrer la valeur de x : "))
b = int(input("Veuillez entrer  la valeur de b : "))
n = int(input("Veuillez entrer  la valeur de n : "))

# Appel de l'algorithme des carrés et des multiplications
resultat = squareAndMultiply(x, b, n)

# Affichage du résultat
print(f"Résultat : {resultat}")
