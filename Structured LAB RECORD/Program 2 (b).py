def word_count(sentence):
    words = sentence.split()
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    
    # Return the total word count and the word frequency dictionary
    return len(words), word_frequency

# Test the function
sentence = input("Enter a sentence: ")
word_count_result, word_frequency_result = word_count(sentence)

print(f"The number of words in the sentence is: {word_count_result}")
print(f"The frequency of each word is: {word_frequency_result}")
