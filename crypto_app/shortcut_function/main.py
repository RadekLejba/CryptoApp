from hashlib import md5, sha1, sha224, sha256, sha384, sha512


class Shortcuter:
    def __init__(self, message):
        self.message = message
        self.encrypt()

    def to_dict(self):
        return {
            'MD5': self.encrypted_md5,
            'SHA1': self.encrypted_sha1,
            'SHA224': self.encrypted_sha224,
            'SHA256': self.encrypted_sha256,
            'SHA384': self.encrypted_sha384,
            'SHA512': self.encrypted_sha512,
        }

    def encrypt(self):
        self.encrypt_md5()
        self.encrypt_sha1()
        self.encrypt_sha224()
        self.encrypt_sha256()
        self.encrypt_sha384()
        self.encrypt_sha512()

    def encrypt_md5(self):
        self.encrypted_md5 = md5(self.message.encode('utf8')).hexdigest()

    def encrypt_sha1(self):
        self.encrypted_sha1 = sha1(self.message.encode('utf8')).hexdigest()

    def encrypt_sha224(self):
        self.encrypted_sha224 = sha224(self.message.encode('utf8')).hexdigest()

    def encrypt_sha256(self):
        self.encrypted_sha256 = sha256(self.message.encode('utf8')).hexdigest()

    def encrypt_sha384(self):
        self.encrypted_sha384 = sha384(self.message.encode('utf8')).hexdigest()

    def encrypt_sha512(self):
        self.encrypted_sha512 = sha512(self.message.encode('utf8')).hexdigest()
