from functions.run_python_file import run_python_file


def test():
    # Test running main.py in calculator
    result = run_python_file("calculator", "main.py")
    print("Result for running calculator/main.py:")
    print(result)
    print("")

    # Test running tests.py in calculator
    result = run_python_file("calculator", "tests.py")
    print("Result for running calculator/tests.py:")
    print(result)
    print("")

    # Test running a file outside the working directory
    result = run_python_file("calculator", "../main.py")
    print("Result for running ../main.py (should error):")
    print(result)
    print("")

    # Test running a non-existent file
    result = run_python_file("calculator", "nonexistent.py")
    print("Result for running nonexistent.py (should error):")
    print(result)
    print("")


if __name__ == "__main__":
    test()
