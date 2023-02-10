def feistel(plaintext, key, rounds):
    def split(word):
        return [char for char in word]
    def xor(a, b):
        return ''.join([chr(ord(x)^ord(y))for (x, y) in zip(a,b)])
    def f_function(block, key):
        return xor(block, key)
    def encrypt_block(plaintext_block,key, rounds):
        L = plaintext_block[:len(plaintext_block)//2]
        R = plaintext_block[len(plaintext_block)//2:]
        for i in range(rounds):
            L, R = R, xor(L, f_function(R, key))
        return L + R
    def encrypt(plaintext, key, rounds):
        plaintext = split(plaintext)
        while len(plaintext)%2 != 0:
            plaintext.append('\0')
        plaintext = ''.join(plaintext)
        encrypted = [encrypt_block(plaintext[i:i+2], key, rounds) for i in range(0, len(plaintext), 2)]
        return ''.join(encrypted)
    return encrypt(plaintext, key, rounds)
#Calling the algorithm
print(feistel('Bonjour', 'Heyo100', 80000))