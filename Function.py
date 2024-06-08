import numpy as np
import json

with open('letter_frequency.json', 'r') as f:
    data = json.load(f)
expected_freq = data['char']
expected_freq_bi = data['bigram']
expected_freq_tri = data['trigram']


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
    key_inv = invert(key[0], 26)  # 求逆元

    if key_inv is None:
        raise ValueError("The key is not invertible.")

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
    # 清除无关字符
    text_copy = text
    for ch in set(list(text_copy)):
        if not ch.isalpha():
            text = text.replace(ch, '')
    key = key.replace('J', 'I').replace(' ', '').replace('\n', '').upper()
    table = construct_playfair_table(key)
    text = text.replace('J', 'I').replace(' ', '').replace('\n', '').upper()
    if not is_alpha(text):
        raise ValueError("The text must be fully alphabetic.")

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
    key = key.replace('J', 'I').replace(' ', '').replace('\n', '').upper()

    table = construct_playfair_table(key)
    text = text.replace('J', 'I').replace(' ', '').replace('\n', '').upper()
    if not is_alpha(text):
        raise ValueError("The text must be fully alphabetic.")

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
def count_char_freq(text: str) -> dict:
    freq = {}
    for char in text:
        # 如果char不是英文字母
        if not char.isalpha():
            continue
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    # 计算频率,结果保留两位小数
    for key in freq:
        freq[key] = freq[key] / len(text.replace(' ', '')) * 100
        freq[key] = round(freq[key], 2)
    # 按照频率降序排列
    freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    return freq


# 统计双个字符频率
def count_bigram_freq(text: str) -> dict:
    freq = {}
    sum = 0
    for i in range(len(text) - 1):
        bigram = text[i:i + 2]
        # 如果bigram含有非英文字母
        if not bigram[0].isalpha() or not bigram[1].isalpha():
            continue
        sum = sum + 1
        if bigram in freq:
            freq[bigram] += 1
        else:
            freq[bigram] = 1
    # 计算频率
    for key in freq:
        freq[key] = freq[key] / sum * 100
        freq[key] = round(freq[key], 2)
    # 按照频率降序排列
    freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:min(10,len(freq))])
    return freq


# 统计三个字符频率
def count_trigram_freq(text: str) -> dict:
    freq = {}
    sum = 0
    for i in range(len(text) - 2):
        trigram = text[i:i + 3]
        # 如果trigram含有非英文字母
        if not trigram[0].isalpha() or not trigram[1].isalpha() or not trigram[2].isalpha():
            continue
        sum = sum + 1
        if trigram in freq:
            freq[trigram] += 1
        else:
            freq[trigram] = 1
    # 计算频率
    for key in freq:
        freq[key] = freq[key] / sum * 100
        freq[key] = round(freq[key], 2)
    # 按照频率降序排列
    freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:min(10,len(freq))])
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


# Coincidence index method 重合指数法
def coincidence_index(freq: dict) -> float:
    sum = 0
    for key in freq:
        sum += (freq[key] / 100) ** 2
    return sum


# Chi-square test 卡方检验
def chi2_test(freq: dict) -> float:
    chi2 = 0
    for key in freq:
        if key in expected_freq:
            chi2 += (freq[key] / 100 - expected_freq[key] / 100) ** 2 / (expected_freq[key] / 100)
    return chi2


# 利用 a-e-i 或 r-s-t 的单字符频率峰值找到两个可能的凯撒密码的key
def find_caesar_key(freq: dict) -> tuple:
    key = 0
    key_second = 0
    max_freq = 0
    max_second_freq = 0
    for i in range(26):
        if chr(i + 65).lower() in freq:
            if freq[chr(i + 65).lower()] > max_freq:
                max_second_freq = max_freq
                max_freq = freq[chr(i + 65).lower()]
                key_second = key
                key = i
            elif freq[chr(i + 65).lower()] > max_second_freq:
                max_second_freq = freq[chr(i + 65).lower()]
                key_second = i
    if (key - 4) % 26 == (key_second - 18) % 26:
        return ((key - 4) % 26,)
    else:
        return (key - 4) % 26, (key_second - 18) % 26


# 通过频率分析，从密文中找到出 t\h\e 三个字母
def find_the(char_freq: dict, bigram_freq: dict, trigram_freq: dict,range_=10) -> dict | None:
    """
    如果存在 两个高概率二元组合尾部和头部字母相同
    且 相连的三元概率也靠前
    且 高概率二元的另外两个字母的单字符概率较高，
    则可以认为 这三个是 the
    :param char_freq:
    :param bigram_freq:
    :param trigram_freq:
    :return: dict{key: str, value: str}
    """
    result = {}
    key_char = list(char_freq.keys())[:min(range_,len(char_freq))]
    key_bigram = list(bigram_freq.keys())[:min(range_,len(bigram_freq))]
    key_trigram = list(trigram_freq.keys())[:min(range_,len(trigram_freq))]
    for i in range(len(key_bigram)):
        for j in range(len(key_bigram)):
            if key_bigram[i][1] == key_bigram[j][0] and key_bigram[i][0] in key_char and key_bigram[j][1] in key_char:
                key = key_bigram[i][0] + key_bigram[i][1] + key_bigram[j][1]
                if key in key_trigram:
                    for i in range(3):
                        result[key[i]] = "the"[i]
                    return result
    return None


