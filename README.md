<div align="center">

  # 🏍️ MXB PadOverlay v2.0
  ### **Standalone Transparent Controller HUD for PC Gaming, Simulators & Discord**

  [![Release](https://img.shields.io/badge/Version-v2.0.0-FF5500?style=for-the-badge&logo=github)](https://github.com/TU_USUARIO/MXB-PadOverlay/releases)
  [![Platform](https://img.shields.io/badge/Platform-Windows_10_%2F_11-0078D6?style=for-the-badge&logo=windows&logoColor=white)]()
  [![Python](https://img.shields.io/badge/Built_With-Python_3.12_%2F_PyQt6-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
  [![License](https://img.shields.io/badge/License-MIT-9C27B0?style=for-the-badge)]()

  <p align="center">
    <b>Show your real-time controller inputs directly over any PC game, simulator, or Discord screen-share without opening OBS or Streamlabs.</b>
  </p>

  <img width="1873" height="1030" alt="MXB PadOverlay v2.0 Preview" src="https://github.com/user-attachments/assets/e7091275-2a8c-4439-ad7a-606a70c8400a" />

</div>

---

### 💡 100% Free & Open Source
**MXB PadOverlay is and always will be completely free.** 
No paywalls, no subscriptions, and no locked features. Nobody should ever have to pay or subscribe for simple utility tools like a controller overlay. The full source code is publicly available here on GitHub for complete transparency—inspect it, modify it, or build upon it freely.

---

## 🔥 Why MXB PadOverlay?

> [!TIP]
> **Universal PC Compatibility:** Designed for MX Bikes, racing simulators, and any PC game. Share your inputs, whips, scrubs, and throttle/brake control with your friends on Discord screen-share or record raw gameplay seamlessly.

- 🎯 **No OBS / Streamlabs Needed:** Runs as a native, standalone floating window on your desktop.
- ⚡ **Optimized Performance:** While it is no longer an ultra-lightweight 8MB script (due to the embedded web engine required for high-definition vector skins), it remains extremely efficient and consumes far fewer resources than running browser sources or heavy streaming suites.
- 👻 **100% Transparent Background:** Clean floating HUD that stays on top of your game (`Always on Top`).
- 🔌 **Plug & Play:** Single `.exe` file with an intuitive configuration launcher. No browser tabs required.

---

## 🚀 What's New in v2.0
- **Official PS5 DualSense Skins:** Added clean, high-definition vector designs for **DualSense White** and **DualSense Black** themes.
- **Expanded Controller Support:** Full native skins for:
  - PS5 DualSense (White & Black)
  - PS4 DualShock 4 (White & Black)
  - Xbox One / Series X|S (White & Black)
  - Xbox 360 Controller
  - PS3 DualShock 3
- **Player Slot Selection:** Dedicated launcher dropdown to easily select between Player 1, 2, 3, or 4.
- **HUD Scaling:** Adjustable sizing options (*Small 75%*, *Normal 100%*, *Large 125%*).

---

## 📊 Performance Comparison

| Feature | **MXB PadOverlay** | OBS / Streamlabs Browser Source | Chrome Tab Capture |
| :--- | :---: | :---: | :---: |
| **Standalone `.exe`** | ✅ Yes | ❌ No | ❌ No |
| **True Desktop Transparency** | ✅ Yes | ⚠️ Only inside recording | ❌ Solid background |
| **Discord Screen-Share Ready** | ✅ Direct | ❌ Requires Virtual Cam / Projector | ❌ Shows browser UI |
| **System Resource Impact** | 🟢 Low / Moderate | 🔴 High | 🟡 Medium |

---

## 🚀 How to Download & Use

1. Go to the [**Releases**](https://github.com/TU_USUARIO/MXB-PadOverlay/releases) section and download `MXB_PadOverlay_v2.exe`.
2. Connect your controller to your PC before launching the app.
3. Run the executable to open the configuration launcher.
4. Select your preferred controller skin, player slot, and HUD size, then click **LAUNCH OVERLAY**.

> [!IMPORTANT]
> **Game Display Mode:** Make sure your game is running in **Windowed** or **Borderless Windowed** mode so the transparent overlay can float on top of the screen.

---

## 🎮 Controls & Shortcuts
- **Move Overlay:** Left-click and drag anywhere on the controller window.
- **Close Overlay:** Right-click directly on the controller window to shut it down instantly.

---

## 🛡️ Antivirus & Security Check

> [!NOTE]
> Because this utility is compiled from Python into a standalone `.exe` using **PyInstaller**, Windows Defender SmartScreen may display an *"Unknown Publisher"* prompt on the first launch. Simply click **More info** $\rightarrow$ **Run anyway**.

- 🔍 **100% Open Source:** You can inspect the exact Python code right here in this repository before downloading.

---

## 🛠️ Build from Source (For Developers)

If you prefer to run the raw Python script or compile the `.exe` yourself:

```bash
# 1. Clone the repository
git clone [https://github.com/TU_USUARIO/MXB-PadOverlay.git](https://github.com/TU_USUARIO/MXB-PadOverlay.git)
cd MXB-PadOverlay

# 2. Install dependencies
pip install PyQt6 PyQt6-WebEngine

# 3. Run the script directly
python "MXB_PadOverlay_v2.py"

# 4. Or compile into a standalone executable
pyinstaller --onefile --noconsole --clean "MXB_PadOverlay_v2.py"
