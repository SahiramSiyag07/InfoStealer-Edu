# Information Stealer - Educational Project for Beginners

## ⚠️ IMPORTANT: Read This First!

**This project is for LEARNING ONLY!** 
- ✅ Use it to understand how hackers steal information
- ✅ Learn how to protect yourself
- ❌ NEVER use this to steal someone's data without permission
- ❌ Doing so is ILLEGAL and can get you in serious trouble

**Think of this like a medical student studying a virus to learn how to cure it, not to spread it!**

---

## 🤔 What is This Project?

This is a **learning tool** that shows you:
1. How attackers steal saved passwords from Chrome
2. How they read what's in your clipboard (copy-paste)
3. How they gather information about your computer

**Why learn this?** So you can protect yourself and your data from real hackers!

---

## 📚 What You'll Learn

### Beginner Concepts:
- How browsers store passwords (and why it's risky)
- What is encryption and why it matters
- How to keep your information safe
- Basic Python programming

### Advanced Concepts:
- Windows security systems (DPAPI)
- Database handling (SQLite)
- System information gathering
- Cybersecurity defense strategies

---

## 🚀 Getting Started (Step-by-Step)

### Step 1: Check What You Need

**You MUST have:**
- Windows computer (Windows 10 or 11)
- Python installed (version 3.7 or newer)
- Google Chrome browser (for password demo)

**Not sure if you have Python?** Open Command Prompt and type:
```bash
python --version
```
If you see a version number, you're good! If not, download Python from python.org.

### Step 2: Download This Project

1. Save all the files to a folder on your computer
2. Remember where you saved them!

### Step 3: Install Required Tools

Open Command Prompt or PowerShell in your project folder and type:

```bash
pip install -r requirements.txt
```

**What this does:** It downloads special Python tools we need:
- `pyperclip` - Reads your clipboard
- `requests` - Gets your public IP address
- `psutil` - Gathers system information
- `pycryptodome` - Handles encryption (advanced)

**Wait for it to finish!** You'll see progress bars and "Successfully installed" messages.

### Step 4: Run the Program

Type this command:
```bash
python info_stealer.py
```

**What you'll see:**
1. A big warning message (remember, this is for learning!)
2. Information about your computer
3. What's currently in your clipboard
4. Security tips to protect yourself

---

## 🎯 What Does Each Part Do?

### 1. Chrome Password Extraction
**What it does:** Tries to read saved passwords from Chrome

**How it works:**
- Chrome stores passwords in a database on your computer
- These passwords are "locked" with Windows encryption
- This script shows how hackers can "unlock" and read them

**Why this matters:** You'll see why using Chrome to save passwords is risky!

**Note:** If you don't have Chrome or saved passwords, this part will show "not found"

### 2. Clipboard Capture
**What it does:** Reads whatever you recently copied

**How it works:**
- When you copy something (Ctrl+C), it goes to clipboard
- This script can read that clipboard
- Hackers use this to steal passwords you copy-paste!

**Try this:** Copy some text, then run the script. You'll see it captured what you copied!

### 3. System Information
**What it does:** Gathers info about your computer

**What it collects:**
- Your Windows version
- Your computer name
- Your IP addresses (where you are on the internet)
- Your processor (CPU)
- How many CPU cores you have

**Why hackers want this:** It helps them plan attacks specific to your system

---

## 🛡️ How to Protect Yourself

### Immediate Actions:

#### 1. Stop Using Browser Password Savers!
**Why:** Browsers are easy targets for hackers

**Better options:**
- **Bitwarden** (Free, open source) - bitwarden.com
- **1Password** (Paid, very user-friendly)
- **KeePass** (Free, stores passwords offline)

**These are safer because:**
- They use stronger encryption
- They don't store passwords where browsers can be hacked
- They have features like password generators

#### 2. Clear Your Clipboard
**After copying passwords:**
- Copy something else (like a word) to overwrite it
- Or restart your computer
- Some password managers clear clipboard automatically

#### 3. Use Two-Factor Authentication (2FA)
**What is it:** Even if someone steals your password, they need a second code (usually from your phone)

**Where to enable it:**
- Email accounts (Gmail, Outlook)
- Banking apps
- Social media (Facebook, Instagram, Twitter)
- Any important account!

#### 4. Keep Everything Updated
- Windows updates (they fix security holes)
- Browser updates
- Antivirus software

---

## 🔍 Understanding the Code (For Beginners)

### Main Parts of the Script:

#### Part 1: Getting Chrome's Secret Key
```python
def get_chrome_encryption_key():
    # Reads a special file Chrome uses
    # This file has the "key" to unlock passwords
```

**Think of it like:** Finding the key to a locked box

#### Part 2: Unlocking Passwords
```python
def decrypt_with_dpapi(encrypted_data):
    # Uses Windows built-in unlock system
    # Only works if you're the computer owner
```

**Think of it like:** Using Windows' own security system to unlock the data

#### Part 3: Reading the Database
```python
def extract_chrome_passwords():
    # Opens Chrome's password file (it's a SQLite database)
    # Reads website URLs, usernames, and passwords
```

**Think of it like:** Opening a filing cabinet and reading the files

#### Part 4: Clipboard Reading
```python
def capture_clipboard():
    # Asks Windows "what's in the clipboard?"
    # Windows tells us the copied text
```

**Think of it like:** Asking someone "what did you just copy?"

#### Part 5: System Info
```python
def gather_system_info():
    # Asks Windows about itself
    # Gets version, name, network info, etc.
```

**Think of it like:** Looking at your computer's "about" page

---

## 🎓 Learning Path

### For Complete Beginners:
1. **Run the script** - See what it does
2. **Read the output** - Understand what information is exposed
3. **Try the defenses** - Install a password manager, enable 2FA
4. **Read DEFENSE_GUIDE.md** - Learn more protection methods

### For Intermediate Learners:
1. **Study the code** - Read through info_stealer.py
2. **Understand Windows API** - Learn how ctypes works
3. **Explore SQLite** - Learn about databases
4. **Try modifications** - Add new features (safely!)

### For Advanced Learners:
1. **Analyze encryption** - Study DPAPI in depth
2. **Build detection tools** - Create scripts to find malware
3. **Research defenses** - Learn enterprise security
4. **Contribute improvements** - Help make this better

---

## ❓ Frequently Asked Questions

### Q: Is this illegal?
**A:** No, if you use it correctly:
- ✅ On your own computer = LEGAL
- ✅ For learning = LEGAL
- ❌ On someone else's computer without permission = ILLEGAL
- ❌ To steal data = ILLEGAL

### Q: Will this harm my computer?
**A:** No! It only READS information, it doesn't:
- Delete files
- Install viruses
- Change settings
- Send data anywhere (unless you modify it)

### Q: Can I get in trouble for using this?
**A:** Only if you use it maliciously. Think of it like a kitchen knife:
- ✅ Using it to cook = Fine
- ❌ Using it to hurt someone = Crime

### Q: Why would I want to learn this?
**A:** Many reasons:
- Become a cybersecurity professional
- Protect yourself from real hackers
- Understand how technology works
- Prepare for a career in IT security

### Q: Do I need to be a programmer?
**A:** No! This guide explains everything. Basic computer knowledge is enough.

### Q: What if I don't understand something?
**A:** That's normal! Try:
- Reading the code comments
- Looking up terms you don't know
- Asking in online forums
- Taking a basic Python course first

---

## 🛠️ Troubleshooting

### Problem: "Python is not recognized"
**Solution:** 
1. Python isn't installed or not in PATH
2. Download from python.org
3. During install, check "Add Python to PATH"

### Problem: "pip is not recognized"
**Solution:**
1. Try: `python -m pip install -r requirements.txt`
2. Or reinstall Python with pip option checked

### Problem: "Chrome Login Data not found"
**Solution:**
1. You don't have Chrome installed, OR
2. Chrome isn't in the default location, OR
3. You need to close Chrome first (it locks the file)
4. This is normal if you don't use Chrome!

### Problem: Script shows errors
**Solution:**
1. Make sure you're on Windows (required for some features)
2. Check all dependencies installed correctly
3. Try running as Administrator (for some system info)
4. Read the error message - it usually tells you what's wrong

---

## 📖 Additional Resources

### Free Learning Platforms:
- **Codecademy** - Learn Python basics
- **Cybrary** - Free cybersecurity courses
- **TryHackMe** - Hands-on security practice
- **Khan Academy** - Computer science fundamentals

### YouTube Channels:
- **NetworkChuck** - Cybersecurity for beginners
- **David Bombal** - Ethical hacking tutorials
- **The Cyber Mentor** - Practical security guides

### Books (Free/Paid):
- "The Web Application Hacker's Handbook"
- "Hacking: The Art of Exploitation"
- "Metasploit: The Penetration Tester's Guide"

### Practice Sites:
- **Hack The Box** - Practice hacking legally
- **OverTheWire** - Security challenges
- **PicoCTF** - Beginner-friendly CTF

---

## 🎯 Quick Start Checklist

Before you start:
- [ ] I'm on Windows 10 or 11
- [ ] Python 3.7+ is installed
- [ ] I understand this is for EDUCATION only
- [ ] I won't use this on others without permission
- [ ] I'm ready to learn about cybersecurity!

Getting started:
- [ ] Downloaded all project files
- [ ] Installed dependencies with pip
- [ ] Ran the script successfully
- [ ] Read and understood the output
- [ ] Read the security recommendations

Next steps:
- [ ] Install a password manager
- [ ] Enable 2FA on important accounts
- [ ] Read the DEFENSE_GUIDE.md
- [ ] Learn more about cybersecurity
- [ ] Share knowledge (responsibly!)

---

## 🤝 How to Contribute

Found a bug? Have a suggestion?
- This is an educational project
- Improvements that help learning are welcome
- Focus on educational value, not malicious features

---

## 📞 Need Help?

**Common issues:**
- Check the Troubleshooting section above
- Read the code comments - they're detailed
- Search online for specific error messages

**Remember:** Learning takes time. Don't get discouraged if you don't understand everything at first!

---

## ⚖️ Final Reminder

**With knowledge comes responsibility.**

This tool shows you how the "bad guys" work so you can:
- Protect yourself
- Help others stay safe
- Maybe even become a cybersecurity professional

**Never use this knowledge to hurt others.**

---

## 🎉 You're Ready!

Go ahead and run:
```bash
python info_stealer.py
```

**Learn, explore, and stay curious - but always stay ethical!** 🔐

---

*Created for educational purposes. Stay safe online!*
