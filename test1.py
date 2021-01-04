def encrypt(text, n):
    if len(text) == 0 or not text:
        return text
    if n <= 0:
        return text
    i = 0
    while i < n:
        result = "".join(text[index].lower() for index in range(1, len(text), 2))
        result2 = "".join(text[index].lower() for index in range(0, len(text), 2))
        text = result + result2
        i += 1
    encrypted_text = text
    return encrypted_text


def decrypt(encrypted_text, n):
    if len(text) == 0 or not text:
        return text
    if n <= 0:
        return text

    def my_decrypt(text_):
        middle = int(len(text_) / 2)
        first_part = text_[:middle]
        second_part = text_[middle:]

        res = ""
        pairs = zip(second_part, first_part)
        for pair in pairs:
            res += pair[0] + pair[1]
        if len(text_) & 1:
            res += second_part[-1]
        return res

    for i in range(n):
        encrypted_text = my_decrypt(encrypted_text)
    return encrypted_text


text = "1234567890ab"
n = 15
encrypted_text = encrypt(text, n)
print(encrypted_text)
print(decrypt(encrypted_text, n))

text1 = str()
stats = 0
all_tries = 100
for i in range(all_tries):
    text1 = encrypt(text, i)
    if text == decrypt(text1, i):
        stats += 1
print(stats)
print(all_tries)
