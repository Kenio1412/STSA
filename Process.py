from Function import *
from Analyze import Analyze

class Process():
    def __init__(self, input_str: str):
        self.input_str = input_str
        self.process_str = input_str
        self.output_str = input_str
        # 中间步骤
        self.step = 0
        self.max_step = self.step  # 最远步骤
        # 记录中间过程
        self.intermediate = {self.step: input_str}
        # 分析
        self.analysis = Analyze(input_str)


    def __len__(self) -> int:
        """
        :return: 去除空格和换行后的长度
        """
        return len(self.run_time.replace(' ', '').replace('\n', ''))

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
        return self.output_str

    # 凯撒密码解密
    def CaesarCipherDecrypt(self, key: int) -> str:
        self.output_str = CaesarCipherDecrypt(self.output_str, key)
        self.step += 1
        self.max_step = self.step
        self.intermediate[self.step] = self.output_str
        return self.output_str

    # 仿射密码加密
    def AffineCipherEncrypt(self, key: tuple) -> str:
        self.output_str = AffineCipherEncrypt(self.output_str, key)
        self.step += 1
        self.max_step = self.step
        self.intermediate[self.step] = self.output_str
        return self.output_str

    # 仿射密码解密
    def AffineCipherDecrypt(self, key: tuple) -> str:
        self.output_str = AffineCipherDecrypt(self.output_str, key)
        self.step += 1
        self.max_step = self.step
        self.intermediate[self.step] = self.output_str
        return self.output_str

    # Playfair密码加密
    def PlayfairCipherEncrypt(self, key: str) -> str:
        self.output_str = PlayfairCipherEncrypt(self.output_str, key)
        self.step += 1
        self.max_step = self.step
        self.intermediate[self.step] = self.output_str
        return self.output_str

    # Playfair密码解密
    def PlayfairCipherDecrypt(self, key: str) -> str:
        self.output_str = PlayfairCipherDecrypt(self.output_str, key)
        self.step += 1
        self.max_step = self.step
        self.intermediate[self.step] = self.output_str
        return self.output_str

    # Atbash密码加密
    def AtbashCipherEncrypt(self) -> str:
        self.output_str = AtbashCipherEncrypt(self.output_str)
        self.step += 1
        self.max_step = self.step
        self.intermediate[self.step] = self.output_str
        return self.output_str



    # 文本多个字符代换
    def MultipleSubstitution(self, sub_dict: dict) -> str:
        self.output_str = multiple_substitution(self.output_str, sub_dict)
        self.step += 1
        self.max_step = self.step
        self.intermediate[self.step] = self.output_str
        return self.output_str

    # 操作回滚
    def Rollback(self) -> str:
        if self.step > 0:
            self.step -= 1
            self.output_str = self.intermediate[self.step]
        return self.output_str

    # 操作前进
    def Forward(self) -> str:
        if self.step < self.max_step:
            self.step += 1
            self.output_str = self.intermediate[self.step]
        return self.output_str
