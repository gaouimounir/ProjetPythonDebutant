def EffectuerConversion(unit1, unit2, facteur):
    valeurStr = input(f"Conversion {unit1} -> {unit2}. Entrez la valeur en {unit1}: ")
    valeurFloat = float(valeurStr)

    try:
        valeurFloat = float(valeurStr)
    except ValueError:
        print(f"Veuillez entrer une valeur numérique valide pour {unit1}!")
        return EffectuerConversion(unit1, unit2, facteur)
    
    valeurConvertie = round(valeurFloat * facteur, 2)
    print(f"Resultat de la conversion : {valeurFloat} {unit1} = {valeurConvertie} {unit2}")


print("Ce programme vous permet d'effectuer des conversions d'unités.")
print("Choisissez parmi celles-ci:")
print("1 - Pouces vers cm")
print("2 - cm vers pouces")

choice = input("Votre choix (1 ou 2): ")

if choice == "1":
    EffectuerConversion("pouces", "cm", 2.54)

if choice == "2":
    EffectuerConversion("cm", "pouces", 0.393701)

