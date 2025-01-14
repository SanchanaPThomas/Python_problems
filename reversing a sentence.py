def reverseWords(s):
    # Step 1: Split the string by spaces and remove empty strings
    words = s.strip().split()
    print(words)
    
    # Step 2: Reverse the list of words
    reversed_words = words[-1:]
    print(reversed_words)
    
    # Step 3: Join the reversed words with a single space
    return ' '.join(reversed_words)
s=input('enter a string')
print(reverseWords(s))
