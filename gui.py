import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QButtonGroup, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIcon
import multiprocessing
import start
import restart

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.processes = []

    def initUI(self):
        # 아이콘 설정
        if getattr(sys, 'frozen', False):
            icon_path = os.path.join(sys._MEIPASS, 'icon.png')
        else:
            icon_path = 'icon.png'
        self.setWindowIcon(QIcon(icon_path))

        # 라벨 및 입력란 생성
        labels = ["작동할 창 수", "찾는 페이지 최대", "찾기 시도 최대", "작업할 유입수", "유입수 단위"]
        self.line_edits = {}

        main_layout = QVBoxLayout()

        for label_text in labels:
            hbox = QHBoxLayout()
            label = QLabel(label_text)
            label.setFixedWidth(100)  # 라벨의 고정 너비 설정
            line_edit = QLineEdit()
            line_edit.setFixedWidth(200)  # 입력란의 고정 너비 설정
            hbox.addWidget(label)
            hbox.addWidget(line_edit)
            main_layout.addLayout(hbox)
            self.line_edits[label_text] = line_edit

        # 라디오 버튼 생성
        self.option_group = QButtonGroup(self)
        self.radio_buttons = {}
        radio_labels = ["통검", "쇼검", "통검&&쇼검", "ID"]  # "통검&쇼검"을 "통검&&쇼검"으로 수정

        radio_layout = QHBoxLayout()
        spacer_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacer_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        radio_layout.addItem(spacer_left)

        for label_text in radio_labels:
            radio_button = QRadioButton(label_text)
            self.option_group.addButton(radio_button)
            radio_layout.addWidget(radio_button)
            spacer_between = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
            radio_layout.addItem(spacer_between)  # 각 라디오 버튼 사이에 공간 추가
            self.radio_buttons[label_text] = radio_button

        radio_layout.addItem(spacer_right)
        main_layout.addLayout(radio_layout)

        # 버튼 생성
        self.start_button = QPushButton('작업 시작')
        self.reset_button = QPushButton('다시 시작')
        self.stop_button = QPushButton('작업 종료')

        self.start_button.clicked.connect(self.confirm_and_start)
        self.reset_button.clicked.connect(self.confirm_and_restart)
        self.stop_button.clicked.connect(self.confirm_and_stop)

        hbox_buttons = QHBoxLayout()
        hbox_buttons.addWidget(self.start_button)
        hbox_buttons.addWidget(self.reset_button)
        hbox_buttons.addWidget(self.stop_button)
        main_layout.addLayout(hbox_buttons)

        self.setLayout(main_layout)
        self.setWindowTitle('SPLIT')
        self.setGeometry(300, 300, 400, 300)
        self.load_values()

    def confirm_and_start(self):
        reply = QMessageBox.question(self, '작업 시작 확인',
                                     "오늘 이미 '작업 시작' 버튼을 눌렀다면, '다시 시작' 버튼을 눌러주세요.\n'작업 시작' 하시겠습니까?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.save_and_start()

    def confirm_and_restart(self):
        reply = QMessageBox.question(self, '다시 시작 확인',
                                     "작업이 진행 중이라면, '작업 종료' 먼저 진행하세요.\n'다시 시작' 전에 열린 웹을 모두 닫아주세요.\n'다시 시작' 하시겠습니까?\n",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.save_and_restart()

    def confirm_and_stop(self):
        reply = QMessageBox.question(self, '작업 종료 확인',
                                     "'작업 종료' 하시겠습니까?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.stop_all_processes()

    def save_and_start(self):
        self.save_values()
        self.run_script(start.work)

    def save_and_restart(self):
        self.save_values()
        self.run_script(restart.work)

    def save_values(self):
        values = {}
        for key, line_edit in self.line_edits.items():
            values[key] = line_edit.text()

        selected_option = None
        for label, radio_button in self.radio_buttons.items():
            if radio_button.isChecked():
                selected_option = label.replace("&&", "&")  # 저장할 때 원래 문자로 복원

        with open('settings.txt', 'w', encoding='utf-8') as f:
            for key, value in values.items():
                f.write(f"{key}:{value}\n")
            if selected_option:
                f.write(f"옵션:{selected_option}\n")

    def load_values(self):
        if os.path.exists('settings.txt'):
            with open('settings.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    key, value = line.strip().split(':')
                    if key in self.line_edits:
                        self.line_edits[key].setText(value)
                    elif key == "옵션":
                        if value in self.radio_buttons:
                            self.radio_buttons[value.replace("&", "&&")].setChecked(True)  # 불러올 때 이스케이프

    def run_script(self, target_function):
        try:
            # 입력된 값들을 인자로 전달
            args = [
                int(self.line_edits["작동할 창 수"].text()),
                int(self.line_edits["찾는 페이지 최대"].text()),
                int(self.line_edits["찾기 시도 최대"].text()),
                int(self.line_edits["작업할 유입수"].text()),
                self.line_edits["유입수 단위"].text(),
                next(label.replace("&&", "&") for label, radio_button in self.radio_buttons.items() if radio_button.isChecked())
            ]

            process = multiprocessing.Process(target=target_function, args=args)
            process.start()
            self.processes.append(process)
            QMessageBox.information(self, "작업 시작", "작업이 시작되었습니다.")
        except Exception as e:
            QMessageBox.critical(self, "오류", f"스크립트 실행 중 오류가 발생했습니다: {e}")

    def stop_all_processes(self):
        try:
            for process in self.processes:
                process.terminate()
            self.processes = []
            QMessageBox.information(self, "작업 종료", "모든 작업이 종료되었습니다.\n열린 모든 웹을 닫아주세요.")
        except Exception as e:
            QMessageBox.critical(self, "오류", f"작업 종료 중 오류가 발생했습니다: {e}")

if __name__ == '__main__':
    multiprocessing.freeze_support()  # Windows에서 멀티프로세싱을 지원하기 위해 필요
    app = QApplication(sys.argv)
    # 아이콘 경로 설정
    if getattr(sys, 'frozen', False):
        icon_path = os.path.join(sys._MEIPASS, 'icon.png')
    else:
        icon_path = 'icon.png'
    app.setWindowIcon(QIcon(icon_path))  # 애플리케이션 아이콘 설정
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())