użytkownicy={"Admin": "1234567"}

def register(dic):
    login= input("Podaj login: ")
    password= input("Podaj hasło: ")
    repeat_password= input("Podaj hasło panownie: ")

    try:
        
        assert len(login) >= 5, "Podaj login muis mieć przjnajmniej 5 znaki"

        if not password == repeat_password : 
            raise ValueError("Hasło są nie zgodne")
        if not len(password) >= 6:
            raise ValueError("Hasło musi być przynajmniej 6 znaków")

        dodaj = { login : password}

        dic.update(dodaj)

        print(dic)

        return login , dic , password

    except AssertionError:
        print("Napotkano assertion error. Zły login. ")

    except ValueError:
        print("Napotkano value error. Zły hasło. ")


#register(użytkownicy)
