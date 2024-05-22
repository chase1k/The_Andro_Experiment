#!/usr/bin/env python3

import requests
import hashlib

def main():
    headers = {'User-Agent': 'okhttp'}
    seed = b'SEED:\x01\x01\x02\x03'

    # URL0 = 'http://127.0.0.1:5000/ping'
    URL0 = 'http://the-andro-experiment.ctf.ritsec.club:5000/ping'
    response = requests.post(url=URL0, data=seed, headers=headers)

    # URL1='http://127.0.0.1:5000/experiment?command=' + command
    URL1='http://127.0.0.1:5000/experiment?command=cat flag.txt'
    payload = hashlib.sha256(b'\x01\x01\x02\x03').digest()

    response = requests.post(url=URL1, data=payload, headers=headers)
    # print(response.text)

    if "RS{" in response.text:
        print("Healtch check passed.")
        exit(0)
    else:
        print("Healtch check failed.")
        exit(1)

if __name__ == "__main__":
    main()
