
**Userverse: The Infinite Username Explorer**  

This Python script scans a list of Instagram usernames to check if they are available. It's fast, multithreaded, and handles rate-limiting like a pro!  

---

## 🌟 Features  

✅ **Concurrent Requests**: Speed up the process with multithreading.  
✅ **Rate-Limit Handling**: Automatically retries when limits are detected.  
✅ **Random User-Agent**: Stay undetected with rotating user agents.  

---

<details>
<summary><b>🛠️ Installation (click to expand)</b></summary>
   
1. **Install dependencies**
   ```bash
   pip install requests fake-useragent colorama
   ```

2. **Clone or download this repository**  
   ```bash
   git clone https://github.com/yourusername/userverse.git
   cd userverse
   ```

3. **Add the usernames you want to check for availability to the usernames.txt**
   ```plaintext
   username1
   username2
   username3
   ```

4. **Run the script**  
   ```bash
   python main.py
   ```
</details>

---


## Console Output  
```plaintext
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
---

## ⚠️ Disclaimer  

Use responsibly and in compliance with Instagram’s Terms of Service.
