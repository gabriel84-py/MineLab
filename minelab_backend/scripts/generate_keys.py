import rsa

# Générer une paire de clés RSA
(public_key, private_key) = rsa.newkeys(2048)

# Sauver la clé privée au format PKCS#1
with open("private.pem", "wb") as priv_file:
    priv_file.write(private_key.save_pkcs1(format='PEM'))

# Sauver la clé publique au format PKCS#1
with open("public.pem", "wb") as pub_file:
    pub_file.write(public_key.save_pkcs1(format='PEM'))
