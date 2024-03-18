def _hash (key):
    my_hash = 0
    for letter in key:
        my_hash = (my_hash+ord(letter) * 23) % 7
        print("ord of letter:", ord(letter), " | individual hash value:", ord(letter) * 23 % 7, "I my_hash", my_hash)
    print("my_hash:", my_hash)

_hash("ABCDE")