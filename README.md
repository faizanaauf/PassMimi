<div align="center">
  <img src="https://github.com/faizanaauf/PassMimi/blob/bdb1d1a829f53ee30ade6051ab4838ce584da778/16fcf2b2-a0d3-4604-89ba-a32266fec153_removalai_preview.png" alt="PassMimi Logo" width="250"/>

  # PassMimi 🔐
</div>

## 🛡️ Defeats 90% of Standard Hacker Attacks

PassMimi ensures 90% of hackers are not able to crack your passwords. This open-source Linux and Windows tool checks major wordlists like RockYou and Seclists to rate password strength from extreme low to extreme high. It provides real-time visual feedback to help you build secure passwords, and the full source code is available right here on GitHub.

---

## ✨ Core Features

* **Advanced Strength Scoring:** Evaluates character variety, length, and structural integrity.
* **Major Breach Detection:** Cross-references your inputs against massive, real-world databases including `rockyou.txt` and `SecLists`.
* **Automated Setup:** Auto-fetches and extracts large wordlists from the cloud upon initial setup.
* **Modern GUI:** A clean, visually striking interface featuring smooth, animated feedback for a premium user experience.
* **Cross-Platform:** Runs seamlessly on both Windows and Linux environments.

---

## 📊 Security & Performance Matrix

| Metric | Rating | Detail |
| :--- | :--- | :--- |
| **Cracking Resistance** | **Extreme High** | Eliminates predictable patterns targeted by dictionary and brute-force attacks. |
| **Setup Complexity** | **Very Low** | Automated cloud-fetching handles wordlist configuration. |
| **Interface Friction** | **Very Low** | Clean, animated GUI provides instant visual feedback. |

---

## 🪟 Windows Quick Start (Pre-compiled .exe)

If you are on Windows and just want to use the software without touching any code, use the standalone executable:

1. Navigate to the **Releases** section on the right side of this GitHub page.
2. Download the latest `PassMimi.exe` file.
3. Double-click the downloaded file to run the program immediately (no installation required).
*Note: On the first launch, the software will automatically download the required wordlists in the background.*

---

## 🛠️ Setup & Installation (Open Source Code)

If you want to run the software directly from the source code on either Windows or Linux, follow these steps.

### Prerequisites
* **Windows & Linux:** Python 3.x installed (ensure Python is added to your system PATH).
* **Linux Users Only:** PyWebView requires system web dependencies to render the UI. On Debian/Ubuntu-based systems, run this first:
  ```bash
  sudo apt update
  sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-webkit2-4.0
Installation Commands
Run these commands in your terminal to clone the repository, install dependencies, and start the application:

Bash
git clone [https://github.com/faizanaauf/PassMimi.git](https://github.com/faizanaauf/PassMimi.git)
cd PassMimi
pip install -r requirements.txt
python post_install.py
python app.py
📦 Compiling to a Standalone Executable (For Developers)
PassMimi is optimized for PyInstaller. If you modify the open-source code and want to compile your own .exe, run:

Bash
pip install pyinstaller
pyinstaller --noconsole --onefile --add-data "static;static" --add-data "wordlists;wordlists" app.py
(Note: If compiling on Linux, change the semicolons ; in the --add-data flags to colons :). The final application will be generated in the dist/ folder.

## 📸 Screenshots
![image alt](https://github.com/faizanaauf/PassMimi/blob/main/Screenshot%20(234).png)

![image alt](https://github.com/faizanaauf/PassMimi/blob/main/Screenshot%20(235).png)

![image alt](https://github.com/faizanaauf/PassMimi/blob/main/Screenshot%20(236).png)
## 📬 Contact Us
Email: fai_ebook@proton.me
