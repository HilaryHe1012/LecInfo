import trie

def create_english_trie():
    t = trie.Trie()
    file = open("words.txt", "r", encoding="Latin-1")
    for word in file:
        if not is_weird(word.strip()):
            t.add_word(word.strip())
    file.close()
    for i in range(1,25):
        t.children[i].is_word = False #Removes singleton word (not "a")
    t.children[8].is_word = True #adds "i" back to the trie
    return t

def is_weird(s):
    for char in s:
        if ord(char) < 97 or ord(char) > 122:
            return True
    return False

t = create_english_trie()


# recursion without dynamic programming
def can_split(s):
    if s == "":
        return True
    b = False
    for i in range(len(s) - 1, max(len(s) - 22, -1), -1):
        b = b or (can_split(s[0:i]) and t.check_word(s[i:]))
    return b

# top down
def can_split_dynamic(s):
    sp = [True]
    d = {}
    for i in range(len(s)):
        b = False
        for j in range(i, max(i - 22, -1), -1):
            b = (sp[j] and t.check_word(s[j:i+1]))
            if b:
                d[i] = j
                break
        sp.append(b)
    return (sp,d)

# recursive memoization
def can_split_memo(s, cache={}):
    if s == "":
        return True
    if s in cache:
        return cache[s]
    b = False
    for i in range(len(s) - 1, max(len(s) - 22, -1), -1):
        b = b or (can_split_memo(s[0:i], cache) and t.check_word(s[i:]))
    cache[s] = b
    return b

# can split with solution recovered
def can_split_helper(s):
    if s == "":
        return True, ""
    if s in cache:
        return cache[s]
    result = False
    split = ""
    for i in range(len(s) - 1, max(len(s) - 22, -1), -1):
        b, sub_split = can_split_helper(s[0:i])
        if b and t.check_word(s[i:]):
            result = True
            split = sub_split + " " + s[i:]
            d[len(s)] = i
            break
    cache[s] = (result, split.strip())
    return cache[s]

    result, split = can_split_helper(s)
    return result, split

# recover solution
def recover_solution(s, sp, d):
    words = []
    i = len(s)
    while i != 0:
        words.append(s[d[i-1]:i])
        i = d[i-1]
    words.reverse()
    return words

