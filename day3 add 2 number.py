# Adding Two Numbers in Reverse Order Using Linked Lists
# In this problem, we’re given two linked lists representing non-negative integers where each node contains a single digit. The digits are stored in reverse order, so the 1's place is at the head of the list. The goal is to add these two numbers and return the sum as a new linked list, also in reverse order.

# Problem Breakdown
# Let’s break down the problem with an example:

# Example 1:
# Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
# Output: [7, 0, 8]
# Explanation: 342 + 465 = 807, so the linked list is [7, 0, 8].
# Solution Approach
# Initialize Variables:

# Use a dummy head node for easy list construction.
# Initialize a carry variable to manage sums greater than 9.
# Iterate Through Lists:

# Loop while there are nodes left in either list or a carry remains.
# At each step, get the value of the current nodes from l1 and l2 (or 0 if the node is None).
# Calculate the sum of the current values plus the carry.
# Create New Node:

# The new digit is columnSum % 10, and the carry for the next column is columnSum // 10.
# Link this new node to the result list.
# Return Result:

# The result list starts at dummyHead.next.



from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
