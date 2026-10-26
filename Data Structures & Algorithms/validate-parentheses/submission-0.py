class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        bracket_map = {")": "(", "}": "{", "]": "["}
        
        for c in s: 
            # If c is a closing bracket (it is in the hashmap)
            if c in bracket_map: 
                # 1. Check if the stack is empty first
                if len(stack) == 0:
                    return False  # No opening bracket exists to match it! Instantly invalid.
                
                # 2. Since the stack has items, it is safe to pop
                top_element = stack.pop()
            
                # 3. Check if they match
                if bracket_map[c] != top_element:
                    return False
            else: 
                # If it's an opening bracket, push it to the stack
                stack.append(c)

        return len(stack) == 0