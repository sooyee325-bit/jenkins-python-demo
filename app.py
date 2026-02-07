"""
Dummy Python application for Jenkins CI/CD practice
"""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    print("Starting dummy Python application...")

    x = 10
    y = 5

    print(f"Add result: {x} + {y} = {add(x, y)}")
    print(f"Subtract result: {x} - {y} = {subtract(x, y)}")

    print("Dummy application finished successfully.")


if __name__ == "__main__":
    main()
