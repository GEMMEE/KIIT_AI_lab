'''
7. Write a function, is_vowel that returns the value true if a given character
is a vowel, and otherwise returns false. Write another function main. In main()
function accept a string from user and count number of vowels in that string.
'''

def is_vowel(a):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    if a in vowels:
        return True
    else:
        return False

def main():
    str = input("Type a string: ")
    count = 0
    for i in str:
        if is_vowel(i):
            count = count + 1
    print(f"\"{str}\" has {count} vowels")

if __name__ == "__main__":
    main()
