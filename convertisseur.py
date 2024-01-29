print("Ce programme vous permet d'eefectuer des conversions d'unités.")
print("Choisissez parmi celles-ci:")
print("1 - Pouces vers cm")
print("2 - cm vers pouces")

choice = input("Votre choix (1 ou 2): ")

if choice == "1":
    valeurStr = input("Conversion Pouces -> cm. Entrez la valeur en pouces: ")
    valeurFloat = float(valeurStr)
    valeurConvertie = round(valeurFloat * 2.54, 2)
    print(f"Resultat de la conversion : {valeurFloat} pouces = {valeurConvertie} cm")

if choice == "2":
    valeurStr = input("Conversion Pouces -> cm. Entrez la valeur en pouces: ")
    valeurFloat = float(valeurStr)
    valeurConvertie = round(valeurFloat * 2.54, 2)
    print(f"Resultat de la conversion : {valeurFloat} pouces = {valeurConvertie} cm")