import sys


def fibonacci(n):
    if n <= 0:
        return False, []

    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return True, fib_sequence


def main():
    if len(sys.argv) != 2:
        print("Usage: python fibonacci.py <number>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])

        result = fibonacci(n)
        if result[0]:
            print("Fibonacci sequence:")
            print(result[1])
        else:
            print("Please provide a valid positive integer.")
    except ValueError:
        print("Please provide a valid positive integer.")
        sys.exit(1)


if __name__ == "__main__":
    main()
