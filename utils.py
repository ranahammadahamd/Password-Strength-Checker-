"""
=========================================================
utils.py
Utility Functions for SecurePass Analyzer
=========================================================
"""

import os
import platform


class Colors:
    """ANSI Color Codes"""

    RESET = "\033[0m"

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"

    BOLD = "\033[1m"


# ==========================================================
# CLEAR TERMINAL
# ==========================================================

def clear_screen():

    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# ==========================================================
# APPLICATION BANNER
# ==========================================================

def banner():

    print(Colors.CYAN + Colors.BOLD)

    print("=" * 70)
    print("              SecurePass Analyzer v1.0")
    print("         Cyber Security Internship Project")
    print("=" * 70)

    print(Colors.RESET)


# ==========================================================
# COLOR FUNCTIONS
# ==========================================================

def success(text):
    return Colors.GREEN + text + Colors.RESET


def warning(text):
    return Colors.YELLOW + text + Colors.RESET


def danger(text):
    return Colors.RED + text + Colors.RESET


def info(text):
    return Colors.BLUE + text + Colors.RESET


# ==========================================================
# TITLES
# ==========================================================

def title(text):

    print()

    print(Colors.MAGENTA + Colors.BOLD)

    print("=" * 60)

    print(text.center(60))

    print("=" * 60)

    print(Colors.RESET)


# ==========================================================
# LINE
# ==========================================================

def line():

    print("-" * 60)


# ==========================================================
# PASSWORD STRENGTH PROGRESS BAR
# ==========================================================

def progress_bar(score):

    total_blocks = 20

    filled = int(score / 5)

    empty = total_blocks - filled

    bar = "█" * filled + "-" * empty

    print()

    print(f"[{bar}] {score}/100")

    print()


# ==========================================================
# PRINT STRENGTH WITH COLOR
# ==========================================================

def print_strength(strength):

    if strength == "WEAK":

        print(danger("Strength : WEAK"))

    elif strength == "MEDIUM":

        print(warning("Strength : MEDIUM"))

    elif strength == "STRONG":

        print(success("Strength : STRONG"))

    else:

        print(success("Strength : VERY STRONG"))


# ==========================================================
# CYBER SECURITY WARNING
# ==========================================================

def security_warning():

    print()

    print(danger("WARNING"))

    print("------------------------------------------")

    print("Weak passwords can be cracked easily.")

    print("Never reuse passwords across websites.")

    print("Enable Two-Factor Authentication (2FA).")

    print("Use a password manager.")

    print("------------------------------------------")


# ==========================================================
# EXIT MESSAGE
# ==========================================================

def goodbye():

    print()

    print(success("Thank you for using SecurePass Analyzer."))

    print(info("Stay Safe • Stay Secure"))

    print()


# ==========================================================
# MASK PASSWORD
# ==========================================================

def mask_password(password):

    return "*" * len(password)


# ==========================================================
# ASCII LOGO
# ==========================================================

def logo():

    print(Colors.GREEN)

    print(r"""
   _____                            _____
  / ____|                          |  __ \
 | (___   ___  ___ _   _ _ __ ___  | |__) |_ _ ___ ___
  \___ \ / _ \/ __| | | | '__/ _ \ |  ___/ _` / __/ __|
  ____) |  __/ (__| |_| | | |  __/ | |  | (_| \__ \__ \
 |_____/ \___|\___|\__,_|_|  \___| |_|   \__,_|___/___/

        SecurePass Analyzer
    """)

    print(Colors.RESET)
