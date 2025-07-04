from functions.get_files_info import get_files_info

def main():
    print("Testing get_files_info function:")
    print("=" * 50)

    print("\n1. Testing current directory (calculator):")
    print('Running: get_files_info("calculator", ".")')
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)

    print("\n2. Testing pkg subdirectory:")
    print('Running: get_files_info("calculator", "pkg")')
    result = get_files_info("calculator", "pkg")
    print("Result for pkg subdirectory:")
    print(result)

    print("\n3. Testing access to /bin (should fail):")
    print('Running: get_files_info("calculator", "/bin")')
    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    print("\n4. Testing access to parent directory (should fail):")
    print('Running: get_files_info("calculator", "../")')
    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)

    print("\n5. Testing with None directory parameter:")
    print('Running: get_files_info("calculator", None)')
    result = get_files_info("calculator", None)
    print("Result for None directory:")
    print(result)

if __name__ == "__main__":
    main()
