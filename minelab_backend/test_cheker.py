from minelab_backend.app_minelab.services.license_checker import license_checker

id = 1
hash = "hello"
taille = 1


if license_checker(id, hash, taille):
    print('okay')
else:
    print('pas ok')