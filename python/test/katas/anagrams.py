#anamgram simple
def anagrams1(word, words):
    ls = []
    for i in words:
        c = 0
        for j in set(word):
            if str(word).count(j) == str(i).count(j) and len(i) == len(word):
                c = c+1
        if c == len(set(word)):
            ls.append(i)
    return ls

#anagrams logic
def anagrams(a,word,words):return [x for x in words if sorted(x) == sorted(word)]

print(anagrams1('abba',['aabb','abbc','baab','baba','abcd','abbab']))
