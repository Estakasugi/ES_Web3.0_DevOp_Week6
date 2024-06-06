"""
LC - 1002. Find Common Characters
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.



Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
"""
def commonChars(words):

    # build a dictionary to be the comparison dicrtionary
    charDictionary = {}
    for char in words[0]:
        if char in charDictionary:
            charDictionary[char] += 1
        else:
            charDictionary[char] = 1

    # create the rest of dictionaries
    restOfDictionariesList = []
    for i in range(1, len(words)):
        dictionary = {}
        for char in words[i]:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
        restOfDictionariesList.append(dictionary)

    
    # update the comparison dictionary based on the rest of dictionaries
    for dictionary in restOfDictionariesList:
        for key in charDictionary:
            
            if key not in dictionary:
                charDictionary[key] = 0
            else:
                if (charDictionary[key] > dictionary[key]):
                    charDictionary[key] = dictionary[key]

    # convert the comparison dictionary to a list and output
    charDictionaryList = []
    for key in charDictionary:

        if charDictionary[key] > 0:
            for i in range(charDictionary[key]):
                charDictionaryList.append(key)

    return charDictionaryList

testCase = commonChars(["bella","label","roller"])
testCase2 = commonChars(["cool","lock","cook"])
print(testCase)