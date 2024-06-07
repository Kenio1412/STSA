# Simple Substitution Cipher
def SimpleSubstitutionCipherEncrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():
            result += key[ord(char) - 65].upper()
        elif char.islower():
            result += key[ord(char) - 97].lower()
        else:
            result += char
    return result


# Simple Substitution Cipher
def SimpleSubstitutionCipherDecrypt(text, key):
    return SimpleSubstitutionCipherEncrypt(text, key)  # 解密和加密是一样的


# Atbash密码加密
def AtbashCipherEncrypt(text):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(90 - (ord(char) - 65))
        elif char.islower():
            result += chr(122 - (ord(char) - 97))
        else:
            result += char
    return result


# Atbash密码解密
def AtbashCipherDecrypt(text):
    return AtbashCipherEncrypt(text)  # Atbash密码是自反的


# 模n乘法逆元
def invert(a, n):
    a = a % n
    for i in range(1, n):
        if (a * i) % n == 1:
            return i
    return None


# 仿射密码加密
def AffineCipherEncrypt(text, key):
    # try:
    #     assert key[0] in [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25] #解的唯一性
    # except:
    #     return "error!"
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr(((ord(char) - 65) * key[0] + key[1]) % 26 + 65)
        elif char.islower():
            result += chr(((ord(char) - 97) * key[0] + key[1]) % 26 + 97)
        else:
            result += char
    return result


# 仿射密码解密
def AffineCipherDecrypt(text, key):
    key_inv = invert(key[0], 26)  # 求逆元

    if key_inv is None:
        raise ValueError("The key is not invertible.")

    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr(((ord(char) - 65 - key[1]) * key_inv % 26) + 65)
        elif char.islower():
            result += chr(((ord(char) - 97 - key[1]) * key_inv % 26) + 97)
        else:
            result += char
    return result


# 凯撒密码加密
def CaesarCipherEncrypt(text, key=3):
    result = AffineCipherEncrypt(text, (1, key))  # 凯撒密码是仿射密码的特例
    return result


# 凯撒密码解密
def CaesarCipherDecrypt(text, key=3):
    result = AffineCipherDecrypt(text, (1, key))  # 凯撒密码是仿射密码的特例
    return result


# 判断一个字符串是否只有字母
def is_alpha(text):
    for char in text:
        if not char.isalpha():
            return False
    return True


# 构造Playfair密码表
def construct_playfair_table(key: str):
    key_copy = key.replace(' ', '').replace('\n', '').upper()
    if not is_alpha(key_copy):
        raise ValueError("The key must be alphabetic.")
    key_copy = set(list(key_copy.replace('J', 'I')))
    key_copy = "".join(key_copy)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for ch in alphabet:
        if ch not in key_copy:
            key_copy += ch

    return key_copy


# 返回一个字符在table中的位置
def find_in_table(ch, table: str):
    idx = table.find(ch)
    row, col = idx // 5, idx % 5
    return row, col


# 得到table中一个特定字符
def get_in_table(idx: tuple, table: str):
    return table[idx[0] * 5 + idx[1]]


# Playfair密码加密
def PlayfairCipherEncrypt(text, key: str):
    table = construct_playfair_table(key)
    text = text.replace('J', 'I').replace(' ', '').replace('\n', '').upper()
    if not is_alpha(text):
        raise ValueError("The text must be alphabetic.")

    # 在重复字母间插入X
    i = 0
    while i < len(text) - 1:
        if text[i] == text[i + 1]:
            text = text[:i + 1] + 'X' + text[i + 1:]
        i += 2

    # 如果长度为奇数，在末尾加X
    if len(text) % 2 == 1:
        text += 'X'

    # 根据table进行加密
    result = ""
    for i in range(0, len(text), 2):
        ch_f = text[i]
        ch_s = text[i + 1]
        row_f, col_f = find_in_table(ch_f, table)
        row_s, col_s = find_in_table(ch_s, table)
        if row_s == row_f:  # 处于同一行时
            col_f_right_shift = (col_f + 1) % 5
            result += get_in_table((row_f, col_f_right_shift), table)
            col_s_right_shift = (col_s + 1) % 5
            result += get_in_table((row_s, col_s_right_shift), table)
        elif col_f == col_s:  # 处于同一列时
            row_f_down_shift = (row_f + 1) % 5
            result += get_in_table((row_f_down_shift, col_f), table)
            row_s_down_shift = (row_s + 1) % 5
            result += get_in_table((row_s_down_shift, col_s), table)
        else:  # 利用同行异列字符替代
            result += get_in_table((row_f, col_s), table)
            result += get_in_table((row_s, col_f), table)

    return result


