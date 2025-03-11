import string

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_sum(start, end):
    return sum(n for n in range(start, end + 1) if is_prime(n))

def length_converter(value, unit):
    if unit.upper() == 'M':
        return round(value * 3.28084, 2)
    elif unit.upper() == 'F':
        return round(value / 3.28084, 2)
    else:
        return "Invalid unit"

def consonant_counter(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)

def min_max_finder(numbers):
    return min(numbers), max(numbers)

def palindrome_checker(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

def word_counter(file_path):
    target_words = {"the", "was", "and"}
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
        words = text.split()
        return sum(words.count(word) for word in target_words)
    except FileNotFoundError:
        return "File not found"

def main():
    while True:
        print("\nMenu:")
        print("1. Prime Number Sum Calculator")
        print("2. Length Unit Converter")
        print("3. Consonant Counter")
        print("4. Min-Max Number Finder")
        print("5. Palindrome Checker")
        print("6. Word Counter")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            start = int(input("Enter start of range: "))
            end = int(input("Enter end of range: "))
            print("Sum of primes:", prime_sum(start, end))
        
        elif choice == '2':
            value = float(input("Enter numeric value: "))
            unit = input("Enter conversion direction (M for meters to feet, F for feet to meters): ")
            print("Converted length:", length_converter(value, unit))
        
        elif choice == '3':
            text = input("Enter text: ")
            print("Number of consonants:", consonant_counter(text))
        
        elif choice == '4':
            num_count = int(input("How many numbers will you enter? "))
            numbers = [float(input(f"Enter number {i+1}: ")) for i in range(num_count)]
            smallest, largest = min_max_finder(numbers)
            print(f"Smallest: {smallest}, Largest: {largest}")
        
        elif choice == '5':
            text = input("Enter text: ")
            print("Is palindrome:", palindrome_checker(text))
        
        elif choice == '6':
            file_path = input("Enter file path: ")
            print("Word count:", word_counter(file_path))
        
        elif choice == '7':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
