import os
import pyaes

## abrir aquivo cripto

file_name = 'teste.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## chave de decripto

key = b"testeransomware"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remove arquivo cripto
os.remove(file_name)

##cria um novo descripto

new_file = 'teste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()
