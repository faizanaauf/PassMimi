# PassMimi

<p align="center">
  <img src="https://github.com/faizanaauf/PassMimi/blob/bdb1d1a829f53ee30ade6051ab4838ce584da778/16fcf2b2-a0d3-4604-89ba-a32266fec153_removalai_preview.png" alt="PassMimi Logo" width="180">
</p>

<h3 align="center">
Privacy-First Open Source Password Security Analyzer
</h3>

<p align="center">
Analyze password strength, detect leaked passwords using real-world breach datasets, and improve password security without sending your data to the cloud.
</p>

<p align="center">

![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-blue)

![Python](https://img.shields.io/badge/Python-3.10%2B-yellow)

![License](https://img.shields.io/badge/License-MIT-green)

![Status](https://img.shields.io/badge/Status-Active-success)

</p>

---

## 🔒 What is PassMimi?

PassMimi is an open-source password security analyzer designed to help individuals, developers, and organizations identify weak or compromised passwords before they are used.

Unlike traditional password strength meters that only evaluate length and character complexity, PassMimi also checks passwords against well-known password breach datasets used in real-world security research.

All password analysis runs locally on your computer. Your passwords are never uploaded or shared with external servers.

---

# ✨ Features

## ✅ Local Password Analysis

Every password is analyzed completely offline to protect user privacy.

- No cloud processing
- No account required
- No password storage
- No telemetry

---

## ✅ Breached Password Detection

PassMimi checks passwords against popular security datasets including:

- RockYou
- SecLists
- Weakpass

If a password exists in these datasets, PassMimi immediately warns the user that the password has previously appeared in known password collections.

---

## ✅ Password Strength Analysis

PassMimi evaluates multiple security factors, including:

- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Symbols
- Password structure
- Dictionary exposure

The result is an easy-to-understand security score with recommendations for improvement.

---

## ✅ Estimated Crack Time

PassMimi estimates how long an offline brute-force attack may take based on password complexity and character diversity.

This helps users better understand the practical strength of their passwords.

---

## ✅ Cross Platform

PassMimi supports:

- Windows
- Linux

The project can be executed directly from source or downloaded as a standalone executable for Windows.

---

---

# 📸 Screenshots

PassMimi features a modern desktop interface designed to provide clear, real-time password security analysis while maintaining a simple user experience.

### Home Screen

![PassMimi Home Screen](https://github.com/faizanaauf/PassMimi/blob/main/Screenshot%20(234).png)

### Password Analysis

![PassMimi Password Security Analysis](https://github.com/faizanaauf/PassMimi/blob/main/Screenshot%20(235).png)

### Password Strength Report

![PassMimi Password Report](https://github.com/faizanaauf/PassMimi/blob/main/Screenshot%20(236).png)


---

# 🚀 Installation

## Windows

1. Download the latest executable from **Releases**.
2. Run `PassMimi.exe`.
3. On first launch, PassMimi automatically downloads the required security wordlists.

No installation is required.

---

## Linux & Source Installation

```bash
git clone https://github.com/faizanaauf/PassMimi.git

cd PassMimi

pip install -r requirements.txt

python post_install.py

python app.py
```

---

# ⚡ Technology Stack

- Python
- Flask
- PyWebView
- HTML
- CSS
- JavaScript

---

# 🛡️ How PassMimi Works

PassMimi combines password policy analysis with real-world breach detection to provide a more meaningful security assessment.

When a password is entered, PassMimi:

1. Analyzes password length and complexity.
2. Checks uppercase, lowercase, numbers, and symbols.
3. Searches local breach datasets such as RockYou, SecLists, and Weakpass.
4. Estimates offline brute-force crack time.
5. Generates a security score with actionable recommendations.

Because every operation runs locally, passwords never leave your computer.

---

# 🔐 Privacy First

Privacy is a core design principle of PassMimi.

- ✅ No cloud processing
- ✅ No password uploads
- ✅ No user tracking
- ✅ No analytics
- ✅ No account required
- ✅ Works completely offline after initial setup

Your passwords remain under your control at all times.

---

# 🏗️ Project Structure

```text
PassMimi/
├── app.py
├── post_install.py
├── requirements.txt
├── static/
├── wordlists/
├── screenshots/
└── README.md
```

---

# 📊 Security Checks

PassMimi evaluates passwords using multiple security indicators.

| Check | Supported |
|---------|:---------:|
| Password Length | ✅ |
| Uppercase Letters | ✅ |
| Lowercase Letters | ✅ |
| Numbers | ✅ |
| Special Characters | ✅ |
| Breached Password Detection | ✅ |
| Password Strength Rating | ✅ |
| Crack Time Estimation | ✅ |
| Offline Analysis | ✅ |

---

# 🎯 Why Use PassMimi?

Many password strength checkers only analyze character types.

PassMimi goes a step further by detecting passwords found in widely used breach datasets, helping users avoid passwords that attackers already know.

Whether you're an individual improving your online security or a developer validating password quality, PassMimi provides fast, private, and reliable password analysis.

---

# 🗺️ Roadmap

The long-term goal of PassMimi is to become a complete open-source password security platform.

### Current Features

- Password strength analysis
- Local breach detection
- Crack time estimation
- Desktop application
- Windows support
- Linux support

### Planned Features

- Secure encrypted password manager
- Enterprise password policy auditing
- Website password validation API
- AI-powered password recommendations
- Browser extension
- Command Line Interface (CLI)
- REST API for developers
- Multi-language support
- Security reports for organizations

---

# 🤝 Contributing

Contributions are welcome from developers, security researchers, designers, and documentation writers.

You can contribute by:

- Reporting bugs
- Improving documentation
- Suggesting new features
- Optimizing performance
- Submitting pull requests

Please read the `CONTRIBUTING.md` guide before opening a pull request.

---

# 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

# ⭐ Support the Project

If PassMimi helps you improve password security, consider supporting the project by:

- ⭐ Starring the repository
- 🍴 Forking the project
- 🐞 Reporting bugs
- 💡 Suggesting new features
- 🤝 Contributing code

Every contribution helps make PassMimi better for the open-source community.

---

# 💬 Feedback

Found a bug or have an idea?

Open an issue or start a discussion in the GitHub repository.

Community feedback helps shape the future of PassMimi.
# 📬 Contact

Have a question, found a bug, or want to contribute?

📧 **Email:** fai_ebook@proton.me

You can also open an Issue or start a Discussion on GitHub.

<p align="center">

**⭐ If you find PassMimi useful, consider starring the repository to support future development.**

</p>

---

<p align="center">

Built with ❤️ for the Open Source Community.

**Secure Passwords. Private by Design. Open by Nature.**

</p>
