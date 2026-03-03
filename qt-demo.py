import sys
# Use PySide6 bindings (official Qt for Python)
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import Qt

def main():
    # You need one (and only one) QApplication instance per application.
    app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    window = QWidget()
    window.setWindowTitle("Wayland Qt App")
    window.setGeometry(100, 100, 400, 200) # x, y, width, height

    # Add a label to the window
    label = QLabel("Hello, Wayland!", parent=window)
    label.setAlignment(Qt.AlignCenter)
    label.setGeometry(0, 0, 400, 200) # Align label in center of window

    # Windows are hidden by default.
    window.show()

    # Start the event loop. Your application won't reach here until you exit.
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
