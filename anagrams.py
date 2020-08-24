def anagram(s1, s2):
    
    #Edge Case detection
    if len(s1) != len(s2):
        print("False")
        return False
    
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else: count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True
            

        

s1 = "Dog god eats tea"
s2 = "god dog eat seat"
anagram(s1,s2)