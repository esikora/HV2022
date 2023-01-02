# Hackvent 2022
#
# Solution for Challenge HV22.18: Santa's Nice List
#
# Decryption based on: https://github.com/lclevy/unarcrypto

from binascii import unhexlify
import time

from hashlib import sha1
import hmac

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util import Counter
from Crypto.Cipher import AES

import zlib


aes_key_len = 32
passwd_verif_len = 2

# Extracted data from zip archive
f_salt = unhexlify('e07f14de6a21906d6353fd5f65bcb339')

f_passwd_verif = unhexlify('5664')

f_enc_data = unhexlify(
    'e6f2437b18cd6bf346bab9beaa3051feba189a66c8d12b33e6d643c52d7362c9bb674d8626c119cb73146299db399b2f64e3edcfdaab8bc290fcfb9bcaccef695d')

f_auth_code = unhexlify('40663473539204e3cefd')


def decrypt_zip(passwd_ascii):

    # Generate keys for AES-256 as specified
    gen_keys = PBKDF2(passwd_ascii, f_salt, dkLen=aes_key_len * 2 + passwd_verif_len, count=1000)

    # Early exit: Check password verification value
    gen_passwd_verif = gen_keys[-2:]
    if gen_passwd_verif != f_passwd_verif:
        return -1

    # Check authentication code
    gen_auth_key = gen_keys[aes_key_len:aes_key_len * 2]
    gen_auth_full = hmac.new(gen_auth_key, f_enc_data, sha1).digest()
    gen_auth_code = gen_auth_full[:10]  # Only the first 10 bytes of the authentication hash value are used
    if gen_auth_code != f_auth_code:
        return -1

    # Decrypt data using the aes key derived from the password
    gen_aes_key = gen_keys[:aes_key_len]
    ctr = Counter.new(nbits=128, initial_value=1, little_endian=True)
    plaintext = AES.new(gen_aes_key, AES.MODE_CTR, counter=ctr).decrypt(f_enc_data)

    # Needed only for mode 'AES-256 Deflate'
    #plaintext = zlib.decompress(plaintext, -15)

    print(plaintext)
    print(plaintext.decode('utf-8'))

    return 0


# Main
start = time.time()

for i in range(32, 128):
    for j in range(32, 128):
        for k in range(32, 128):

            s = f'{i:02x}'+f'{j:02x}'+f'{k:02x}'
            passwd_hex_str = s + '69792b677e3e4c7a6d78545c205c4e5e26'
            passwd_ascii = unhexlify(passwd_hex_str).decode('utf-8')

            if decrypt_zip(passwd_ascii) == 0:
                print(passwd_hex_str)
                print(passwd_ascii)

                end = time.time()
                print(f'Duration: {end-start:.1f} s')

                exit(0)

print('Sorry, no matching password found.')
