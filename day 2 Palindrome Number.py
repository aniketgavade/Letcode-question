
# Palindrome Number Problem

# Given an integer `x`, determine if `x` is a palindrome.
#  Return `true` if `x` reads the same forward and backward, and `false` otherwise.

# ## Examples

# **Example 1**  
# **Input**: `x = 121`  
# **Output**: `true`  
# **Explanation**: The number `121` reads the same from left to right and from right to left.

# **Example 2**  
# **Input**: `x = -121`  
# **Output**: `false`  
# **Explanation**: Reading from left to right yields `-121`, but from right to left it reads `121-`. Thus, it is not a palindrome.

# **Example 3**  
# **Input**: `x = 10`  
# **Output**: `false`  
# **Explanation**: From right to left, `10` reads as `01`, which is not the same as the original.

# constraints
#  where -2^31 <= x <= 2^31 - 1

# ans=
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        temp = x
        while temp != 0:
            digit = temp % 10
            reversed_num = 10 * reversed_num + digit
            temp //= 10
            
        return reversed_num == x
