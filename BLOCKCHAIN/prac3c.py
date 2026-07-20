import hashlib
import datetime
import json

class Block:
    def __init__(self, transactions, previous_hash="0"*64):
        self.index = 0
        self.timestamp = str(datetime.datetime.now())
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True)

        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return (
            f"Block index: {self.index}\n"
            f"Timestamp: {self.timestamp}\n"
            f"Transactions:\n" +
            "\n".join(f" - {tx}" for tx in self.transactions) + "\n"
            f"Previous hash: {self.previous_hash}\n"
            f"Hash: {self.hash}\n"
        )

transactions = [
    "Alice pays Bob 5 BTC",
    "Bob pays Charlie 2 BTC",
    "Charlie pays Dave 1 BTC"
]

block = Block(transactions)
print(block)                    