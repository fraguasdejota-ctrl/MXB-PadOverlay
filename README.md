<div align="center">

  # 🏍️ MXB PadOverlay
  ### **Standalone Transparent Controller HUD for MX Bikes & Discord**

  [![Release](https://img.shields.io/badge/Version-v1.0.0-FF5500?style=for-the-badge&logo=github)](https://github.com/TU_USUARIO/MXB-PadOverlay/releases)
  [![Platform](https://img.shields.io/badge/Platform-Windows_10_%2F_11-0078D6?style=for-the-badge&logo=windows&logoColor=white)]()
  [![Python](https://img.shields.io/badge/Built_With-Python_3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
  [![Size](https://img.shields.io/badge/Lightweight-~8_MB-00C853?style=for-the-badge)]()
  [![License](https://img.shields.io/badge/License-MIT-9C27B0?style=for-the-badge)]()

  <p align="center">
    <b>Show your real-time controller inputs directly over your screen or on Discord streams without opening OBS or Streamlabs.</b>
  </p>

  <!-- Sube una captura o GIF de tu mando sobre el juego a GitHub y pega el enlace aquí abajo -->
  <img width="1873" height="1030" alt="Captura de pantalla 2026-11-13 003826" src="https://github.com/user-attachments/assets/e7091275-2a8c-4439-ad7a-606a70c8400a" />


</div>

---

## 🔥 Why MXB PadOverlay?

> [!TIP]
> **Designed specifically for the MX Bikes community:** Share your whips, scrubs, and throttle/clutch control with your friends on Discord screen-share or record raw gameplay with zero FPS drops.

* 🎯 **No OBS / Streamlabs Needed:** Runs as a native, standalone floating window on your desktop.
* ⚡ **Ultra Lightweight:** Consumes virtually **0% CPU** and minimal RAM compared to heavy streaming software.
* 👻 **100% Transparent Background:** Clean floating HUD that stays on top of your game (`Always on Top`).
* 🔌 **Plug & Play:** Single `.exe` file. No Python installation or browser tabs required.

---

## 📊 Performance Comparison

| Feature | **MXB PadOverlay** | OBS / Streamlabs Browser Source | Chrome Tab Capture |
| :--- | :---: | :---: | :---: |
| **Standalone `.exe`** | ✅ Yes | ❌ No | ❌ No |
| **True Desktop Transparency** | ✅ Yes | ⚠️ Only inside recording | ❌ Solid background |
| **Discord Screen-Share Ready** | ✅ Direct | ❌ Requires Virtual Cam / Projector | ❌ Shows browser UI |
| **RAM / CPU Impact** | 🟢 Ultra Low | 🔴 High | 🟡 Medium |

---

## 🚀 How to Download & Use (For Riders)

1. **Connect your PS4/DualShock controller** to your PC before launching the app.
2. Go to the [**Releases**](https://github.com/TU_USUARIO/MXB-PadOverlay/releases) section on the right side of this page and download `MXB_PadOverlay.zip`.
3. Extract the `.zip` and run **`MXB PadOverlay.exe`**.

> [!IMPORTANT]
> **MX Bikes Display Mode:** Make sure MX Bikes is running in **Windowed** or **Borderless Windowed** mode so the transparent overlay can float on top of the game screen.

---

## 🛡️ Antivirus & Security Check (VirusTotal)

> [!NOTE]
> Because this utility is compiled from Python into a standalone `.exe` using **PyInstaller**, Windows Defender SmartScreen may display an *"Unknown Publisher"* prompt on the first launch. Simply click **More info** $\rightarrow$ **Run anyway**.

* 🔍 **100% Open Source:** You can inspect the exact Python script right here in this repository before downloading.
* ✅ **VirusTotal Official Scan:** [**Click here to view the clean VirusTotal report**](https://www.virustotal.com/gui/file/e62fdc1332d89df8a07d2c6b5597555921d7d34c781cdc76830afc26131d7124)

---

## 🛠️ Build from Source (For Developers)

If you prefer to run the raw Python script or compile the `.exe` yourself:

```bash
# 1. Clone the repository
git clone [https://github.com/TU_USUARIO/MXB-PadOverlay.git](https://github.com/TU_USUARIO/MXB-PadOverlay.git)
cd MXB-PadOverlay

# 2. Install dependencies
pip install pywebview pyinstaller

# 3. Run the script directly
python "MXB PadOverlay.py"

# 4. Or compile into a standalone executable
pyinstaller --onefile --noconsole --clean "MXB PadOverlay.py"
