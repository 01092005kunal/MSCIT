from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


def blowfish_encrypt(key, plaintext):
    # Generate random 8-byte Initialization Vector (IV)
    iv = os.urandom(8)

    # Create Blowfish cipher in CBC mode
    cipher = Cipher(
        algorithms.Blowfish(key),
        modes.CBC(iv),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()

    # Blowfish block size is 64 bits (8 bytes)
    padder = padding.PKCS7(64).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    # Encrypt plaintext
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Return IV + ciphertext
    return iv + ciphertext


def blowfish_decrypt(key, ciphertext):
    # Extract IV and ciphertext
    iv = ciphertext[:8]
    actual_ciphertext = ciphertext[8:]

    # Create Blowfish cipher for decryption
    cipher = Cipher(
        algorithms.Blowfish(key),
        modes.CBC(iv),
        backend=default_backend()
    )
    decryptor = cipher.decryptor()

    # Decrypt data
    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(64).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode()


# Usage Example
key = os.urandom(16)  # Blowfish key (4-56 bytes allowed)
message = "Hello Blowfish!"

encrypted = blowfish_encrypt(key, message)
print("Encrypted Blowfish:\n", encrypted)

decrypted = blowfish_decrypt(key, encrypted)
print("Decrypted Blowfish:", decrypted)