from string import ascii_lowercase, punctuation, digits

def is_pangram(sentence: str) -> bool:
    for i in punctuation:
        sentence = sentence.replace(i, '')
        
    for i in digits:
        sentence = sentence.replace(i, '')
        
    sentence = sentence.replace(' ', '')

    return list(sorted(set(sentence.lower()))) == list(ascii_lowercase)


def is_pangram2(sentence: str) -> bool:
    for i in ascii_lowercase:
        if i not in sentence:
            return False
        
        return True
    
    
def is_pangram3(sentence: str) -> bool:
    return set(ascii_lowercase).issubset(sentence.lower())