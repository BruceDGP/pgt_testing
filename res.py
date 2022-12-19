print("se ejecuto")
import codecs

token = "4f 54 6b 79 4f 54 6b 79 4e 7a 67 30 4e 54 45 34 4e 7a 55 34 4e 54 67 77 2e 47 6b 79 79 61 69 2e 54 47 53 6c 31 78 5a 5f 49 63 53 77 39 42 31 74 74 33 38 4c 2d 64 68 36 56 5f 69 76 47 2d 36 31 41 30 78 55 68 49"

token = bytes.fromhex(token)

token = str(token)[2:-1]

print(token)