# Code base64 loop

import sys
import base64

file_name = str(sys.argv[1])
file_content = str(file.read(open(file_name, "r")))

def decode(encoded):
        for i in range(1,14):
                decoded = base64.b64decode(encoded)
                encoded = decoded
        print(decoded)

decode(file_content)
