# 此文件用于测试所有功能
import matplotlib.pyplot as plt
from Analyze import Analyze
from Function import *
import time


def Test(text: str):
    input_str = text
    print("原文长度：", len(input_str))

    from Process import Process
    # 记录时间
    start_all = time.time()

    Process = Process(input_str)
    # 凯撒密码加密
    key = 3
    # start = time.time()
    output_str = Process.CaesarCipherEncrypt(key)
    # print("凯撒密码加密：", output_str)
    # end = time.time()
    # print(f"凯撒密码耗时：{end - start} s")

    # 获得分析结果
    # start = time.time()
    analysis = Process.getAnalysis()
    # end = time.time()
    # print(f"分析耗时：{end - start} s")
    # print(f"一元频率：{analysis['frequency']['char']}")
    # print(f"二元频率：{analysis['frequency']['bigram']}")
    # print(f"三元频率：{analysis['frequency']['trigram']}")
    # print(f"凯撒密码key：{analysis['caesar_key']}")
    # print(f"是否是单表代换：{analysis['is_monoalphabetic']}")
    # print(f"是否是单表代换（卡方检验）：{analysis['is_monoalphabetic_chi2']}")
    # print(f'findChar: {analysis["findChar"]}')
    # print(f'findThe: {analysis["findThe"]}')

    # 凯撒密码解密
    # start = time.time()
    output_str = Process.CaesarCipherDecrypt(key)
    # end = time.time()
    # print(f"凯撒密码解密耗时：{end - start} s")
    # print("凯撒密码解密：", output_str)

    # 仿射密码加密
    key = (3, 2)
    # start = time.time()
    output_str = Process.AffineCipherEncrypt(key)
    # end = time.time()
    # print(f"仿射密码加密耗时：{end - start} s")
    # print("仿射密码加密：", output_str)

    # 代换U->g H->t
    replaced_dict = {'U': 'g', 'H': 't', 'A': 'i'}
    # start = time.time()
    output_str = Process.MultipleSubstitution(replaced_dict)
    # end = time.time()
    # print(f"多表代换耗时：{end - start} s")
    # print("多表代换：", output_str)

    # 回滚
    # start = time.time()
    output_str = Process.RollBack()
    # end = time.time()
    # print(f"回滚耗时：{end - start} s")
    # print("回滚：", output_str)

    # 前进
    # start = time.time()
    output_str = Process.Forward()
    # end = time.time()
    # print(f"前进耗时：{end - start} s")
    # print("前进：", output_str)

    # 回滚
    # start = time.time()
    output_str = Process.RollBack()
    # end = time.time()
    # print(f"回滚耗时：{end - start} s")
    # print("回滚：", output_str)

    # 仿射密码解密
    # start = time.time()
    output_str = Process.AffineCipherDecrypt(key)
    # end = time.time()
    # print(f"仿射密码解密耗时：{end - start} s")
    # print("仿射密码解密：", output_str)

    end_all = time.time()
    print(f"总耗时：{end_all - start_all} s")
    return end_all - start_all


if __name__ == '__main__':
    input_str = """
    Getty Images It is shortly after 10 a.m., and The Body—all 237 pounds of him—is in his cubicle, sifting through e-mails. I am wedged next to his liver, sifting through the metabolic remains of his morning drink: Vitaminwater. It calls itself a “nutrient enhanced” beverage, a nutritious cocktail. Ha! It is mostly sugar in a bottle, and I love it. It sneaks past the digestive system and lands in the liver, which converts it to fat and sends it straight to me. What a bonanza! 
    """
    len_list = []
    time_list = []
    for i in range(1000):
        len_list.append(len(input_str*i))
        time_ = Test(input_str*i)
        time_list.append(time_)

    # 绘制曲线图

    plt.plot(len_list, time_list)
    plt.xlabel('Length')
    plt.ylabel('Time')
    plt.title('Length-Time')
    plt.show()
