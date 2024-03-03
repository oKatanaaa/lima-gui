from lima_gui.controller.main_controller import Controller
from lima_gui.view.main_window import MainWindow
import threading


if __name__ == '__main__':
    threading.stack_size(131072)  # 128KiB stack
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    main_window = MainWindow()
    controller = Controller(main_window)
    main_window.show()
    sys.exit(app.exec())
