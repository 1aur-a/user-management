

import os
import json
import hashlib

# REGISTER USERS

def register_user():
    username = input('Insert your username: ')
    password = input ('Enter password: ')
    email = input ('Enter email: ')
    
    # Ladda befintliga användare
    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
          users = json.load(file)
    else:
        users = {}  # om filen inte finns än

    # Kontrollera om användarnamnet redan finns
    if username in users:
        print ("Användarnamnet finns redan!")
        return # Avsluta funktionen tidigt
    
    # Hasha lösernordet
    password_bytes = password.encode() #Omvandlar lösenordet till bytes.
    hashed_password = hashlib.sha256(password_bytes).hexdigest() # Skapar en SHA-256 hash av bytes. # Omvandlar resultatet till en läsbar textsträng (hexadecimal form).
    
    # Lägg till användare
    users[username] = {
        "email": email,
        "password": hashed_password
    }

    # Spara till fil
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

    print("Användaren har registrerats!")

    print ('Username:', username)
    print ('Email: ', email)

register_user()

# INLOG

def login_user():
    input('Username: ')
    input('Password: ')

    if username ==