import base64, os, getpass, hashlib
from Crypto import Random
from simplecrypt import decrypt
from Crypto.PublicKey import RSA


# import keys
if not os.path.exists('privkey_encrypted.der'):
	print("Warning: privkey_encrypted.der not found !!")
	pass
else:
	password = getpass.getpass()
	encrypted_privkey = open('privkey_encrypted.der').read()
	decrypted_privkey = decrypt(password, base64.b64decode(encrypted_privkey))
	key = RSA.importKey(decrypted_privkey)  # be able to sign
	private_key_readable = key.exportKey().decode("utf-8")

	public_key_readable = open('pubkey.der').read()

	if (len(public_key_readable)) != 271 and (len(public_key_readable)) != 799:
		raise ValueError("Invalid public key length: {}".format(len(public_key_readable)))

	public_key_hashed = base64.b64encode(public_key_readable.encode("utf-8")).decode("utf-8")
	address = hashlib.sha224(public_key_readable.encode("utf-8")).hexdigest()
	# import keys
	
	
	print("")
	print("Your BIS address is: {}".format(address))
	print("")
	if private_key_readable:
		print("Private Key is readable")
	if public_key_readable:
		print("Public Key is readable")
	if public_key_hashed:
		print("Public can be hashed")
