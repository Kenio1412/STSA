# 此文件用于测试所有功能

from Analyze import Analyze
from Process import Process
from Function import *

if __name__ == '__main__':
    input_str = """
    Getty Images It is shortly after 10 a.m., and The Body—all 237 pounds of him—is in his cubicle, sifting through e-mails. I am wedged next to his liver, sifting through the metabolic remains of his morning drink: Vitaminwater. It calls itself a “nutrient enhanced” beverage, a nutritious cocktail. Ha! It is mostly sugar in a bottle, and I love it. It sneaks past the digestive system and lands in the liver, which converts it to fat and sends it straight to me. What a bonanza! 
    """
    print("原文：", input_str)

    Process = Process(input_str)
    # 凯撒密码加密
    key = 3
    output_str = Process.CaesarCipherEncrypt(key)
    print("凯撒密码加密：", output_str)

    # 获得分析结果
    analysis = Process.getAnalysis()
    print(f"一元频率：{analysis['frequency']['char']}")
    print(f"二元频率：{analysis['frequency']['bigram']}")
    print(f"三元频率：{analysis['frequency']['trigram']}")
    print(f"凯撒密码key：{analysis['caesar_key']}")
    print(f"是否是单表代换：{analysis['is_monoalphabetic']}")
    print(f"是否是单表代换（卡方检验）：{analysis['is_monoalphabetic_chi2']}")
    print(f'findChar: {analysis["findChar"]}')
    print(f'findThe: {analysis["findThe"]}')

    # 凯撒密码解密
    output_str = Process.CaesarCipherDecrypt(key)
    print("凯撒密码解密：", output_str)

    # 仿射密码加密
    key = (3, 2)
    output_str = Process.AffineCipherEncrypt(key)
    print("仿射密码加密：", output_str)

    # 代换U->g H->t
    replaced_dict = {'U': 'g', 'H': 't', 'A': 'i'}
    output_str = Process.MultipleSubstitution(replaced_dict)
    print("多表代换：", output_str)

    # 回滚
    output_str = Process.RollBack()
    print("回滚：", output_str)

    # 前进
    output_str = Process.Forward()
    print("前进：", output_str)

    # 回滚
    output_str = Process.RollBack()
    print("回滚：", output_str)

    # 仿射密码解密
    output_str = Process.AffineCipherDecrypt(key)
    print("仿射密码解密：", output_str)
