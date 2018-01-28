"""
 Bismuth Public Key Regenerator
 Test Version 0.0.1
 Date 28/01/2018
 Copyright Maccaspacca 2018
 Copyright Hclivess 2016 to 2018
 Author Maccaspacca
"""

import base64, os, getpass, hashlib, pathlib
from Crypto import Random
from simplecrypt import decrypt
from Crypto.PublicKey import RSA

try:
	# import key from private key file

	if not os.path.exists('privkey_encrypted.der'):
		key = RSA.importKey(open('privkey.der').read())

	else:
		password = getpass.getpass()
		encrypted_privkey = open('privkey_encrypted.der').read()
		decrypted_privkey = decrypt(password, base64.b64decode(encrypted_privkey))
		key = RSA.importKey(decrypted_privkey)
		
	# import key from private key file

	# regenerate public key

	public_key = key.publickey()
	private_key_readable = key.exportKey().decode("utf-8")
	public_key_readable = key.publickey().exportKey().decode("utf-8")

	if (len(public_key_readable)) != 271 and (len(public_key_readable)) != 799:
		raise ValueError("Invalid public key length: {}".format(len(public_key_readable)))

	address = hashlib.sha224(public_key_readable.encode("utf-8")).hexdigest()  # hashed public key
		
	# regenerate public key

	# write der files out into separate folder

	pathlib.Path(address).mkdir(parents=True, exist_ok=True)

	pem_file = open("{}/privkey.der".format(address), 'a')
	pem_file.write(str(private_key_readable))
	pem_file.close()

	pem_file = open("{}/pubkey.der".format(address), 'a')
	pem_file.write(str(public_key_readable))
	pem_file.close()

	address_file = open("{}/address.txt".format(address), 'a')
	address_file.write(str(address) + "\n")
	address_file.close()
	
	print("pubkey.der and privkey.der regenerated in folder {}".format(address))
	
except:
	print("There was a problem or corruption so I cannot help you")
	



