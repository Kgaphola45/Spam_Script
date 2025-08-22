"""
Message Automation Script
-------------------------
This script automates typing and sending a message multiple times
using pyautogui. Useful for testing automation workflows.

Requirements:
    pip install pyautogui
"""

import pyautogui
import time

def send_messages(message: str, count: int, delay: float = 0.3) -> None:
    """
    Send a given message multiple times.

    Args:
        message (str): The message to send.
        count (int): How many times to send the message.
        delay (float): Delay in seconds between each message.
    """
    print("\nYou have 5 seconds to click on the input field...")
    time.sleep(5)

    for i in range(count):
        pyautogui.typewrite(message)
        pyautogui.press("enter")
        print(f"[{i+1}/{count}] Message sent.")
        time.sleep(delay)


def main():
    print("=== Message Automation Script ===\n")
    message = input("Enter the message you want to send: ")

    while True:
        try:
            count = int(input("How many times do you want to send it? "))
            if count <= 0:
                raise ValueError("Count must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    while True:
        try:
            delay = float(input("Delay between messages (in seconds, e.g. 0.3): "))
            if delay < 0:
                raise ValueError("Delay cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    send_messages(message, count, delay)


if __name__ == "__main__":
    main()
