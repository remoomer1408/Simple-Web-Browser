import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Python Browser")
        self.setGeometry(100, 100, 800, 600)
        
        # Main widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Layout
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)
        self.layout.addWidget(self.url_bar)
        
        # Web view
        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)
        
        # Load a default page
        self.browser.setUrl(QUrl("https://www.google.com"))

    def load_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
