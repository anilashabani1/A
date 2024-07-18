def tekst():
    num_students = int(input("Shkruani numrin total te nxeneseve ne klase: "))
    students = {}
    for i in range(num_students):
        emri = input(f"Shkruani emrin e nxenesit {i+1}: ")
        nota = float(input(f"Shkruani noten e nxenesit {emri}: "))
        students[emri] = nota
    notat = list(students.values())
    nota_minimale = min(notat)
    nota_maximale = max(notat)
    mesatarja_e_notave = sum(notat) / num_students
    print(f"Nota minimale ne klase eshte: {nota_minimale}")
    print(f"Nota maximale ne klase esht : {nota_maximale}")
    print(f"Mesatarja e notave ne klase eshte: {mesatarja_e_notave}")
tekst()
