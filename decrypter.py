import os
import pyaes

# Nome do arquivo criptografado
encrypted_file = "teste.txt.ransomwaretroll"

def decrypt_file(file_path, key):
    """Descriptografa um arquivo usando AES-CTR."""
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted_data = aes.decrypt(encrypted_data)
    
    return decrypted_data

# Chave para descriptografia
key = b"testeransomwares"

decrypted_data = decrypt_file(encrypted_file, key)

# Remover o arquivo criptografado
os.remove(encrypted_file)

# Criar o arquivo descriptografado
decrypted_file = "teste.txt"
with open(decrypted_file, "wb") as file:
    file.write(decrypted_data)

print(f"Arquivo '{decrypted_file}' descriptografado com sucesso.")
