import hashlib
import os

def hash_string(data, algo):
    if algo == 'md5':
        return hashlib.md5(data.encode()).hexdigest()
    elif algo == 'sha1':
        return hashlib.sha1(data.encode()).hexdigest()
    elif algo == 'sha256':
        return hashlib.sha256(data.encode()).hexdigest()

def hash_file(path, algo):
    h = hashlib.new(algo)
    try:
        with open(path, 'rb') as f:
            while chunk := f.read(8192):
                h.update(chunk)
        return h.hexdigest()
    except FileNotFoundError:
        return None

def select_algorithm():
    print("\n=== Choose Hashing Algorithm ===")
    print("[1] MD5")
    print("[2] SHA-1 (Not recommended due to vulnerabilities)")
    print("[3] SHA-256")
    
    while True:
        algo_choice = input("Select algorithm (1-3): ").strip()
        if algo_choice == '1':
            return 'md5'
        elif algo_choice == '2':
            print("Warning: SHA-1 is considered obsolete for secure hashing. Proceed with caution.")
            confirm = input("Still use SHA-1? (y/n): ").lower()
            if confirm == 'y':
                return 'sha1'
        elif algo_choice == '3':
            return 'sha256'
        else:
            print("Invalid choice. Enter 1, 2, or 3.")

def get_valid_string():
    while True:
        data = input("Enter the string to hash: ").strip()
        if data.isalpha():  # Check if string only contains alphabets
            return data
        else:
            print("Invalid input. Please enter a valid string (letters only).")

def compare_hashes():
    print("\n=== Hash Comparison ===")
    hash1 = input("Enter the first hash: ").strip()
    hash2 = input("Enter the second hash: ").strip()
    
    if hash1 == hash2:
        print("The hashes match!")
    else:
        print("The hashes do not match.")

def main():
    print("=== HashGen - Hasher MultiTool ===        Made For Practice by https://github.com/j0xh ")
    print("[1] Hash a string")
    print("[2] Hash a file")
    print("[3] Compare two hashes")

    choice = input("Choose an option (1/2/3): ").strip()

    if choice == '1':
        data = get_valid_string()  # Get valid string input
        algo = select_algorithm()
        result = hash_string(data, algo)
        print(f"\n{algo.upper()} hash:\n{result}")
    
    elif choice == '2':
        path = input("Enter the full file path (e.g., C:\\Users\\you\\file.txt): ").strip()
        if not os.path.exists(path):
            print("File not found.")
            return
        algo = select_algorithm()
        result = hash_file(path, algo)
        if result:
            print(f"\n{algo.upper()} hash of file:\n{result}")
        else:
            print("Error hashing file.")
    
    elif choice == '3':
        compare_hashes()  # Compare two hashes
    
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
