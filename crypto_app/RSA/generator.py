import random
import sys
from math import gcd as bltin_gcd

from prime import generateLargePrime


class RSAGenerator():
    stats_e = 0
    stats_n = 0

    def __init__(self, p=None, q=None):
        if not p:
            self.p = generateLargePrime(1024)
        else:
            self.p = p
        if not q:
            self.q = generateLargePrime(1024)
        else:
            self.q = q
        print('generating e')
        self.e = self.generate_e()
        print('e generated, primes generated until success: {} \n'.format(self.stats_e))
        self.d = self.modinv(self.e, self.phi)
        print('d generated, recursion depth: {} \n'.format(self.stats_n))

    @property
    def phi(self):
        return (self.p - 1) * (self.q - 1)

    @property
    def n(self):
        return self.p * self.q

    def egcd(self, a, b):
        """
        functions for modular inverse (from stack overflow:
        http://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python)
        """
        self.stats_n += 1
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(self, a, m):
        """
        functions for modular inverse (from stack overflow:
        http://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python)
        """
        print('Comparing a and g with modular inverse \n')
        sys.setrecursionlimit(1500)
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist \n')
        else:
            return x % m

    def generate_e(self):
        print('Checking e and phi for relative prime \n')
        while 1:
            self.stats_e += 1
            e = random.randrange(4, self.phi)
            if self.are_relatively_prime(e, self.phi):
                return e

    def are_relatively_prime(self, a, b):
        if bltin_gcd(a, b) == 1:
            return True
        return False


class PublicKey():
    def __init__(self, e, n):
        self.e = e
        self.n = n

    def encrypt(self, x):
        return pow(x, self.e, self.n)


class PrivateKey():
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def decrypt(self, x):
        return pow(x, self.d, self.n)
