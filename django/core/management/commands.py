# manage.py

import sys
import os
import argparse

def commands_frameworks(command):
    """Custom command handler for your framework."""
    if command == "runserver":
        print("Starting server...")
        # Serverni ishga tushirish uchun kerakli kod
        # Misol uchun: aiohttp, FastAPI, yoki boshqa serverni ishga tushirish
    elif command == "makemigrations":
        print("Creating migrations...")
        # Migratsiya yaratish funksiyasi
    elif command == "migrate":
        print("Applying migrations...")
        # Ma'lumotlar bazasini yangilash funksiyasi
    else:
        print(f"Unknown command: {command}")

def main():
    """Framework asosiy funksiyasi."""
    if len(sys.argv) < 2:
        print("Usage: python manage.py [command]")
        sys.exit(1)

    command = sys.argv[1]
    commands_frameworks(command)

if __name__ == "__main__":
    main()
