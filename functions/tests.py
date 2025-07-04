from get_files_info import get_files_info

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
