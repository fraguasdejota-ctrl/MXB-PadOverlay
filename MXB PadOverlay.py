import sys
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView

class OverlayMando(QMainWindow):
    def __init__(self):
        super().__init__()
        # Ventana sin bordes y siempre por encima (Always on Top)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )
        # Transparencia nativa real de Windows
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.resize(450, 360)

        # Navegador integrado con fondo 100% transparente
        self.browser = QWebEngineView(self)
        self.browser.page().setBackgroundColor(QColor(0, 0, 0, 0))
        self.browser.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        # Ignorar eventos de ratón en la web para que Python controle el arrastre
        self.browser.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.setCentralWidget(self.browser)

        self.browser.loadFinished.connect(self.ajustar_mando)
        self.browser.setUrl(QUrl("https://gamepadviewer.com/?p=1&s=8"))
        self.old_pos = None

    def ajustar_mando(self):
        # Ajustamos zoom al 50% y quitamos márgenes para que el mando quede centrado
        self.browser.setZoomFactor(0.50)
        js = """
        const style = document.createElement('style');
        style.innerHTML = `
            html, body {
                background: transparent !important;
                margin: 0 !important;
                padding: 0 !important;
                overflow: hidden !important;
            }
            .container {
                margin: 0 !important;
                padding: 0 !important;
            }
        `;
        document.head.appendChild(style);
        """
        self.browser.page().runJavaScript(js)

    # Arrastrar ventana con clic izquierdo y cerrar con clic derecho
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()
        elif event.button() == Qt.MouseButton.RightButton:
            self.close()

    def mouseMoveEvent(self, event):
        if self.old_pos is not None:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.old_pos = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = OverlayMando()
    ventana.show()
    sys.exit(app.exec())