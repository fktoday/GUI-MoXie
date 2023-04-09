import re
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QLineEdit, QRadioButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtGui import QGuiApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('默写卷生成器')
        self.setGeometry(100, 100, 500, 450)

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout(widget)

        self.label = QLabel('请输入文本:', self)
        layout.addWidget(self.label)

        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

        self.split_label = QLabel('请输入文本所有标点类型，如"，""。"（区分中英文）:', self)
        layout.addWidget(self.split_label)

        self.split_edit = QLineEdit(self)
        layout.addWidget(self.split_edit)

        self.radio_label = QLabel('请选择输出类型:', self)
        layout.addWidget(self.radio_label)

        self.radio_button_even = QRadioButton('偶数句留空', self)
        layout.addWidget(self.radio_button_even)

        self.radio_button_odd = QRadioButton('奇数句留空', self)
        layout.addWidget(self.radio_button_odd)

        self.button = QPushButton('分割', self)
        layout.addWidget(self.button)

        self.result_text_edit = QTextEdit(self)
        layout.addWidget(self.result_text_edit)

        self.copy_button = QPushButton('复制输出结果', self)
        layout.addWidget(self.copy_button)

        self.radio_button_even.setChecked(True)
        self.radio_button_even.clicked.connect(self.split_text)
        self.radio_button_odd.clicked.connect(self.split_text)
        self.button.clicked.connect(self.split_text)
        self.copy_button.clicked.connect(self.copy_result)

    def split_text(self):
        text = self.text_edit.toPlainText()
        split_symbol = self.split_edit.text()
        try:
            sentences = re.split('[' + split_symbol + ']', text)
        except:
            self.result_text_edit.setPlainText('请使用有效的分隔符')
            return
        if self.radio_button_even.isChecked():
            output_sentencese_even = sentences[0::2]  # 偶数序列元素，实是奇数句。
            output_sentences_odd = sentences[1::2]
            output_sentencese_even = [sentence.strip() for sentence in output_sentencese_even]
            # result = '____________'.join(output_sentencese_even) # 输出恒定长度横线
            list_line_even = ['____' * len(sentence) for sentence in output_sentences_odd]
            result = ''
            for i in range(len(output_sentencese_even)):
                if i < len(list_line_even):
                    result += output_sentencese_even[i] + list_line_even[i]  # 按照偶数句长度来计算横线长度并拼接到奇数句后，如果i等于list1的长度，则直接将output_sentencese_even的最后一个元素添加到result字符串中。
                else:
                    result += output_sentencese_even[i]
        else:
            output_sentencese_even = sentences[0::2]
            output_sentences_odd = sentences[1::2]
            output_sentences_odd = [sentence.strip() for sentence in output_sentences_odd]
            # result = '____________' + '____________'.join(output_sentences_odd)
            # 生成长度为偶数字符串长度的'———'列表
            list_line_odd = ['____' * len(sentence) for sentence in output_sentencese_even]
            result = ''
            for i in range(len(output_sentences_odd)):
                result += list_line_odd[i] + output_sentences_odd[i]

            # 处理最后一个偶数字符串，如果output_sentences_even的长度比output_sentences_odd多1，那么把list_line_odd最后一个元素加到result最后
            if len(output_sentencese_even) == len(output_sentences_odd) + 1:
                result += list_line_odd[-1]
        self.result_text_edit.setPlainText(result)

    def copy_result(self):
        result = self.result_text_edit.toPlainText()
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(result)
        QMessageBox.information(self, '提示', '输出结果已复制到剪贴板！')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
