import rsa
import json
import base64

def signer_json(data_dict: dict):
    with open("/Users/gabrieljeanvermeille/PycharmProjects/MineLab/private.pem", "rb") as f:
        privkey = rsa.PrivateKey.load_pkcs1(f.read())

    message = json.dumps(data_dict).encode()
    signature = rsa.sign(message, privkey, 'SHA-256')

    return {
        "message": base64.b64encode(message).decode(),
        "signature": base64.b64encode(signature).decode()
    }




def verifier_signature(response: dict) -> bool:
    with open("/Users/gabrieljeanvermeille/PycharmProjects/MineLab/public.pem", "rb") as f:
        pubkey = rsa.PublicKey.load_pkcs1(f.read())

    message = response["message"].encode()
    signature = base64.b64decode(response["signature"])

    try:
        rsa.verify(message, signature, pubkey)
        return True  # signature OK
    except rsa.VerificationError:
        return False  # signature invalide


if __name__ == "__main__":
    data = {
        "status": "error",
        "message": "Licence et plugin introuvables."
    }
    signe = signer_json(data)
    print(verifier_signature(signe))