import hashlib
import hmac
def generate_hash(data):
    hash_object= hashlib.sha256()
    hash_object.update(data.encode())
    return hash_object.hexdigest()

def verify_hash(data, original_hash):
    new_hash = generate_hash(data)
    return new_hash == original_hash

def check_data_integrity (data, original_hash):
    if verify_hash(data , original_hash):
        print("Data is intact and verified")
    else:
        print("Warning : Data has been tampered with!")

original_data = "this is a secret message"
hash_value = generate_hash(original_data)
print(f"Original hash: {hash_value}\n")

print("checking original data:")
check_data_integrity(original_data, hash_value)

tampered_data = "this is a hacked message."
print("\n CHecking the tampered data.")
check_data_integrity(tampered_data, hash_value)

tampered_data_space = "This is a secret message. "
print("\n checking data with added space:")
check_data_integrity(tampered_data_space, hash_value)

tampered_data_char = "This is a seet message."
print("\n Checking the data with missing charecters: ")
check_data_integrity(tampered_data_char,  hash_value)