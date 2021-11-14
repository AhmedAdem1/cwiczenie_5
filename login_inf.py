import dodaj_uz
while True:

 def wybór_opcji():
    
    print('1-Dodaj użytkownik')
    print('2-Zobacz użytkowników')
    print('3-Zmień moje hasło')
    print('4-Usuń moje konto ')
    print('5-Wyjście ')

    option= input(" Wybierz opcji: ")

    if option == "1":
        dodaj_uz.register(dodaj_uz.użytkownicy)
    elif option=="2":
        for key in dodaj_uz.użytkownicy:
            print(key)
    elif option=="3":
        login= input("Podaj swój login: ")
        password= input("Podaj swój hasło: ")
        if login in dodaj_uz.użytkownicy and password in dodaj_uz.użytkownicy.values():
            print("Taki użytkownik istnieje")
            print(dodaj_uz.użytkownicy)
            dodaj_uz.użytkownicy.update({login: input("Podaj nowy hasło: ")})
            print(dodaj_uz.użytkownicy)

        else:
            print("Zły login lub hasło")

    elif option=="4":
         login= input("Podaj swój login: ")
         password= input("Podaj swój hasło: ")
         if login in dodaj_uz.użytkownicy and password in dodaj_uz.użytkownicy.values():
            print(dodaj_uz.użytkownicy)
            dodaj_uz.użytkownicy.pop(login)
            print(dodaj_uz.użytkownicy)
         else:
            print("Zły login lub hasło")

    elif option=="5":
        quit()
    
    else:
        print("Nie ma takiej opcji")

 
 
 wybór_opcji()


    

        