"""
NeuralCoin

t1: Anna sends Bob 2 NC
t2: Bob sends Daniel 4.3 NC
t3: Mark sends Charlie 3.2 NC


B1 ("AAA", t1, t2, t3) -> 76fd89, B2 ("76fd89", t4, t5, t6) -> 8923ff, B3 ("8923ff", t7)

NeuralHash()
"""
import hashlib


class NeuralCoinBlock:
    def __init__(self, previous_block_hash, *transactions):
        self.previous_block_hash = previous_block_hash
        self.transactions = transactions

        self.block_data = "-".join(transactions) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


def main():
    t1 = "Anna sends 2 NC to Mike"
    t2 = "Bob sends 4.2 NC to Mike"
    t3 = "Mike sends 3.2 NC to Bob"
    t4 = "Daniel sends 0.2 NC to Anna"
    t5 = "Anna sends 1.52 NC to Bob"
    t6 = "Anna sends 5 NC to Daniel"

    init_block = NeuralCoinBlock("Initial", t1, t2)
    print(init_block.block_data)
    print(init_block.block_hash)

    second_block = NeuralCoinBlock(init_block.block_hash, t3, t4)
    print(second_block.block_data)
    print(second_block.block_hash)

    third_block = NeuralCoinBlock(second_block.block_hash, t5, t6)
    print(third_block.block_data)
    print(third_block.block_hash)


if __name__ == "__main__":
    main()
