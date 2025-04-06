def word_count(sentence):
    words=sentence.split()
    return len(words)
# Test the function
sentence = input("Enter a sentence: ")
print(f"The number of words in the sentence is: {word_count(sentence)}")

