import os
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[-1:])]

def encrypt_file(key, filename):
    try:
        with open(filename, 'rb') as f:
            plaintext = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.decode('latin1')).encode('latin1'))
    with open(filename, 'wb') as f:
        f.write(iv)
        f.write(ciphertext)
    print(f"File '{filename}' encrypted successfully.")

def decrypt_file(key, filename):
    try:
        with open(filename, 'rb') as f:
            iv, ciphertext = f.read(AES.block_size), f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext).decode('latin1')).encode('latin1')
    with open(filename, 'wb') as f:
        f.write(plaintext)
    print(f"File '{filename}' decrypted successfully.")


print("Note: You can use eg.txt , eg.docx , eg.pdf for example \n ")

choice = input("Enter 1 to encrypt or 2 to decrypt: ")
if choice not in ['1', '2']:
    print("Invalid choice.")
    exit()
filename = input("Enter file name: ")
key_input = input("Enter key (16/24/32 bytes): ")
if len(key_input) not in [16, 24, 32]:
    print("Invalid key length.")
    exit()
key = key_input.encode()
if os.path.splitext(filename)[1] not in {".txt", ".pdf", ".docx"}:
    print("Unsupported file type.")
else:
    encrypt_file(key, filename) if choice == '1' else decrypt_file(key, filename)
