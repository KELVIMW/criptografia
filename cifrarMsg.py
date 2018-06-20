from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64

#função de criptografia
def encrypt_blob(blob, public_key):
    #importa a chave publica
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    #comprimi os dados para o uso da chave
    blob = zlib.compress(blob)
    chunk_size = 470
    end_loop = False
    encrypted =  ""
    chunk = blob[0:0 + chunk_size]
    
    # criptografa os dados compactados
    encrypted = rsa_key.encrypt(chunk)

    # Base64 codifica o arquivo criptografado
    return base64.b64encode(encrypted)

# Use a chave pública para criptografia
fd = open("public_key.pem", "rb")
public_key = fd.read()
fd.close()

# mensagem a ser criptografado
unencrypted_blob = input('Mensagem a ser cifrada: ')
unencrypted_blob = unencrypted_blob.encode('utf-8')
encrypted_blob = encrypt_blob(unencrypted_blob, public_key)

# Grava o conteúdo criptografado em um arquivo
fd = open("encrypted.txt", "wb")
fd.write(encrypted_blob)
fd.close()
print('a mensagem foi criptografada com sucesso')
