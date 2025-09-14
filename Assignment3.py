# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 23:17:13 2025

@author: Jae
"""

#!/usr/bin/env python3
"""
assignment_exercises.py

Implements the 10 exercises from the PPT.
Each exercise is implemented as a function, and a demo runner prints sample results.
"""

# 1. Calculate area of a rectangle
def area_rectangle(length: float, width: float) -> float:
    return length * width

# 2. Greeting message with name and age
def greeting(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old!"

# 3. Check if number is even or odd
def even_or_odd(n: int) -> str:
    return "Even" if n % 2 == 0 else "Odd"

# 4. Find max and min in a list
def find_max_min(numbers: list) -> tuple:
    return (max(numbers), min(numbers)) if numbers else (None, None)

# 5. Check if string is palindrome
def is_palindrome(s: str) -> bool:
    s_clean = "".join(ch.lower() for ch in s if ch.isalnum())
    return s_clean == s_clean[::-1]

# 6. Calculate compound interest
def compound_interest(principal: float, rate: float, time: int) -> float:
    # rate should be in percentage, time in years
    amount = principal * ((1 + rate / 100) ** time)
    return round(amount, 2)

# 7. Convert days to years, weeks, and days
def convert_days(days: int) -> tuple:
    years = days // 365
    weeks = (days % 365) // 7
    remaining_days = (days % 365) % 7
    return years, weeks, remaining_days

# 8. Sum of positive numbers in a list
def sum_of_positives(numbers: list) -> int:
    return sum(n for n in numbers if n > 0)

# 9. Count words in a sentence
def count_words(sentence: str) -> int:
    return len(sentence.split())

# 10. Swap two variables
def swap(a, b) -> tuple:
    return b, a


# Demo runner
def demo():
    print("=== Demo Results ===\n")

    # 1
    print("1) Rectangle area (5 x 3):", area_rectangle(5, 3))

    # 2
    print("2) Greeting:", greeting("Gabriela", 18))

    # 3
    print("3) Number 7 is:", even_or_odd(7))

    # 4
    nums = [5, 1, 9, 3, 7]
    print("4) Max/Min of", nums, "=>", find_max_min(nums))

    # 5
    word = "Racecar"
    print(f"5) '{word}' is palindrome?", is_palindrome(word))

    # 6
    print("6) Compound Interest (P=1000, r=5%, t=2yrs):", compound_interest(1000, 5, 2))

    # 7
    print("7) 400 days =", convert_days(400), "(years, weeks, days)")

    # 8
    nums2 = [-2, 5, -1, 7, 0, 3]
    print("8) Sum of positives in", nums2, "=", sum_of_positives(nums2))

    # 9
    sentence = "This is a simple test sentence"
    print("9) Word count:", count_words(sentence))

    # 10
    a, b = 10, 20
    a, b = swap(a, b)
    print("10) Swapping values (10, 20) =>", (a, b))

    print("\n=== End Demo ===")


if __name__ == "__main__":
    demo()
