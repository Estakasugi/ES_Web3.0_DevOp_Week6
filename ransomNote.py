def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    ransomNoteDictionary = {}
        
    for char in ransomNote:
        if char in ransomNoteDictionary:
            ransomNoteDictionary[char] += 1
        else:
            ransomNoteDictionary[char] = 1

    for char in magazine:
        if char in ransomNoteDictionary:
            ransomNoteDictionary[char] -= 1
    
    for key in ransomNoteDictionary:
        if ransomNoteDictionary[key] > 0:
            return False
    
    return True
    # print(ransomNoteDictionary)
    
    

ans = canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")
print(ans)