import requests
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init
from fake_useragent import UserAgent

init(autoreset=True)

try:
    with open("usernames.txt", "r") as f:
        usernames = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    print(f"{Fore.RED}⚠️ ERROR: File 'usernames.txt' not found. Please ensure it exists.")
    exit(1)

INSTAGRAM_URL = "https://www.instagram.com/{}/"
MAX_THREADS = 10 

ua = UserAgent()

def display_ascii_art():
    print(f"""
    {Fore.CYAN}
    🚀 WELCOME TO USERVERSE: The Infinite Username Explorer
    {Style.RESET_ALL}
    """)

# Check username availability
def check_username(username):
    url = INSTAGRAM_URL.format(username)
    headers = {"User-Agent": ua.random}  # Generate a random User-Agent

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            if '<meta property="og:title"' in response.text or '<meta property="og:description"' in response.text:
                return False
            else:
                return True
        elif response.status_code == 429:
            print(f"{Fore.YELLOW}⚠️ RATE LIMIT DETECTED: Retrying after a delay...")
            time.sleep(random.uniform(5, 10))
            return check_username(username)
        else:
            print(f"{Fore.RED}⚠️ UNEXPECTED STATUS CODE: {response.status_code} for {username}")
            return False
    except Exception as e:
        print(f"{Fore.RED}⚠️ SYSTEM ERROR: Exception for {username}: {e}")
        return False

def save_available_username(username):
    with open("available.txt", "a") as f:
        f.write(username + "\n")

# Pre-check
def precheck_instagram():
    print(f"{Fore.YELLOW}🛠️ SYSTEM DIAGNOSTICS: Pre-checking username 'instagram'")
    if check_username("instagram"):
        print(f"{Fore.RED}🚨 WARNING: Rate limit detected! 'instagram' appears available. SHUTTING SYSTEM DOWN...")
        exit(1)
    else:
        print(f"{Fore.GREEN}✅ SYSTEM CHECK PASSED: Rate limits are stable")

def main():
    display_ascii_art()
    precheck_instagram()
    print(f"{Fore.CYAN}🚀 ACTIVATING SCAN MODULE: Initiating username availability search")
    
    available_usernames = []
    taken_usernames = []

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = {executor.submit(check_username, username): username for username in usernames}
        for future in as_completed(futures):
            username = futures[future]
            try:
                if future.result():
                    available_usernames.append(username)
                else:
                    taken_usernames.append(username)
                # Introduce a small random delay
                time.sleep(random.uniform(1, 3))
            except Exception as e:
                print(f"{Fore.RED}⚠️ THREAD MALFUNCTION: Exception for {username}: {e}")
    
    # Display results
    print("\n")
    print(f"{Fore.GREEN}{Style.BRIGHT}AVAILABLE USERNAMES".center(50, "="))
    for username in available_usernames:
        print(f"{Fore.GREEN}💡 {username}")
    
    print("\n")
    print(f"{Fore.RED}{Style.BRIGHT}TAKEN USERNAMES".center(50, "="))
    for username in taken_usernames:
        print(f"{Fore.RED}⛔ {username}")
    
    with open("available.txt", "a") as f:
        for username in available_usernames:
            f.write(username + "\n")
    
    print(f"\n{Fore.CYAN}🛰️ MISSION COMPLETE: Username scan finalized. Results stored in 'available.txt'")

if __name__ == "__main__":
    main()