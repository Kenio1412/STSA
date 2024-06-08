from PySide6.QtWidgets import QApplication, QDialog, QTableWidgetItem
from PySide6.QtCore import Signal, Slot
import sys

from ui_windows import Ui_STAT
from ui_sub_windows import Ui_Form
from Process import Process
from Function import data


class MainWindow(QDialog, Ui_STAT):
    send_name = Signal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.process = None
        self.Caesar.clicked.connect(self.Caesar_clicked)
        self.Affine.clicked.connect(self.Affine_clicked)
        self.Playfair.clicked.connect(self.Playfair_clicked)
        self.Atbash.clicked.connect(self.Atbash_clicked)
        self.Replace.clicked.connect(self.Replace_clicked)
        self.Frequency.clicked.connect(self.Frequency_clicked)
        self.CaesarKey.clicked.connect(self.CaesarKey_click)
        self.isMonoalphabetic.clicked.connect(self.isMonoalphabetic_clicked)
        self.FindThe.clicked.connect(self.FindThe_clicked)
        self.FineChar.clicked.connect(self.FineChar_clicked)
        self.LOAD.clicked.connect(self.LOAD_clicked)
        self.RollBack.clicked.connect(self.RollBack_clicked)
        self.Forward.clicked.connect(self.Forward_clicked)
        self.Tips.clicked.connect(self.Tips_clicked)
        self.bind()

    def bind(self):
        self.SubWindow = SubWindow(self)
        self.send_name.connect(self.SubWindow.initialize)

    def LOAD_clicked(self):
        self.input_str = self.Input_text.toPlainText()
        self.process = Process(self.input_str)
        self.Output_text.setText(self.process.get_output_str())

    def Caesar_clicked(self):
        if self.process is None:
            self.LOAD_clicked()
        self.send_name.emit("Caesar")
        self.SubWindow.show()

    def CaesarProcess(self, key1, key2, way):
        self.Input_text.setText(self.process.intermediate[self.process.step])
        if way:
            result = self.process.CaesarCipherEncrypt(key2)
        else:
            result = self.process.CaesarCipherDecrypt(key2)
        self.Output_text.setText(result)
        self.History_text.append(f"Step {self.process.step}: Caesar Cipher {key2} {'Encrypt' if way else 'Decrypt'}")
        self.SubWindow.close()

    def Affine_clicked(self):
        if self.process is None:
            self.LOAD_clicked()
        self.send_name.emit("Affine")
        self.SubWindow.show()

    def AffineProcess(self, key1, key2, way):
        self.Input_text.setText(self.process.intermediate[self.process.step])
        try:
            if way:
                result = self.process.AffineCipherEncrypt((key1, key2))
            else:
                result = self.process.AffineCipherDecrypt((key1, key2))
            self.Output_text.setText(result)
            self.History_text.append(
                f"Step {self.process.step}: Affine Cipher ({key1}, {key2}) {'Encrypt' if way else 'Decrypt'}")
        except ValueError:
            self.Output_text.setText("Error: a must be coprime with 26")
            self.History_text.append(f"Step {self.process.step}: Error: a must be coprime with 26")
            return

        self.SubWindow.close()

    def Playfair_clicked(self):
        if self.process is None:
            self.LOAD_clicked()
        self.send_name.emit("Playfair")
        self.SubWindow.show()

    def PlayfairProcess(self, key, way):
        self.Input_text.setText(self.process.intermediate[self.process.step])
        if way:
            result = self.process.PlayfairCipherEncrypt(key)
        else:
            result = self.process.PlayfairCipherDecrypt(key)
        self.Output_text.setText(result)
        self.History_text.append(f"Step {self.process.step}: Playfair Cipher {key} {'Encrypt' if way else 'Decrypt'}")
        self.SubWindow.close()

    def Atbash_clicked(self):
        if self.process is None:
            self.LOAD_clicked()
        self.Input_text.setText(self.process.intermediate[self.process.step])
        result = self.process.AtbashCipherEncrypt()
        self.Output_text.setText(result)
        self.History_text.append(f"Step {self.process.step}: Atbash Cipher")
        self.SubWindow.close()

    def Replace_clicked(self):
        if self.process is None:
            self.LOAD_clicked()
        self.send_name.emit("Replace")
        self.SubWindow.show()

    def ReplaceProcess(self, sub_dict: dict):
        self.Input_text.setText(self.process.intermediate[self.process.step])
        result = self.process.MultipleSubstitution(sub_dict)
        self.Output_text.setText(result)
        self.History_text.append(f"Step {self.process.step}: Multiple Substitution {sub_dict}")
        self.SubWindow.close()

    def Frequency_clicked(self):
        """
        频率分析，输出结果
        结果包括：一元频率，二元频率，三元频率
        输出至Analysis_text
        :return:
        """
        if self.process is None:
            self.LOAD_clicked()
        result = self.process.getAnalysis()
        self.Analysis_text.setText(f"一元频率：{result['frequency']['char']}\n"
                                   f"二元频率：{result['frequency']['bigram']}\n"
                                   f"三元频率：{result['frequency']['trigram']}\n"
                                   )
        self.History_text.append(f"Step {self.process.step}: Frequency Analysis")
        self.SubWindow.close()

    def isMonoalphabetic_clicked(self):
        """
        判断是否是单表代换密码
        输出至Analysis_text
        :return:
        """
        if self.process is None:
            self.LOAD_clicked()
        result = self.process.getAnalysis()
        self.Analysis_text.setText(f"是否是单表代换：{result['is_monoalphabetic']}\n")
        self.Analysis_text.append(f"是否是单表代换（卡方检验）：{result['is_monoalphabetic_chi2']}")
        self.History_text.append(f"Step {self.process.step}: Is Monoalphabetic")
        self.SubWindow.close()

    def FindThe_clicked(self):
        """
        通过频率分析，从密文中找到出 t\h\e 三个字母
        如果存在 两个高概率二元组合尾部和头部字母相同 且 相连的三元概率也靠前 且 高概率二元的另外两个字母的单字符概率较高，则可以认为 这三个是 the
        输出至Analysis_text
        :return:
        """
        if self.process is None:
            self.LOAD_clicked()
        result = self.process.getAnalysis()
        self.Analysis_text.setText(f"findChar: {result['findThe']}")
        self.History_text.append(f"Step {self.process.step}: Find The")
        self.SubWindow.close()

    def FineChar_clicked(self):
        """
        通过频率分析，从密文中找到几个可能的字母
        输出至Analysis_text
        :return:
        """
        if self.process is None:
            self.LOAD_clicked()
        result = self.process.getAnalysis()
        self.Analysis_text.setText(f"findChar: {result['findChar']}")
        self.History_text.append(f"Step {self.process.step}: Find Char")
        self.SubWindow.close()

    def CaesarKey_click(self):
        if self.process is None:
            self.LOAD_clicked()
        result = self.process.getAnalysis()
        self.Analysis_text.setText(f"凯撒密码key：{result['caesar_key']}")
        self.History_text.append(f"Step {self.process.step}: Find Caesar Key")
        self.SubWindow.close()

    def RollBack_clicked(self):
        """
        回滚
        :return:
        """
        if self.process is None:
            self.LOAD_clicked()
        result = self.process.RollBack()
        self.Output_text.setText(result)
        self.Input_text.setText(self.process.intermediate[self.process.step - 1] if self.process.step > 0 else self.process.intermediate[0])
        self.History_text.append(f"Roll Back to Step {self.process.step}")
        self.SubWindow.close()

    def Forward_clicked(self):
        """
        前进
        :return:
        """
        if self.process is None:
            self.LOAD_clicked()
        result = self.process.Forward()
        self.Output_text.setText(result)
        self.Input_text.setText(self.process.intermediate[self.process.step - 1])
        self.History_text.append(f"Forward to Step {self.process.step}")
        self.SubWindow.close()

    def Tips_clicked(self):
        self.send_name.emit("Tips")
        self.SubWindow.show()
