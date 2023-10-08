# Basics in Python
# Michi von Ah - October 2023

# Data structures
# Array
brands = ["Apple", "Samsung", "Google", "OnePlus"]

# Dictionary
phone = {
  "brand": "Apple",
  "model": "iPhone 14 Pro",
  "cameras": 3
}

# Dictionaries in Array
phones = [
    {
        "brand":"Apple",
        "model":"iPhone 14 Pro",
        "cameras":3,
        "memory":"6GB"
    },
    {
        "brand":"Samsung",
        "model":"Galaxy S23",
        "cameras":3,
        "memory":"8GB"
    }
]

# Split strings into Array
fruits = "Apple,Banana,Pear,Cherry"
split = fruits.split(",") # Output: ['Apple', 'Banana', 'Pear', 'Cherry']

# Transform text
text = "I love Python!"

upper = text.upper() # Output: I LOVE PYTHON!
lower = text.lower() # Output: i love python!

# Convert String-To-Int and Int-To-String
number = 12
numberConverted = int("12")

string = "Hello World"

combined = string + str(numberConverted) # Output: Hello World12
