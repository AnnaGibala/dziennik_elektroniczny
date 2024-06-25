students_in_gropu = {"JanBednarek", "JanTestowy", "SaraKostek", "AnnaMasternak"}

homework_done = set()

print("""
Dostępne opcje:
1 - Wprowadź identyfikator studenta, który oddał zadanie
2 - Wyświetl listę wszystkich stydentów
3 - Wyświetl listę stydentów, którzy oddali zadanie
4 - Wyświetl listę stydentów, którzy nie oddali zadania
5 - Zakończ program
""")

program_active = True

while program_active:

    option = int(input("Proszę podaj opcję (1-5): "))

    if option == 1:
        iden = input("Prosze podaj identyfikator studenta: ")
        if iden in students_in_gropu:
            if iden not in homework_done:
                homework_done.add(iden)
            else:
                print("Taki student już oddał swoje zadanie!")
        else:
            print("Taki student nie istnieje w tej grupie!")
    elif option == 2:
        print(students_in_gropu)
    elif option == 3:
        if len(homework_done) == 0:
            print("Jeszcze nikt nie oddał zadania!")
        else:
            print(homework_done)
    elif option == 4:
        print(students_in_gropu.difference(homework_done))
    elif option == 5:
        print("Dziękujmy za skorzystanie z programu!")
        program_active = False
    else:
        print("Wybrana opcja poza zakrestem dostępnych!")

