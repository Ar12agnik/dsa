def infix_to_postfix(expr):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    stack = []
    output = []
    
    tokens = expr.split()
    for token in tokens:
        if token.isalpha():
            
            output.append(token)
        elif token in precedence:
            
            while stack and stack[-1] != '(' and precedence[token] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            
            stack.append(token)
        elif token == '(':
            
            stack.append(token)
        elif token == ')':
            
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            
            stack.pop()
    
    while stack:
        output.append(stack.pop())
    
    return ' '.join(output)
expr = "a + b * c / ( d - a ) ^ c"
postfix = infix_to_postfix(expr)
print(postfix)  
