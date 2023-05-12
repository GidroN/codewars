from string import ascii_lowercase, punctuation, digits

def is_pangram(sentence: str) -> bool:
    for i in punctuation:
        sentence = sentence.replace(i, '')
        
    for i in digits:
        sentence = sentence.replace(i, '')
        
    sentence = sentence.replace(' ', '')

    return list(sorted(set(sentence.lower()))) == list(ascii_lowercase)


print(is_pangram("The quick brown fox jumps over the lazy dog"))