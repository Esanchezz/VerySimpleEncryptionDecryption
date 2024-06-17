#I am using the cryptography library because of a symmetric encryption method I will be using for this project called Fernet
import cryptography
from cryptography import fernet

#Alias for the fernet module
f = cryptography.fernet

#Asks user if they are making a new key or old key
Newold = input("Are you generating a (N)ew key or reusing an (O)ld key ")

if Newold.lower() == "n":
    key = f.Fernet.generate_key() #generates a new key
    print_key = key.decode("ASCII") #converts to bytes for fernet
    print("This is your KEY:   " + print_key) #shows user created key
elif Newold.lower() == "o":
    key = input("Paste KEY: \n") #user pastes old key
    key = key.encode("ASCII") #converts to bytes for fernet
else:
    print("Please input either N or O") #shuts down program for not using n or o

def decryption(): #decryption function: allows users to decrypt message
    paste = input("Paste message:   \n")
    paste = paste.encode("ASCII") #converts to bytes for fernet
    paste = f.Fernet(key).decrypt(paste) #decrypts user inputed message
    print("This is your DECRYPTED MESSAGE:  " + paste.decode("ASCII")) #shows inputed decrypted message

def encryption(): #encryption function: allows users to encrypt message
    message = input("Enter message: \n")
    message = message.encode("ASCII") #converts to bytes for fernet
    message = f.Fernet(key).encrypt(message) #encrypts user inputed message
    print("This is your ENCRYPTED MESSAGE:  " + message.decode("ASCII")) #shows user's encrypted message

while True:
    process = input("(E)ncrypt or (D)ecrypt or (Q)uit?   \n") #user input options
    if process.lower() == "q": #kills process
        break
    elif process.lower() == "d": #user initiates decrypts message
        decryption()
    elif process.lower() == "e": #user initiates encrypt message
        encryption()
    else: #checks if user only put allowed input options
        print("Please check entry again.")