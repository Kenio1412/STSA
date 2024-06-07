from Function import *


class Analyze():
    def __init__(self, input_str: str):
        self.input_str = input_str
        self.process_str = input_str
        self.output_str = input_str

        # 字频统计
        self.frequency = {}

    # 利用 a-e-i 或 r-s-t 的单字符频率峰值找到凯撒密码的key
    def findCaesarKey(self) -> tuple:
        if self.frequency is None:
            self.FrequencyAnalysis()
        result = find_caesar_key(self.frequency['char'])
        return result

    # 利用卡方检验判断密文是否为单表代换密码
    def isMonoalphabetic_chi2(self, epsilon=0.05) -> bool:
        if self.frequency is None:
            self.FrequencyAnalysis()
        result = chi2_test(self.frequency['char'])
        return result < epsilon

    # 利用重合指数法判断密文是否为单表代换密码
    def isMonoalphabetic(self, epsilon=0.005) -> bool:
        if self.frequency is None:
            self.FrequencyAnalysis()
        result = coincidence_index(self.frequency['char'])
        return abs(result - 0.065) < epsilon

    # 字频统计
    def FrequencyAnalysis(self) -> dict:
        self.frequency['char'] = count_char_freq(self.input_str)
        self.frequency['bigram'] = count_bigram_freq(self.input_str)
        self.frequency['trigram'] = count_trigram_freq(self.input_str)
        return self.frequency

    # 通过频率分析，从密文中找到出 t\h\e 三个字母
    # 如果存在 两个高概率二元组合尾部和头部字母相同 且 相连的三元概率也靠前 且 高概率二元的另外两个字母的单字符概率较高，则可以认为 这三个是 the
    def findThe(self) -> dict | None:
        if self.frequency is None:
            self.FrequencyAnalysis()
        result = find_the(self.frequency['char'], self.frequency['bigram'], self.frequency['trigram'])
        return result

    # 通过频率分析，从密文中找到几个可能的字母
    def findChar(self, replaced_dict: dict) -> dict:
        if self.frequency is None:
            self.FrequencyAnalysis()
        result = find_char(self.frequency['char'], self.frequency['bigram'], self.frequency['trigram'], replaced_dict)
        return result

    # 根据英文的连接特征，进一步分析字母代换可能
    def findCharByConnect(self, replaced: dict) -> dict:
        if self.frequency is None:
            self.FrequencyAnalysis()
        result = find_char_by_connect(self.frequency['char'], self.frequency['bigram'], self.frequency['trigram'], replaced)
        return result

    # 分析input_str
    def Analysis(self,replaced: dict) -> dict:
        result = {}
        result['frequency'] = self.FrequencyAnalysis()
        result['findThe'] = self.findThe()
        result['findChar'] = self.findChar(replaced)
        result['findCharByConnect'] = self.findCharByConnect(replaced)
        result['caesar_key'] = self.findCaesarKey()
        result['is_monoalphabetic'] = self.isMonoalphabetic()
        result['is_monoalphabetic_chi2'] = self.isMonoalphabetic_chi2()


        return result

    # 更新传入文本
    def updata(self, input_str: str, replaced: dict):
        self.input_str = input_str
        return self.Analysis(replaced)
