"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]

Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lastNode = head
        midNode = head
        lastNodeMovingCounter = 1

        while (lastNode.next != None):
            lastNode = lastNode.next
            lastNodeMovingCounter += 1
            
            if (lastNodeMovingCounter % 2 == 0):
                midNode = midNode.next
        
        return midNode
