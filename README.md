
# 🚀 USERVERSE
**Userverse: The Infinite Username Explorer**  

This Python script scans a list of Instagram usernames to check if they are available. It's fast, multithreaded, and handles rate-limiting like a pro!  

---

## 🌟 Features  

✅ **Concurrent Requests**: Speed up the process with multithreading.  
✅ **Rate-Limit Handling**: Automatically retries when limits are detected.  
✅ **Random User-Agent**: Stay undetected with rotating user agents.  


---

## 📋 Requirements  

1. **Python**  
2. Install dependencies using:  
   ```bash
   pip install requests fake-useragent colorama
   ```

---

## 🛠️ Installation 

1. Clone or download this repository.  
2. Prepare a `usernames.txt` file with Instagram usernames, one per line:  

   Example `usernames.txt`:  
   ```plaintext
   username1
   username2
   username3
   ```

3. Run the script:  
   ```bash
   python main.py
   ```

4. **Check Console Output**:  
   The script logs statuses for usernames as available or taken.  

5. **View Results**:  
   - **Available usernames** are saved in `available.txt`.  
   - **Taken usernames** are logged in the console.  

---

## 🖥️ Example Output  

### Console Output  
```plaintext
🚀 WELCOME TO USERVERSE: The Infinite Username Explorer  

🛠️ SYSTEM DIAGNOSTICS: Pre-checking username 'instagram'  
✅ SYSTEM CHECK PASSED: Rate limits are stable  

🚀 ACTIVATING SCAN MODULE: Initiating username availability search  

================= AVAILABLE USERNAMES =================  
💡 username1  
💡 username4  

================== TAKEN USERNAMES ==================  
⛔ username2  
⛔ username3  

🛰️ MISSION COMPLETE: Username scan finalized. Results stored in 'available.txt'
```

### Output File: `available.txt`  
```plaintext
username1
username4
```

---

## 🛡️ Pre-Check  

Before scanning, the script performs a system check using the username `instagram` to detect rate limits. If rate-limiting is detected, the script will exit gracefully.

---

## ⚠️ Disclaimer  

This script is for **educational purposes only**. Use responsibly and in compliance with Instagram’s Terms of Service. The author assumes no liability for misuse.  