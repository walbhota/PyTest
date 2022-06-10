def wordbreak2_generator(s, words):
    if len(s) == 0: 
        yield []
    else:
        
        for i in range(1, len(s)+1):
            sub = s[:i]
            if not sub in words:
                continue
            for others in wordbreak2_generator(s[i:], words):
                yield [sub] + others

def wordbreak2(s, words):
    words = set(words)
    for combo in wordbreak2_generator(s, words):

        print(combo)

