

def encrypt(s):
    print s
def decrypt(s):
    print s
text = raw_input("Enter the data you want to encripyt of decripyt\n")
s = raw_input("'E' for Encryption\n'D' for Decryption")
if s == 'E' or s =='e':
    encrypt(text)
elif s == "D" or  s == "d" :
    decrypt(text)
else:
    print("Entry Invalid !!")

