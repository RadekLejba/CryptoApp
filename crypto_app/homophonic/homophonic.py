#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import math
import random
import pickle


class HomophonicGenerator(object):
    APPEARANCES = {
        'a': 0.0891,
        'ą': 0.0099,
        'b': 0.0147,
        'c': 0.0396,
        'ć': 0.004,
        'd': 0.0325,
        'e': 0.0766,
        'ę': 0.0111,
        'f': 0.003,
        'g': 0.0142,
        'h': 0.0108,
        'i': 0.0821,
        'j': 0.0228,
        'k': 0.0351,
        'l': 0.0210,
        'ł': 0.0182,
        'm': 0.0280,
        'n': 0.0552,
        'ń': 0.002,
        'o': 0.0775,
        'ó': 0.0085,
        'p': 0.0313,
        'q': 0.0014,
        'r': 0.0469,
        's': 0.0432,
        'ś': 0.0066,
        't': 0.0398,
        'u': 0.025,
        'v': 0.004,
        'w': 0.0465,
        'x': 0.002,
        'y': 0.0376,
        'z': 0.0564,
        'ź': 0.006,
        'ż': 0.083
    }
    encode_table = {}
    SPECIAL_CHARACTERS = [' ', ',', '.', '!', '?', '/', '"', '\n', '(', ')']
    table_name = 'encode_table'

    def chunkstring(self, string, length):
        return (
            string[0 + i:length + i] for i in range(0, len(string), length)
        )

    def pick_random_value(self, letter):
        return str(random.choice(self.encode_table[letter]))

    def generate(self, generate=True):
        if generate:
            values = random.sample(range(100, 300), 150)
            for letter, value in self.APPEARANCES.items():
                generated_values = []
                for i in range(int(math.ceil(100 * value))):
                    generated_values.append(values.pop())
                self.encode_table[letter] = generated_values

                iterator = 301
                for character in self.SPECIAL_CHARACTERS:
                    self.encode_table[character] = [iterator]
                    iterator += 1

                iterator = 401
                for i in range(10):
                    self.encode_table[str(i)] = [iterator]
                    iterator += 1
            self.save_code(self.encode_table)
        else:
            self.load_code()

    def encode(self, message):
        with open('encoded_file', 'w') as file:
            for letter in message:
                file.write(self.pick_random_value(letter.lower()))

    def decode(self):
        with open('encoded_file', 'r') as encoded_file, open('decoded_file', 'wb') as decoded_file:
            chunked_file = self.chunkstring(encoded_file.read(), 3)
            for chunk in chunked_file:
                for key, value in self.encode_table.items():
                    if int(chunk) in value:
                        decoded_file.write(key.encode('utf-8'))

    def print_decoded(self):
        with open('decoded_file', 'r') as decoded_file:
            print(decoded_file.read())

    def print_encoded(self):
        with open('encoded_file', 'r') as decoded_file:
            print(decoded_file.read())

    def save_code(self, obj):
        with open(self.table_name + '.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    def load_code(self):
        with open(self.table_name + '.pkl', 'rb') as f:
            self.encode_table = pickle.load(f)
