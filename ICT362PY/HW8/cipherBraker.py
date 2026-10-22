########################################################
# Software Req Doc: HW8 Working with Files in Python   #
# Release Date: October 12, 2026                       #
# Coder: Alexis Barraza                                #
# Description: Automatically breaks a Caesar cipher.   #
########################################################

from cipherCounter import caesar_cipher


def main():
    """Read the contents of cipherJA.txt. and mysteryCipher.txt"""

    with open("mysteryCipher.txt", "r") as file:
        cja = file.read()

    word_list = [
        " the ",
        " and ",
        " of ",
        " to ",
        " is ",
        " in ",
        " that ",
        " was ",
        " for ",
        " this "
    ]

    for n in range(1, 25):
        decrypt_attempt = caesar_cipher(cja, n)

        check = 0

        for word in word_list:
            if word in decrypt_attempt.lower():
                check += 1

        if check > 9:
            print(f"Shift is {n}")
            print(decrypt_attempt)
            
            with open("EM.txt", "w") as output_file:
                output_file.write(decrypt_attempt)


if __name__ == "__main__":
    main()