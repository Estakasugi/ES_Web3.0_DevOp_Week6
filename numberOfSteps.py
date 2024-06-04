def numberOfSteps(num):
    """
    :type num: int
    :rtype: int
    """
    steps = 0

    while num != 0:
            
      if (num % 2 == 0):
        num = num / 2
        steps += 1
      else:
        num -= 1
        steps += 1
        
    return steps

testCase1 = numberOfSteps(14)
testCase2 = numberOfSteps(8)
testCase3 = numberOfSteps(123)
