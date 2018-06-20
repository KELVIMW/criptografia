from Crypto.PublicKey import RSA

#Gerar um par de chaves publica/privada usando o comprimento de chave de 4096 bits
new_key = RSA.generate(4096, e=65537)
#codifica o exponente e modulo da chave para o formate PEM
private_key = new_key.exportKey("PEM")
public_key = new_key.publickey().exportKey("PEM")

#cria os arquivos
fd = open("private_key.pem", "wb")
fd.write(private_key)
fd.close()

fd = open("public_key.pem", "wb")
fd.write(public_key)
fd.close()

print('Chaves geradas com sucesso')
