from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import zlib

# Função de descriptografia
def decrypt_blob(encrypted_blob, private_key):

    # Importar as chave privada e usar para descriptografia usando PKCS1_OAEP
    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)
    # Decodifica(base64) e descriptografar os dados
    encrypted_blob = base64.b64decode(encrypted_blob)
    chunk_size = 512
    decrypted = ""
    chunk = encrypted_blob[0:0 + chunk_size]
    decrypted = rsakey.decrypt(chunk)

    # retorna os dados descriptografados descompactados
    return zlib.decompress(decrypted)

# Use a chave privada para descriptografia
fd = open("private_key.pem", "rb")
private_key = fd.read()
fd.close()

# Arquivo candidato a ser descriptografado
fd = open("encrypted.txt", "rb")
encrypted_blob = fd.read()
fd.close()

# Decodifica(utf-8) e exibe o conteúdo descriptografado
msg = decrypt_blob(encrypted_blob, private_key)
msg = msg.decode('utf-8')
print(msg)
