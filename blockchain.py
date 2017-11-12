"""
Simple DIY blockchain from:
https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
"""

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self):

        pass

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined block

        :param sender: <str> Address of sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        pass

    @staticmethod
    def hash(block):
        pass

    @property
    def last_block(self):

        pass
