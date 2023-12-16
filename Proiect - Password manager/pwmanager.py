import cryptocode

parola_master = 'ionela2002'


# Funcție pentru verificarea parolei master
def verificare_parola(parola_introdusa_de_utilizaor):
    if parola_master != parola_introdusa_de_utilizaor:
        print("Parola master introdusa este incorecta!")
        return False
    return True


# Funcție pentru criptarea parolei
def criptare_parola(parola):
    parola_criptata = cryptocode.encrypt(parola, parola_master)
    return parola_criptata


# Funcție pentru decriptarea parolei
def decriptare_parola(parola_criptata):
    parola_decriptata = cryptocode.decrypt(parola_criptata, parola_master)
    return parola_decriptata