class SubWindow(QDialog, Ui_Form):
    send_caesar_key = Signal(int, int, bool)
    send_affine_key = Signal(int, int, bool)
    send_playfair_key = Signal(str, bool)
    send_replace_key = Signal(dict)

    def __init__(self, main_window: MainWindow):
        super(SubWindow, self).__init__()
        self.setupUi(self)
        self.MainWindow = main_window
        self.Ensure.clicked.connect(self.Ensure_clicked)
        self.Cancel.clicked.connect(self.Cancel_clicked)
        self.Encrypt.setChecked(True)
        self.Encrypt.clicked.connect(self.Encrypt_clicked)
        self.Decrypt.clicked.connect(self.Decrypt_clicked)
        self.bind()

    def bind(self):
        self.send_caesar_key.connect(self.MainWindow.CaesarProcess)
        self.send_affine_key.connect(self.MainWindow.AffineProcess)
        self.send_playfair_key.connect(self.MainWindow.PlayfairProcess)
        self.send_replace_key.connect(self.MainWindow.ReplaceProcess)

    def initialize(self, name):
        self.name = name
        if name == "Tips":
            self.Tips_text.setText("Tips")
        else:
            self.setWindowTitle(self.name + " Cipher")
        self.Tips_text.hide()
        self.From.hide()
        self.To.hide()
        self.Encrypt.hide()
        self.Decrypt.hide()
        self.label.hide()
        self.Playfair_key.hide()
        self.spinBox.hide()
        self.spinBox_2.hide()
        self.key1_name.hide()
        self.key2_name.hide()
        self.Ensure.hide()
        self.Cancel.hide()
        if name == "Caesar":
            self.label.setText("密钥key:")
            self.label.show()
            self.spinBox_2.show()
            self.spinBox_2.setEnabled(True)
            self.spinBox_2.setRange(1, 25)
            self.spinBox_2.setValue(3)
            self.key2_name.setText("key:")
            self.Encrypt.show()
            self.Decrypt.show()
            self.Ensure.show()
            self.Cancel.show()
        elif name == "Affine":
            self.label.setText("密钥key:")
            self.label.show()
            self.spinBox.setEnabled(True)
            self.spinBox.show()
            self.spinBox_2.show()
            self.spinBox_2.setEnabled(True)
            self.spinBox_2.setRange(1, 25)
            self.spinBox_2.setValue(2)
            self.spinBox.setRange(1, 25)
            self.spinBox.setValue(3)
            self.key1_name.show()
            self.key2_name.show()
            self.key1_name.setText("a:")
            self.key2_name.setText("b:")
            self.Encrypt.show()
            self.Decrypt.show()
            self.Ensure.show()
            self.Cancel.show()
        elif name == "Playfair":
            self.label.setText("密钥key:")
            self.label.show()
            self.Playfair_key.setEnabled(True)
            self.Playfair_key.show()
            self.Encrypt.show()
            self.Decrypt.show()
            self.Ensure.show()
            self.Cancel.show()
        elif name == "Replace":
            self.label.setText("替换字典:")
            self.label.show()
            self.key1_name.setText("From:")
            self.key2_name.setText("To:")
            self.key1_name.show()
            self.key2_name.show()
            self.From.setEnabled(True)
            self.From.show()
            self.To.setEnabled(True)
            self.To.show()
            self.Ensure.show()
            self.Cancel.show()
        elif name == "Tips":
            self.Tips_text.show()
            tips = f"""
            从统计意义上，英文中字母组合频率如下:
            单字母：{data['char']}
            双字母：{data['bigram']}
            三字母：{data['trigram']}
            
            **特殊字符的二元分析**
            - q后几乎百分之百连接着u
            - x前几乎总是i和e，只在极个别情况下是o和a
            - e和e之间，r的出现频率很高
            """
            self.Tips_text.setText(tips)
            self.Tips_text.show()
            self.Cancel.show()

    def Encrypt_clicked(self):
        self.Encrypt.setChecked(True)
        self.Decrypt.setChecked(False)

    def Decrypt_clicked(self):
        self.Encrypt.setChecked(False)
        self.Decrypt.setChecked(True)

    def Ensure_clicked(self):
        """
        将key1和key2传递给MainWindow
        :return:
        """
        if self.name == "Caesar":
            key1 = self.spinBox.value() if self.spinBox.isEnabled() else 0
            key2 = self.spinBox_2.value()
            way = self.Encrypt.isChecked()
            self.send_caesar_key.emit(key1, key2, way)
        elif self.name == "Affine":
            key1 = self.spinBox.value() if self.spinBox.isEnabled() else 0
            key2 = self.spinBox_2.value()
            way = self.Encrypt.isChecked()
            self.send_affine_key.emit(key1, key2, way)
        elif self.name == "Playfair":
            way = self.Encrypt.isChecked()
            self.send_playfair_key.emit(self.Playfair_key.toPlainText(), way)
        elif self.name == "Replace":
            sub_dict = {}
            from_text = self.From.toPlainText()
            to_text = self.To.toPlainText()
            for i in range(len(from_text)):
                sub_dict[from_text[i]] = to_text[i]
            self.send_replace_key.emit(sub_dict)
        self.close()

    def Cancel_clicked(self):
        self.close()
