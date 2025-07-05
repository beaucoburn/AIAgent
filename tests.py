from functions.write_file import write_file


def test():
    # Test writing to lorem.txt in calculator
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for writing to calculator/lorem.txt:")
    print(result)
    print("")

    # Test writing to morelorem.txt in calculator/pkg
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for writing to calculator/pkg/morelorem.txt:")
    print(result)
    print("")

    # Test writing to a file outside the working directory
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for writing to /tmp/temp.txt (should error):")
    print(result)
    print("")


if __name__ == "__main__":
    test()