# Playfair密码解密
def PlayfairCipherDecrypt(text, key: str):
    table = construct_playfair_table(key)
    text = text.replace('J', 'I').replace(' ', '').replace('\n', '').upper()
    if not is_alpha(text):
        raise ValueError("The text must be alphabetic.")

    # 根据table进行解密
    result = ""
    for i in range(0, len(text), 2):
        ch_f = text[i]
        ch_s = text[i + 1]
        row_f, col_f = find_in_table(ch_f, table)
        row_s, col_s = find_in_table(ch_s, table)
        if row_s == row_f:  # 处于同一行时
            col_f_left_shift = (col_f - 1) % 5
            result += get_in_table((row_f, col_f_left_shift), table)
            col_s_left_shift = (col_s - 1) % 5
            result += get_in_table((row_s, col_s_left_shift), table)
        elif col_f == col_s:  # 处于同一列时
            row_f_up_shift = (row_f - 1) % 5
            result += get_in_table((row_f_up_shift, col_f), table)
            row_s_up_shift = (row_s - 1) % 5
            result += get_in_table((row_s_up_shift, col_s), table)
        else:  # 利用同行异列字符替代
            result += get_in_table((row_f, col_s), table)
            result += get_in_table((row_s, col_f), table)

    return result.lower()


# 统计单个字符频率
def count_char_freq(text) -> dict:
    freq = {}
    for char in text:
        if char == " ":  # 忽略空格
            continue
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    return freq


# 统计双个字符频率
def count_bigram_freq(text) -> dict:
    freq = {}
    for i in range(len(text) - 1):
        bigram = text[i:i + 2]
        if " " in bigram:  # 忽略空格
            continue
        if bigram in freq:
            freq[bigram] += 1
        else:
            freq[bigram] = 1

    freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    return freq


# 统计三个字符频率
def count_trigram_freq(text) -> dict:
    freq = {}
    for i in range(len(text) - 2):
        trigram = text[i:i + 3]
        if " " in trigram:  # 忽略空格
            continue
        if trigram in freq:
            freq[trigram] += 1
        else:
            freq[trigram] = 1

    freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    return freq


# 文本多个字符代换
def multiple_substitution(text, sub_dict):
    result = ""
    for char in text:
        if char in sub_dict:
            result += sub_dict[char]
        else:
            result += char
    return result


if __name__ == "__main__":
    test = "Congratulations, your example passed the test!"
    test_rot3 = "Frqjudwxodwlrqv, brxu hadpsoh sdvvhg wkh whvw!"

    # 测试凯撒密码加解密
    assert CaesarCipherEncrypt(test) == test_rot3
    assert CaesarCipherDecrypt(test_rot3) == test

    # 测试仿射密码
    key = (7, 10)
    assert AffineCipherEncrypt(test, key) == "Yexazknujknoexg, weuz mpkqljm lkggmf nhm nmgn!"
    assert AffineCipherDecrypt("Yexazknujknoexg, weuz mpkqljm lkggmf nhm nmgn!", key) == test
    assert AffineCipherDecrypt(AffineCipherEncrypt(test, key), key) == test

    # 测试频率统计
    text = "hello world"
    freq = count_char_freq(text)
    assert freq == {'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1}
    freq = count_bigram_freq(text)
    assert freq == {'he': 1, 'el': 1, 'll': 1, 'lo': 1, 'wo': 1, 'or': 1, 'rl': 1, 'ld': 1}
    freq = count_trigram_freq(text)
    assert freq == {'hel': 1, 'ell': 1, 'llo': 1, 'wor': 1, 'orl': 1, 'rld': 1}

    # 测试Playfair密码
    key = "playfair example"
    text = "Hide the gold in the tre stump"  # 为了避免出现x 这里把tree改为 tre
    cipher_text = PlayfairCipherEncrypt(text, key)
    assert PlayfairCipherDecrypt(cipher_text, key) == text.lower().replace(' ', '')

    print("All tests passed!")
