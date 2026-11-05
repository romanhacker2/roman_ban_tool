import os, sys, time, random

RESET="\033[0m"; BOLD="\033[1m"; GREEN="\033[92m"; RED="\033[91m"; YELLOW="\033[93m"; BLUE="\033[94m"; CYAN="\033[96m"; WHITE="\033[97m"

def clear(): os.system("clear")

def show_banner():
    print(f"""{RED}{BOLD}
    ██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║
    ██████╔╝██║   ██║██╔████╔██║███████║██╔██╗ ██║
    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    {CYAN}         [ C Y B E R   B A N   H A M M E R ]{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    {GREEN}  WA: {WHITE}923037224620 {GREEN}| TG: {WHITE}@romanempire078{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    """)

def show_menu():
    print(f"""{BLUE}{BOLD}
    ┌──────────────────────────────────────────────────┐
    │                SELECT TARGET PLATFORM            │
    ├──────────────────────────────────────────────────┤
    │  {WHITE}[1]{BLUE} Instagram Account Ban                  │
    │  {WHITE}[2]{BLUE} Facebook Account Ban                   │
    │  {WHITE}[3]{BLUE} TikTok Account Ban                     │
    │  {WHITE}[4]{BLUE} YouTube Channel Ban                   │
    │  {WHITE}[5]{BLUE} Exit System                             │
    └──────────────────────────────────────────────────┘
{RESET}""")

def execute_ban(platform):
    clear(); show_banner()
    print(f"{GREEN}{BOLD}  [!] TARGET PLATFORM: {WHITE}{platform.upper()}{RESET}\n")
    
    target = input(f"{CYAN}{BOLD}  ► Enter Profile Link (e.g., https://instagram.com/username): {RESET}").strip()
    
    if not target:
        print(f"{RED}  [!] Error: Target cannot be empty!{RESET}")
        time.sleep(2)
        return

    # Check if input is a valid link (must start with http or contain .com)
    if not (target.startswith("http://") or target.startswith("https://") or ".com/" in target or ".com" in target):
        print(f"\n{RED}{BOLD}  [!] ERROR: TARGET PROFILE NOT FOUND!{RESET}")
        print(f"{RED}  [!] You entered a username. Please enter a valid FULL PROFILE LINK.{RESET}")
        print(f"{YELLOW}  [!] Example: https://www.{platform.lower()}.com/username{RESET}")
        time.sleep(3)
        return

    # Clean target name for display (extract username from link)
    display_target = target.rstrip("/").split("/")[-1]
    
    print(f"\n{YELLOW}  [~] Link Verified. Initializing Ban Protocol for: {WHITE}{display_target}{RESET}")
    time.sleep(1)
    
    # Fake Scanning Animation
    frames = ["|", "/", "-", "\\"]
    for _ in range(15):
        for frame in frames:
            sys.stdout.write(f"\r{YELLOW}{BOLD}  [{frame}] Bypassing {platform} Security Protocols...{RESET}   ")
            sys.stdout.flush()
            time.sleep(0.05)
    
    print(f"\n{GREEN}  [✓] Security Bypassed! Target Located.{RESET}")
    time.sleep(0.8)
    print(f"{YELLOW}  [~] Sending Mass Reports...{RESET}\n")
    time.sleep(0.5)

    # Massive Reporting Loop (Scrolling effect)
    total_reports = random.randint(45000, 65000)
    try:
        for i in range(1, total_reports + 1, random.randint(50, 150)):
            fake_ip = f"{random.randint(11, 250)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
            sys.stdout.write(f"\033[91m  [REPORT {i:05d}] Sent from IP: {fake_ip} -> SUCCESS\033[0m\n")
            sys.stdout.flush()
            time.sleep(0.005) # Fast scrolling
    except KeyboardInterrupt:
        print(f"\n\n{RED}  [!] Process Aborted.{RESET}")
        time.sleep(1)
        return

    print(f"\n{YELLOW}  [~] Finalizing Ban Process...{RESET}")
    time.sleep(1.5)

    # Final Success Screen
    clear(); show_banner()
    print(f"\n{RED}{BOLD}")
    print("  ╔══════════════════════════════════════════════════╗")
    print("  ║               ACCOUNT BANNED!                    ║")
    print("  ╠══════════════════════════════════════════════════╣")
    print(f"  ║  {YELLOW}PLATFORM : {WHITE}{platform.upper():<33} {RED}║")
    print(f"  ║  {YELLOW}TARGET   : {WHITE}{display_target[:33]:<33} {RED}║")
    print(f"  ║  {YELLOW}REPORTS  : {WHITE}{total_reports} Sent{' '*(22-len(str(total_reports)))} {RED}║")
    print(f"  ║  {YELLOW}STATUS   : {RED}PERMANENTLY BANNED{' '*14} {RED}║")
    print("  ╚══════════════════════════════════════════════════╝")
    print(f"{RESET}")
    
    input(f"{CYAN}  Press ENTER to return to menu...{RESET}")

def main():
    while True:
        try:
            clear(); show_banner(); show_menu()
            choice = input(f"{GREEN}{BOLD}  └──► Select Platform [1-5]: {RESET}").strip()
            
            if choice == "1": execute_ban("Instagram")
            elif choice == "2": execute_ban("Facebook")
            elif choice == "3": execute_ban("TikTok")
            elif choice == "4": execute_ban("YouTube")
            elif choice == "5":
                print(f"\n{RED}  Exiting System...{RESET}")
                time.sleep(1)
                break
            else:
                print(f"{RED}  Invalid Option!{RESET}")
                time.sleep(1)
        except KeyboardInterrupt:
            break

if __name__ == "__main__": main()
EOF
