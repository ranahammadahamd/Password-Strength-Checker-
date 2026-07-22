"""
=========================================================
password_checker.py
SecurePass Analyzer
Cyber Security Internship Project
=========================================================
"""

import math
import string
from datetime import datetime


class PasswordChecker:

    def __init__(self):
        """
        Load common passwords from file.
        """

        self.common_passwords = set()

        try:
            with open("common_passwords.txt", "r", encoding="utf-8") as file:
                for line in file:
                    password = line.strip().lower()
                    if password:
                        self.common_passwords.add(password)

        except FileNotFoundError:
            print("Warning: common_passwords.txt not found.")

    # ===================================================
    # MAIN ANALYSIS FUNCTION
    # ===================================================

    def analyze(self, password):

        result = {}

        result["password"] = password
        result["time"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # ----------------------------
        # Basic Checks
        # ----------------------------

        result["length"] = len(password)

        result["has_upper"] = any(c.isupper() for c in password)

        result["has_lower"] = any(c.islower() for c in password)

        result["has_digit"] = any(c.isdigit() for c in password)

        result["has_symbol"] = any(
            c in string.punctuation
            for c in password
        )

        # ----------------------------
        # Advanced Checks
        # ----------------------------

        result["common_password"] = (
            password.lower()
            in self.common_passwords
        )

        result["repeated"] = self.has_repeated_characters(
            password
        )

        result["sequential"] = self.has_sequential_characters(
            password
        )

        # ----------------------------
        # Security Metrics
        # ----------------------------

        result["score"] = self.calculate_score(result)

        result["strength"] = self.get_strength(
            result["score"]
        )

        result["entropy"] = self.calculate_entropy(
            password
        )

        result["crack_time"] = self.estimate_crack_time(
            result["entropy"]
        )

        result["complexity"] = self.calculate_complexity(
            result
        )

        result["suggestions"] = self.generate_suggestions(
            result
        )

        return result

    # ===================================================
    # PASSWORD SCORE
    # ===================================================

    def calculate_score(self, result):

        score = 0

        # Length

        if result["length"] >= 8:
            score += 15

        if result["length"] >= 12:
            score += 15

        if result["length"] >= 16:
            score += 10

        # Character Variety

        if result["has_upper"]:
            score += 15

        if result["has_lower"]:
            score += 15

        if result["has_digit"]:
            score += 15

        if result["has_symbol"]:
            score += 15

        # Penalties

        if result["common_password"]:
            score -= 30

        if result["repeated"]:
            score -= 10

        if result["sequential"]:
            score -= 10

        if score < 0:
            score = 0

        if score > 100:
            score = 100

        return score

    # ===================================================
    # PASSWORD STRENGTH
    # ===================================================

    def get_strength(self, score):

        if score < 40:
            return "WEAK"

        elif score < 70:
            return "MEDIUM"

        elif score < 90:
            return "STRONG"

        return "VERY STRONG"

    # ===================================================
    # PASSWORD COMPLEXITY
    # ===================================================

    def calculate_complexity(self, result):

        value = 0

        if result["has_upper"]:
            value += 1

        if result["has_lower"]:
            value += 1

        if result["has_digit"]:
            value += 1

        if result["has_symbol"]:
            value += 1

        if result["length"] >= 12:
            value += 1

        levels = {
            1: "Poor",
            2: "Average",
            3: "Good",
            4: "Very Good",
            5: "Excellent"
        }

        return levels.get(value, "Very Poor")
        # ===================================================
    # PASSWORD ENTROPY
    # ===================================================

    def calculate_entropy(self, password):

        pool = 0

        if any(c.islower() for c in password):
            pool += 26

        if any(c.isupper() for c in password):
            pool += 26

        if any(c.isdigit() for c in password):
            pool += 10

        if any(c in string.punctuation for c in password):
            pool += len(string.punctuation)

        if pool == 0:
            return 0

        entropy = len(password) * math.log2(pool)

        return round(entropy, 2)

    # ===================================================
    # ESTIMATED CRACK TIME
    # ===================================================

    def estimate_crack_time(self, entropy):

        if entropy < 28:
            return "Instantly"

        elif entropy < 35:
            return "A Few Minutes"

        elif entropy < 45:
            return "Several Hours"

        elif entropy < 60:
            return "Several Days"

        elif entropy < 80:
            return "Several Months"

        elif entropy < 100:
            return "Several Years"

        else:
            return "Centuries"

    # ===================================================
    # REPEATED CHARACTER DETECTION
    # ===================================================

    def has_repeated_characters(self, password):

        if len(password) < 3:
            return False

        count = 1

        for i in range(1, len(password)):

            if password[i] == password[i - 1]:

                count += 1

                if count >= 3:
                    return True

            else:
                count = 1

        return False

    # ===================================================
    # SEQUENTIAL CHARACTER DETECTION
    # ===================================================

    def has_sequential_characters(self, password):

        sequences = [

            "abcdefghijklmnopqrstuvwxyz",

            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",

            "0123456789",

            "qwertyuiop",

            "asdfghjkl",

            "zxcvbnm"

        ]

        password_lower = password.lower()

        for seq in sequences:

            for i in range(len(seq) - 2):

                part = seq[i:i + 3]

                if part.lower() in password_lower:
                    return True

        return False

    # ===================================================
    # PASSWORD STATISTICS
    # ===================================================

    def password_statistics(self, password):

        stats = {

            "uppercase": 0,

            "lowercase": 0,

            "digits": 0,

            "symbols": 0

        }

        for char in password:

            if char.isupper():
                stats["uppercase"] += 1

            elif char.islower():
                stats["lowercase"] += 1

            elif char.isdigit():
                stats["digits"] += 1

            elif char in string.punctuation:
                stats["symbols"] += 1

        return stats
        # ===================================================
    # SECURITY SUGGESTIONS
    # ===================================================

    def generate_suggestions(self, result):

        suggestions = []

        if result["length"] < 12:
            suggestions.append(
                "Increase password length to at least 12 characters."
            )

        if not result["has_upper"]:
            suggestions.append(
                "Add at least one uppercase letter (A-Z)."
            )

        if not result["has_lower"]:
            suggestions.append(
                "Add at least one lowercase letter (a-z)."
            )

        if not result["has_digit"]:
            suggestions.append(
                "Include at least one numeric digit (0-9)."
            )

        if not result["has_symbol"]:
            suggestions.append(
                "Use special symbols like @, #, $, %, &, !."
            )

        if result["common_password"]:
            suggestions.append(
                "Avoid commonly used passwords."
            )

        if result["repeated"]:
            suggestions.append(
                "Avoid repeating the same character multiple times."
            )

        if result["sequential"]:
            suggestions.append(
                "Avoid sequential patterns like abc, 123 or qwerty."
            )

        if len(suggestions) == 0:
            suggestions.append(
                "Excellent! Your password follows strong security practices."
            )

        return suggestions

    # ===================================================
    # DISPLAY REPORT
    # ===================================================

    def display(self, result):

        stats = self.password_statistics(result["password"])

        print("\n")
        print("=" * 65)
        print("              PASSWORD SECURITY REPORT")
        print("=" * 65)

        print(f"Password Length         : {result['length']}")
        print(f"Uppercase Letters       : {stats['uppercase']}")
        print(f"Lowercase Letters       : {stats['lowercase']}")
        print(f"Digits                  : {stats['digits']}")
        print(f"Special Symbols         : {stats['symbols']}")

        print("-" * 65)

        print(f"Contains Uppercase      : {'Yes' if result['has_upper'] else 'No'}")
        print(f"Contains Lowercase      : {'Yes' if result['has_lower'] else 'No'}")
        print(f"Contains Numbers        : {'Yes' if result['has_digit'] else 'No'}")
        print(f"Contains Symbols        : {'Yes' if result['has_symbol'] else 'No'}")
        print(f"Common Password         : {'Yes' if result['common_password'] else 'No'}")
        print(f"Repeated Characters     : {'Yes' if result['repeated'] else 'No'}")
        print(f"Sequential Characters   : {'Yes' if result['sequential'] else 'No'}")

        print("-" * 65)

        print(f"Password Score          : {result['score']}/100")
        print(f"Strength                : {result['strength']}")
        print(f"Complexity              : {result['complexity']}")
        print(f"Entropy                 : {result['entropy']} bits")
        print(f"Estimated Crack Time    : {result['crack_time']}")

        print("=" * 65)
        print("SECURITY RECOMMENDATIONS")
        print("=" * 65)

        for index, tip in enumerate(result["suggestions"], start=1):
            print(f"{index}. {tip}")

        print("=" * 65)

    # ===================================================
    # SAVE HISTORY
    # ===================================================

    def save_history(self, result):

        with open("history.txt", "a", encoding="utf-8") as file:

            file.write("=" * 60 + "\n")
            file.write(f"Date               : {result['time']}\n")
            file.write(f"Password Length    : {result['length']}\n")
            file.write(f"Score              : {result['score']}/100\n")
            file.write(f"Strength           : {result['strength']}\n")
            file.write(f"Complexity         : {result['complexity']}\n")
            file.write(f"Entropy            : {result['entropy']} bits\n")
            file.write(f"Crack Time         : {result['crack_time']}\n")
            file.write(f"Common Password    : {result['common_password']}\n")
            file.write(f"Repeated Characters: {result['repeated']}\n")
            file.write(f"Sequential Chars   : {result['sequential']}\n")

            file.write("Suggestions:\n")

            for tip in result["suggestions"]:
                file.write(f" - {tip}\n")

            file.write("=" * 60 + "\n\n")
