#I am using the cryptography library because of a symmetric encryption method I will be using for this project called Fernet
import cryptography
from cryptography import fernet

#Alias for the fernet module
f = cryptography.fernet

#Asks user if they are making a new key or old key
Newold = input("Are you generating a (N)ew key or reusing an (O)ld key ")

if Newold.lower() == "n":
    key = f.Fernet.generate_key() #generates a new key
    print_key = key.decode("ASCII") #creates variable to save the new key and decodes the key into ascii
    print(print_key) #shows user created key
elif Newold.lower() == "o":
    key = input("Paste key: \n") #user pastes old key
    key = key.encode("ASCII") #converts to bytes for fernet
else:
    print("Please input either N or O") #shuts down program for not using n or o
