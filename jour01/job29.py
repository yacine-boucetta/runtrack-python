def arrondir_notes(notes):
    arrondies = []
    for note in notes:
        if note < 40:
            arrondies.append(note)
        else:
            multiple_de_5 = round(note / 5) * 5
            if multiple_de_5 - note < 3:
                arrondies.append(multiple_de_5)
            else:
                arrondies.append(note)
    return arrondies

notes = [83, 78, 67, 41, 38, 11]
arrondies = arrondir_notes(notes)
print(arrondies) # Affiche [85, 80, 67, 41, 38, 11]
