from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


def aes_encrypt(key, plaintext):
    # Generate a random 16-byte Initialization Vector (IV)
    iv = os.urandom(16)

    # Create AES cipher in CBC mode
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()

    # Pad plaintext to AES block size (16 bytes)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Return IV + ciphertext
    return iv + ciphertext


def aes_decrypt(key, ciphertext):
    # Extract IV and ciphertext
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]

    # Create AES cipher for decryption
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()

    # Remove PKCS7 padding
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    # Return the original plaintext
    return plaintext.decode()


# Usage Example
key = os.urandom(32)  # AES-256 key (32 bytes)
message = "Hello AES!"

encrypted = aes_encrypt(key, message)
print("Encrypted AES:\n", encrypted)

decrypted = aes_decrypt(key, encrypted)
print("Decrypted AES:", decrypted)