# 计算相对熵
def relative_entropy(freq: dict, expected_freq: dict) -> float:
    entropy = 0
    for key in freq:
        if key in expected_freq:
            entropy += freq[key] / 100 * (np.log2(freq[key] / 100) - np.log2(expected_freq[key] / 100))
    return entropy


# 从字典从返回键中含有特定字符的键值对
def find_key_with_char(sub_dict: dict, char: str, replace_char: str) -> dict:
    if replace_char is None:
        replace_char = char
    result = {}
    for key in sub_dict:
        if char in key:
            result[key.replace(char, replace_char)] = sub_dict[key]
    return result


# 比较两个字符串中的小写字母是否相同
def compare_char(text: str, text2: str) -> bool:
    if len(text) == len(text2):
        for i in range(len(text)):
            if text[i].islower() and text2[i].islower() and text[i] != text2[i]:
                return False
        return True
    return False


# 匹配两个字典中键的小写字母部分相同的键值对
def match_key_score(sub_dict: dict, sub_dict2: dict) -> float:
    result1 = {}
    result2 = {}
    for key in sub_dict:
        for key2 in sub_dict2:
            if compare_char(key, key2) and key2 not in result2.keys():
                result1[key2] = sub_dict[key]
                result2[key2] = sub_dict2[key2]
                break
    # 把两个字典中的值归一化
    sum1 = sum(result1.values())
    sum2 = sum(result2.values())
    for key in result1:
        result1[key] = result1[key] / sum1
        result2[key] = result2[key] / sum2

    return relative_entropy(result1, result2)


# 通过频率分析，从密文中找到几个可能的字母
def find_char(char_freq: dict, bigram_freq: dict, trigram_freq: dict, replaced_dict: dict) -> dict:
    """
    通过频率分析，从密文中找到几个可能的字母
    :param char_freq: 单字符频率
    :param bigram_freq: 双字符频率
    :param trigram_freq: 三字符频率
    :param replaced_dict: 替换过的字符
    :return: dict{key: str, value: str}
    """
    result = {}
    # 从char_freq中找到第一个没被替换过的字母
    target_char = ""
    for key in char_freq.keys():
        if key not in replaced_dict.values():
            target_char = key
            break
    guess_char = []
    # 从expected_freq中找到没在replaced_dict中出现过的三个字母
    for i in range(3):
        for ch in expected_freq.keys():
            if ch not in replaced_dict.values() and ch not in guess_char:
                guess_char.append(ch)
                break
    # 通过相对熵找到最可能的字母
    k_1 = 1
    k_2 = 1
    for ch in guess_char:
        sub_dict = find_key_with_char(bigram_freq, target_char, ch)
        entropy_bi = match_key_score(sub_dict, expected_freq_bi)
        sub_dict = find_key_with_char(trigram_freq, target_char, ch)
        entropy_tri = match_key_score(sub_dict, expected_freq_tri)
        result[ch] = k_1 * entropy_bi + k_2 * entropy_tri
    # result 升序排序
    result = dict(sorted(result.items(), key=lambda x: x[1]))
    # 返回 result的第一个键
    return {target_char: list(result.keys())[0]}

# 根据英文的连接特征，进一步分析字母代换可能
def find_char_by_connect(char_freq: dict, bigram_freq: dict, trigram_freq: dict, replaced: dict) -> dict:
    """
    根据英文的连接特征，进一步分析字母代换可能
    :param char_freq: 单字符频率
    :param bigram_freq: 双字符频率
    :param trigram_freq: 三字符频率
    :param replaced: 替换过的字符
    :return: dict{key: str, value: dict}
    """
    result = {'r':None,'u':None,'x':None}

    if 'e' in replaced.values():
        r = {}
        for key in trigram_freq.keys():
            if key.startswith('e') and key.endswith('e'):
                r[key[1]] = char_freq[key[1]]
        r = dict(sorted(r.items(), key=lambda x: x[1], reverse=True))
        result['r'] = r

    if 'q' in replaced.values():
        u = {}
        for key in bigram_freq.keys():
            if key.startswith('q'):
                u[key[1]] = char_freq[key[1]]
        u = dict(sorted(u.items(), key=lambda x: x[1], reverse=True))
        result['u'] = u

    if 'x' in replaced.values():
        x = {}
        for key in bigram_freq.keys():
            if key.endswith('x'):
                x[key[1]] = char_freq[key[1]]
        x = dict(sorted(x.items(), key=lambda x: x[1], reverse=True))
        result['x'] = x

    # 返回 result的第一个键
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
