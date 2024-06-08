from Function import *
from Analyze import Analyze


class Process:
    def __init__(self, input_str: str):
        self.input_str = input_str.upper()
        self.process_str = self.input_str
        self.output_str = self.input_str
        # 中间步骤
        self.step = 0
        self.max_step = self.step  # 最远步骤
        # 记录中间过程
        self.intermediate = {self.step: self.input_str}
        self.intermediate_replace = {}
        # 分析
        self.analysis = Analyze(self.input_str)
        # 已替换过的字符
        self.replaced = {}

    def __str__(self):
        return self.output_str

    def get_output_str(self):
        return self.output_str

    # 凯撒密码加密
    def CaesarCipherEncrypt(self, key: int) -> str:
        self.output_str = CaesarCipherEncrypt(self.output_str, key)
        self.step += 1
        self.max_step = self.step
        self.intermediate[self.step] = self.output_str
        self.intermediate_replace[self.step] = self.replaced
        return self.output_str.upper()

    # 凯撒密码解密
    def CaesarCipherDecrypt(self, key: int) -> str:
        self.output_str = CaesarCipherDecrypt(self.output_str, key)
        self.step += 1
        self.max_step = self.step
        self.intermediate[self.step] = self.output_str
        self.intermediate_replace[self.step] = self.replaced
        return self.output_str.lower()

    # 仿射密码加密
    def AffineCipherEncrypt(self, key: tuple) -> str:
        self.output_str = AffineCipherEncrypt(self.output_str, key)
        self.step += 1
        self.max_step = self.step
        self.intermediate[self.step] = self.output_str
        self.intermediate_replace[self.step] = self.replaced
        return self.output_str.upper()

    # 仿射密码解密
    def AffineCipherDecrypt(self, key: tuple) -> str:
        self.output_str = AffineCipherDecrypt(self.output_str, key)
        self.step += 1
        self.max_step = self.step
        self.intermediate[self.step] = self.output_str
        self.intermediate_replace[self.step] = self.replaced
        return self.output_str.lower()

    # Playfair密码加密
    def PlayfairCipherEncrypt(self, key: str) -> str:
        self.output_str = PlayfairCipherEncrypt(self.output_str, key)
        self.step += 1
        self.max_step = self.step
        self.intermediate[self.step] = self.output_str
        self.intermediate_replace[self.step] = self.replaced
        return self.output_str.upper()

    # Playfair密码解密
    def PlayfairCipherDecrypt(self, key: str) -> str:
        self.output_str = PlayfairCipherDecrypt(self.output_str, key)
        self.step += 1
        self.max_step = self.step
        self.intermediate[self.step] = self.output_str
        self.intermediate_replace[self.step] = self.replaced
        return self.output_str.lower()

    # Atbash密码加密
    def AtbashCipherEncrypt(self) -> str:
        self.output_str = AtbashCipherEncrypt(self.output_str)
        self.step += 1
        self.max_step = self.step
        self.intermediate[self.step] = self.output_str
        self.intermediate_replace[self.step] = self.replaced
        return self.output_str.upper()

    # 将替换过的字符记录下来
    def ReplaceMemory(self, sub_dict: dict) -> dict:
        key = self.replaced.keys()
        value = self.replaced.values()
        for k in sub_dict.keys():
            if k not in value and k not in key:
                self.replaced[k] = sub_dict[k]
            elif k in key:
                raise ValueError('The key has been replaced')
            else:
                idx = value.index(k)
                self.replaced[key[idx]] = sub_dict[k]
        return self.replaced

    # 文本多个字符代换
    def MultipleSubstitution(self, sub_dict: dict) -> str:

        # 将替换过的字符记录下来
        self.ReplaceMemory(sub_dict)

        self.output_str = multiple_substitution(self.output_str, sub_dict)
        self.step += 1
        self.max_step = self.step
        self.intermediate[self.step] = self.output_str
        self.intermediate_replace[self.step] = self.replaced
        return self.output_str

    # 操作回滚
    def RollBack(self) -> str:
        if self.step > 0:
            self.step -= 1
            self.output_str = self.intermediate[self.step]
            self.replaced = self.intermediate_replace[self.step] if self.step in self.intermediate_replace else {}
        return self.output_str

    # 操作前进
    def Forward(self) -> str:
        if self.step < self.max_step:
            self.step += 1
            self.output_str = self.intermediate[self.step]
            self.replaced = self.intermediate_replace[self.step]
        return self.output_str

    # 获得分析结果
    def getAnalysis(self):
        return self.analysis.updata(self.output_str, self.replaced)
