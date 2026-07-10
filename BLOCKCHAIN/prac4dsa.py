from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import  hashes


private_key = dsa.generate_private_key(key_size=2048)

def dsa_sign(private_key,message):
    signature = private_key.sign(
        message.encode(),
        hashes.SHA256()
    )
    return signature

def dsa_verify(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode(),
            hashes.SHA256()

            )
        return True
    except:
        return False
    
message = "HELLO DSAI"
signature = dsa_sign(private_key,message)
public_key = private_key.public_key()

print("Signature valid?",dsa_verify(public_key,message,signature))