from pprint import pprint

# Überprüfen, ob die Eingabe nicht leer ist

def input_with_prompt(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():  
            return user_input
        else:
            print("Fehler: Die Eingabe darf nicht leer sein. Bitte geben Sie eine gültige Eingabe ein.")

# Eingaben ------------------------------------------------------------

while True:
    try:
        game = input_with_prompt("Für welches Game möchtest du farmen?\n")
        spielfigur = input_with_prompt("Für welchen Character möchtest du farmen?\n")
        anzahl_matz = int(input_with_prompt("Wie viele verschiedene Matz möchtest du farmen?\n"))

        if anzahl_matz <= 0:
            raise ValueError("Die Anzahl der Matz muss größer als 0 sein.")

        break  # Wenn alle Eingaben erfolgreich waren, verlasse die Schleife

    except ValueError as e:
        print(f"Fehler: {e}. Bitte gib die Informationen erneut ein.")

# Matz array Eingaben ---------------------------------------------------
matz_arrayz = []

for i in range(anzahl_matz):
    print(f"\nEingabe für Material {i+1}:\n")
    matzname = input_with_prompt("Gib den Namen für das Material an:\n")

    while True:
        try:
            matzanzahl_input = input_with_prompt("Gib die Droppmänge für das Material an:\n")
            matzanzahl = int(matzanzahl_input)
            if matzanzahl <= 0:
                raise ValueError("Die Anzahl der Matz muss größer als 0 sein.")
            break
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine ganze Zahl größer als 0 ein.")

    while True:
        droppchance_input = input_with_prompt("Wie hoch ist die Droppchance für das Material (Prozent in Zahl)?\n")
        try:
            droppchance = float(droppchance_input)
            if not (0 <= droppchance <= 100):
                raise ValueError("Die Droppchance muss zwischen 0 und 100 liegen.")
            break
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Dezimalzahl zwischen 0 und 100 ein.")

    matzort = input_with_prompt("Gib den Ort für das Material an:\n")

    matz_info = [matzname, matzanzahl, droppchance, matzort]
    matz_arrayz.append(matz_info)

    korrektur = input(f"Möchtest du etwas von den Eingaben für Material {i+1} ändern? (ja / nein)\n")
    if korrektur.lower() != 'nein':
        print(f"Korrektur für Material {i+1} durchgeführt.")

print("Deine Matz, die du famen möchtest, sind: ", matz_arrayz)

# Berechnung -----------------------------------------------------------

# Ausgabe des gesamten Arrays in die Datei schreiben
with open(f"{game}_{spielfigur}_daten.txt", 'w') as datei:
    
    datei.write("\nMinimale und maximale Wiederholungen:\n\n")

    # Berechnung und Schreiben für jedes Material im Array
    for i, material in enumerate(matz_arrayz):
        matzname = material[0]  # Ändern
        matzanzahl = material[1]  # Ändern
        droppchance_prozent = material[2]
        droppchance = droppchance_prozent / 100
        matzort = material[3]
        
        ziel_anzahl = int(input(f"Bitte die Zielanzahl für Material {i+1} ({matzname}) ein:\n"))

        min_wiederholungen = int(ziel_anzahl / matzanzahl)
        max_wiederholungen = int(ziel_anzahl / (matzanzahl * droppchance))

        # wenn das ergebnis unter 1 sein sollte
        if min_wiederholungen < 1:
            min_wiederholungen = 1
        if max_wiederholungen < 1:
            max_wiederholungen = 1

        # Schreiben in die Datei
        datei.write(f"Das Material: {matzname}\n")
        datei.write(f"mit einer Zielanzahl von: {ziel_anzahl},\n")
        datei.write(f"einer Droppmänge von: {matzanzahl} und einer Droppchance von: {droppchance * 100}%\n")
        datei.write(f"sollte es an dem Ort {matzort}\n")
        datei.write(f"Minimale Wiederholungen: {min_wiederholungen}\n")
        datei.write(f"Maximale Wiederholungen: {max_wiederholungen}\n")
        datei.write("benötigen\n")
        datei.write("---------\n")

print(f"Daten wurden in '{game}_{spielfigur}_daten.txt' gespeichert.")
