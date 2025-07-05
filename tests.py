from functions.get_file_content import get_file_content


def test():
    # Test reading main.py in calculator
    result = get_file_content("calculator", "main.py")
    print("Result for calculator/main.py:")
    print(result)
    print("")

    # Test reading calculator.py in calculator/pkg
    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for calculator/pkg/calculator.py:")
    print(result)
    print("")

    # Test reading a file outside the working directory
    result = get_file_content("calculator", "/bin/cat")
    print("Result for /bin/cat (should error):")
    print(result)
    print("")


if __name__ == "__main__":
    test()
