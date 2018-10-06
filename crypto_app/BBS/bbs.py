#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from prime import generateLargePrime


class BlumBlumShub(object):
    output = 0
    p = 0
    q = 0

    def __init__(self, bits):
        self.n = self.generateN(int(bits))
        length = self.n.bit_length()
        seed = random.getrandbits(length)
        self.setSeed(seed)

    def getPrime(self, bits):
        while True:
            p = generateLargePrime(bits)
            if p & 3 == 3:
                return p

    def generateN(self, bits):
        p = self.getPrime(bits / 2)
        while 1:
            q = self.getPrime(bits / 2)
            if p != q:
                self.p = p
                self.q = q
                return p * q

    def setSeed(self, seed):
        self.state = seed % self.n

    def generate(self, numBits):
        result = 0
        for i in range(int(numBits)):
            self.state = (self.state**2) % self.n
            result = (result << 1) | (self.state & 1)
        self.output = result
        return result
