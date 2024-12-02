# manage.py

import sys
from django.run import runserver

def main():
    if len(sys.argv) < 2:
        print("Usage: python manage.py [command]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "runserver":
        runserver()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
