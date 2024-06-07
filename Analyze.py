from Function import *

class Analyze():
    def __init__(self, input_str: str):
        self.input_str = input_str
        self.process_str = input_str
        self.output_str = input_str

        # 字频统计
        self.frequency = None

        # 字频统计
    def FrequencyAnalysis(self) -> dict:
        self.frequency['char'] = count_char_freq(self.input_str)
        self.frequency['bigram'] = count_bigram_freq(self.input_str)
        self.frequency['trigram'] = count_trigram_freq(self.input_str)
        return self.frequency

    # 分析input_str
    def Analysis(self) -> dict:
        result = {}
        result['frequency'] = self.FrequencyAnalysis()

        return result

    # 更新传入文本
    def updata(self, input_str: str):
        self.input_str = input_str
        return self.Analysis()
