# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# 1.Open brackets must be closed by the same type of brackets.
# 2.Open brackets must be closed in the correct order.
# 3.Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


# solution=>
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize an empty stack
        bracket_map = {')': '(', '}': '{', ']': '['}  # Mapping of closing to opening brackets

        # Loop through each character in the input string
        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                # Check if the stack is empty or the top of the stack doesn't match
                top_element = stack.pop() if stack else '#'  # Use '#' if stack is empty
                if bracket_map[char] != top_element:  # Check if it matches
                    return False  # Not valid
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets matched correctly
        return not stack  # Return True if empty, else False


