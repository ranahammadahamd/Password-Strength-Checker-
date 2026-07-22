"""
=========================================================
 SecurePass Analyzer v1.0
 Cyber Security Internship Project
=========================================================

Author : Your Name
Language : Python 3

Description:
A professional password strength analyzer with
security checks, password scoring, entropy,
crack time estimation, and history logging.
=========================================================
"""

import os

from password_checker import PasswordChecker
from utils import banner, clear_screen


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("               MAIN MENU")
    print("=" * 50)
    print("1. Analyze Password")
    print("2. View Scan History")
    print("3. About Project")
    print("4. Exit")
    print("=" * 50)


def view_history():
    """Display saved password scan history."""
    print("\n" + "=" * 60)
    print("PASSWORD SCAN HISTORY")
    print("=" * 60)

    if not os.path.exists("history.txt"):
        print("No history found.")
        return

    with open("history.txt", "r", encoding="utf-8") as file:
        print(file.read())


def about():
    """Display project information."""
    print("""
============================================================
                ABOUT SecurePass Analyzer
============================================================

Project Name :
SecurePass Analyzer

Purpose :
Analyze password strength using cybersecurity best practices.

Features
--------
✔ Password Length Check
✔ Uppercase Detection
✔ Lowercase Detection
✔ Number Detection
✔ Symbol Detection
✔ Password Score (0-100)
✔ Entropy Calculation
✔ Crack Time Estimation
✔ Common Password Detection
✔ Sequential Character Detection
✔ Repeated Character Detection
✔ Security Suggestions
✔ Scan History

Developed for Cyber Security Internship.
============================================================
""")


def analyze_password(checker):
    """Analyze a user-entered password."""

    password = input("\nEnter Password : ").strip()

    if password == "":
        print("Password cannot be empty.")
        return

    result = checker.analyze(password)

    checker.display(result)

    checker.save_history(result)


def main():

    checker = PasswordChecker()

    while True:

        clear_screen()

        banner()

        show_menu()

        choice = input("\nEnter your choice : ").strip()

        if choice == "1":

            analyze_password(checker)

            input("\nPress Enter to continue...")

        elif choice == "2":

            view_history()

            input("\nPress Enter to continue...")

        elif choice == "3":

            about()

            input("\nPress Enter to continue...")

        elif choice == "4":

            print("\nThank you for using SecurePass Analyzer.")
            print("Stay Safe. Stay Secure.\n")
            break

        else:

            print("\nInvalid Choice!")

            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
