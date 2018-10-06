from os import system
import pprint
import struct

from AES.main import AESCipher
from BBS.bbs import BlumBlumShub
from homophonic.homophonic import HomophonicGenerator
from RSA.generator import RSAGenerator, PublicKey, PrivateKey
from secret_division.main import Member, Divider
from shortcut_function.main import Shortcuter


class Menu:
    def __init__(self):
        self.pp = pprint.PrettyPrinter(indent=4)

    def run_homophonic(self):
        generator = HomophonicGenerator()
        while 1:
            system('clear')
            print(
                "Homophonic generator \n"

                "1. Load code file \n"
                "2. Generate new code file \n"
                "0. Back to main menu \n"
            )
            choice = input("What is your choice? ")

            if choice == '1':
                generator.generate(generate=False)
            elif choice == '2':
                pass
            elif choice == '0':
                return

            system('clear')
            print(
                "Homophonic generator \n"

                "1. Encode file \n"
                "2. Decode file \n"
                "3. Show code table \n"
                "0. Back to main menu \n"
            )
            choice = input("What is your choice? ")

            if choice == '1':
                text = input("Enter text to encode: ")
                generator.encode(text)
                generator.print_encoded()
                input("Press any key to continue ")
            elif choice == '2':
                generator.decode()
                generator.print_decoded()
                input("Press any key to continue ")
            elif choice == '3':
                print(generator.encode_table)
                input("Press any key to continue ")
            elif choice == '0':
                return

    def run_BBS(self):
        system('clear')
        print("BBS generator \n")
        n_size = input('Enter size of the n: ')
        output_len = input('Enter lenght of the output: ')
        bbs = BlumBlumShub(n_size)
        choice = input('Chose 0 to save file as txt, 1 to save file as bytes: ')

        if choice == '0':
            with open('encoded_file_bbs', 'w') as file:
                result = bbs.generate(output_len)
                for byte in bin(result)[2:]:
                    file.write(byte)
        elif choice == '1':
            with open('encoded_file_bbs.bin', 'wb') as file:
                result = bbs.generate(output_len)
                for byte in bin(result)[2:]:
                    file.write(struct.pack('i', int(byte)))

        while 1:
            system('clear')
            print(
                "BBS generator \n"

                "1. Print p \n"
                "2. Print q \n"
                "3. print output \n"
                "0. Back to main menu \n"
            )
            choice = input("What is your choice? ")

            if choice == '1':
                print(bbs.p)
                input("Press any key to continue ")
            elif choice == '2':
                print(bbs.q)
                input("Press any key to continue ")
            elif choice == '3':
                print(bin(bbs.output))
                input("Press any key to continue ")
            elif choice == '0':
                return

    def run_RSA(self):
        encrypted_message = None
        system('clear')
        print(
            "RSA generator \n\n"

            "1. Set variables \n"
            "2. Randomize variables q \n"
            "0. Back to main menu \n"
        )
        choice = input("What is your choice? ")
        if choice == '1':
            p = int(input("Set p: "))
            q = int(input("Set q: "))
            generator = RSAGenerator(p, q)
        elif choice == '2':
            generator = RSAGenerator()
        elif choice == '0':
            return

        encryptor = PublicKey(generator.e, generator.n)
        decryptor = PrivateKey(generator.n, generator.d)
        input("Press any key to continue")
        while 1:
            system('clear')
            print(
                "RSA generator \n\n"

                "1. Encrypt message \n"
                "2. Decrypt message \n"
                "3. Show generator stats \n"
                "0. Back to previous menu \n"
            )
            choice = input("What is your choice?: ")

            if choice == '1':
                message = int(input("Type your message: "))
                encrypted_message = encryptor.encrypt(message)
                print('message successfuly encoded: \n')
                print(encrypted_message)
                input("Press any key to continue")
            elif choice == '2':
                if encrypted_message:
                    print('message decrypted: \n')
                    print(decryptor.decrypt(encrypted_message))
                    input("Press any key to continue")
            elif choice == '3':
                print('p: {} \n'.format(generator.p))
                print('q: {} \n'.format(generator.q))
                print('e: {} \n'.format(generator.e))
                print('phi: {} \n'.format(generator.phi))
                print('d: {} \n'.format(generator.d))
                input("Press any key to continue")
            elif choice == '0':
                return

    def run_AES(self):
        encrypted_message = ''
        decrypted_message = ''
        encrypted_messages = {}
        message = ''
        cbc = False
        encryptor = AESCipher('test')

        while 1:
            system('clear')
            print(
                "AES scrambler \n\n"
                "CBC mode {} \n\n".format(cbc) +
                "1. encrypt \n"
                "2. decrypt \n"
                "3. print encrypted message \n"
                "4. switch encrypt mode \n"
                "0. Back to main menu \n"
            )
            choice = input("What is your choice?: ")
            if choice == '1':
                message = input("Enter your message: ")
                encrypted_message = encryptor.encrypt(
                    str.encode(encryptor.pad(message)), cbc
                )
                if not cbc:
                    encrypted_messages['ECB'] = encrypted_message
                else:
                    encrypted_messages['CBC'] = encrypted_message

            elif choice == '2':
                decrypted_message = encryptor.decrypt(
                    encrypted_message, cbc
                )
                print(
                    encryptor.unpad(decrypted_message.decode('utf-8')) +
                    '\n'
                )
                input("Press any key to continue")
            elif choice == '3':
                self.pp.pprint(encrypted_messages)
                input("\nPress any key to continue")
            elif choice == '4':
                cbc = not cbc
            elif choice == '0':
                return

    def run_shortcut(self):
        while 1:
            system('clear')
            print(
                "Shortcut functions\n\n"
                "1. Enter message\n"
                "0. Back to main menu\n"
            )
            choice = input("What is your choice?: ")
            if choice == '1':
                message = input("Enter message: ")
                system('clear')
                shortcuter = Shortcuter(message)
                self.pp.pprint(shortcuter.to_dict())
                input("\nPress any key to continue")
            elif choice == '0':
                return

    def run_secret(self):
        while 1:
            system('clear')
            print(
                "Shortcut functions\n\n"
                "1. Enter secret\n"
                "0. Back to main menu\n"
            )
            choice = input("What is your choice?: ")
            if choice == '1':
                system('clear')
                secret = input("Enter secret: ")
                members_number = input("How many members?")
                secret_range = input("Enter range:")
                members_list = Divider.generate_members_list(
                    int(members_number)
                )
                divider = Divider(int(secret_range), int(secret))

                for member in members_list:
                    divider.members.append(member)

                divider.generate_members_values()

                for member in members_list:
                    member.value = divider.get_value_for_member(member.id)
                    divider.summary_value += member.value
                while 1:
                    system('clear')
                    print(
                        "Shortcut functions\n\n"
                        "1. Show members\n"
                        "2. Decore secret\n"
                        "0. Back to main menu\n"
                    )
                    choice = input("What is your choice?: ")

                    if choice == '1':
                        system('clear')
                        for member in members_list:
                            print("Member {} : {}".format(member.id, member.value))
                        input("\nPress any key to continue")

                    elif choice == '2':
                        print("{} % {} = {}".format(
                            divider.summary_value,
                            secret_range,
                            divider.summary_value % int(secret_range)
                        ))
                        input("\nPress any key to continue")

                    elif choice == '0':
                        return

            elif choice == '0':
                return


def main():
    menu = Menu()
    while 1:
        system('clear')
        print(
            "Crypto-app by Radek Lejba\n\n"
            "1. Homophonic\n"
            "2. BBS\n"
            "3. RSA\n"
            "4. AES\n"
            "5. Shortcut functions\n"
            "6. Secret Division\n"
            "0. Quit\n\n"
        )
        choice = input("What is your choice? ")

        if choice == '1':
            menu.run_homophonic()
        elif choice == '2':
            menu.run_BBS()
        elif choice == '3':
            menu.run_RSA()
        elif choice == '4':
            menu.run_AES()
        elif choice == '5':
            menu.run_shortcut()
        elif choice == '6':
            menu.run_secret()
        elif choice == '0':
            return


if __name__ == '__main__':
    main()
