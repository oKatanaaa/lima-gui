from lima_gui.controller.main_controller import Controller
from lima_gui.view.main_window import MainWindow
import threading


def main():
    # Otherwise the app crashes with a mysterios segmentation fault
    threading.stack_size(262144)  # 256KiB stack
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    main_window = MainWindow()
    controller = Controller(main_window)
    main_window.show()
    sys.exit(app.exec())
