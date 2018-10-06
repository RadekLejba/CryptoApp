from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from Crypto.Random import OSRNG
from hashlib import md5


class AESCipher:
    block_size = AES.block_size

    def __init__(self, key):
        self.key = md5(key.encode('utf8')).hexdigest()
        self.cipher = AES.new(self.key, AES.MODE_ECB)
        self.iv = OSRNG.posix.new().read(AES.block_size)

    def pad(self, string):
        return (
            string + (self.block_size - len(string) % self.block_size) *
            chr(self.block_size - len(string) % self.block_size)
        )

    def unpad(self, string):
        return string[0:-ord(string[-1])]

    def encrypt(self, plaintext, cbc=False):
        if not cbc:
            return self.cipher.encrypt(plaintext)
        return self.encrypt_cbc(plaintext)

    def decrypt(self, ciphertext, cbc=False):
        if not cbc:
            return self.cipher.decrypt(ciphertext)
        return self.decrypt_cbc(ciphertext)

    def encrypt_cbc(self, plaintext):
        prev_block = self.iv
        block_index = 0
        ciphertext = b''

        while block_index < len(plaintext):
            block = plaintext[block_index: block_index + self.block_size]
            final_block = strxor(block, prev_block)

            cipher_block = self.encrypt(final_block)
            prev_block = cipher_block
            ciphertext += cipher_block

            block_index += self.block_size

        return ciphertext

    def decrypt_cbc(self, ciphertext):
            prev_block = self.iv
            block_index = 0
            plaintext = b''

            while block_index < len(ciphertext):
                block = ciphertext[block_index: block_index + AES.block_size]

                prep_plaintext = self.decrypt(block)
                plaintext += strxor(prev_block, prep_plaintext)
                prev_block = block

                block_index += AES.block_size

            return plaintext
