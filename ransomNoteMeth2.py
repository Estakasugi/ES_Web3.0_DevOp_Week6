def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    magazineDictionary = {}
        
    for char in magazine:
        if char in magazineDictionary:
            magazineDictionary[char] += 1
        else:
            magazineDictionary[char] = 1

    # print(magazineDictionary)

    for char in ransomNote:
        if char in magazineDictionary:
            magazineDictionary[char] -= 1
        
            if magazineDictionary[char] == 0:
                return False
        
        else:
            return False
            
    return True

    

ans = canConstruct("a", "b")
print(ans)