import sys
import tkinter as tk
from tkinter import ttk
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView

# Hojas de estilo oficiales de justehcupcake para PS5 DualSense (Blanco y Negro)
PS5_WHITE_PARAM = "s=5&editcss=https%3A%2F%2Fjustehcupcake.github.io%2FPS5_Display_Pics%2FPS5_White.css"
PS5_BLACK_PARAM = "s=5&editcss=https%3A%2F%2Fjustehcupcake.github.io%2FPS5_Display_Pics%2FPS5_Black.css"

# Diccionario de Skins 100% verificado
SKINS = {
    "PS5 DualSense (White)": PS5_WHITE_PARAM,
    "PS5 DualSense (Black)": PS5_BLACK_PARAM,
    "PS4 DualShock 4 (White)": "s=8",
    "PS4 DualShock 4 (Black)": "s=5",
    "Xbox One / Series (Black)": "s=0",
    "Xbox One / Series (White)": "s=1",
    "Xbox 360 Controller": "s=4",
    "PS3 DualShock 3": "s=2"
}

class VentanaOverlay(QMainWindow):
    def __init__(self, skin_param, player_id, escala):
        super().__init__()
        self.setWindowTitle("CoreHUD v2.0")

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        
        ancho = int(450 * escala)
        alto = int(360 * escala)
        self.resize(ancho, alto)
        self.move(80, 80)

        self.browser = QWebEngineView(self)
        self.browser.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.browser.page().setBackgroundColor(QColor(0, 0, 0, 0))
        self.browser.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.setCentralWidget(self.browser)

        self.browser.setZoomFactor(escala * 0.5)

        url = f"https://overlay.gamepadviewer.com/?p={player_id}&{skin_param}"
        self.browser.load(QUrl(url))
        
        self._drag_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
        elif event.button() == Qt.MouseButton.RightButton:
            QApplication.quit()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self._drag_pos is not None:
            self.move(event.globalPosition().toPoint() - self._drag_pos)
            event.accept()

def abrir_launcher():
    seleccion = {"lanzar": False}

    root = tk.Tk()
    root.title("CoreHUD v2.0 - Setup")
    root.geometry("360x325")
    root.configure(bg="#18181b")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')

    tk.Label(root, text="🎮 CoreHUD v2.0", fg="#ff5500", bg="#18181b", font=("Segoe UI", 14, "bold")).pack(pady=(15, 10))

    tk.Label(root, text="Controller Skin:", fg="#e4e4e7", bg="#18181b", font=("Segoe UI", 10)).pack(anchor="w", padx=35)
    combo_skin = ttk.Combobox(root, values=list(SKINS.keys()), state="readonly", width=32, font=("Segoe UI", 10))
    combo_skin.current(0)
    combo_skin.pack(pady=(4, 10))

    tk.Label(root, text="Controller Slot (Player):", fg="#e4e4e7", bg="#18181b", font=("Segoe UI", 10)).pack(anchor="w", padx=35)
    combo_player = ttk.Combobox(root, values=["Player 1", "Player 2", "Player 3", "Player 4"], state="readonly", width=32, font=("Segoe UI", 10))
    combo_player.current(0)
    combo_player.pack(pady=(4, 10))

    tk.Label(root, text="HUD Size:", fg="#e4e4e7", bg="#18181b", font=("Segoe UI", 10)).pack(anchor="w", padx=35)
    combo_size = ttk.Combobox(root, values=["Small (75%)", "Normal (100%)", "Large (125%)"], state="readonly", width=32, font=("Segoe UI", 10))
    combo_size.current(1)
    combo_size.pack(pady=(4, 12))

    def lanzar():
        seleccion["skin_param"] = SKINS[combo_skin.get()]
        seleccion["player_id"] = combo_player.current() + 1
        escalas = [0.75, 1.0, 1.25]
        seleccion["escala"] = escalas[combo_size.current()]
        seleccion["lanzar"] = True
        root.destroy()

    tk.Button(
        root, text="LAUNCH OVERLAY", command=lanzar,
        bg="#ff5500", fg="white", font=("Segoe UI", 10, "bold"),
        relief="flat", width=25, pady=6, cursor="hand2"
    ).pack()

    tk.Label(root, text="💡 Left-Click & Drag: Move  |  Right-Click: Close", fg="#a1a1aa", bg="#18181b", font=("Segoe UI", 8)).pack(pady=(10, 0))

    root.mainloop()

    if seleccion["lanzar"]:
        app = QApplication(sys.argv)
        ventana = VentanaOverlay(seleccion["skin_param"], seleccion["player_id"], seleccion["escala"])
        ventana.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    abrir_launcher()
