
def percedence(op):
    if op == '(' or op == ')' : return 0
    elif op == '+' or op == '-' : return 1
    elif op == '*' or op == '/' : return 2
    else : return -1

def huwi(expr):
    stack = []
    output = []
    
    for term in expr:
        if term == '(' : stack.append('(')
        elif term == ')' :
            while len(stack):
                op = stack.pop()
                if op == '(' : break
                else : output.append(op)
        elif term in ['+', '-', '*', '/']:
            while len(stack):
                op = stack[-1]
                if percedence(term) <= percedence(op):
                    output.append(op)
                    stack.pop()
                else: break
            stack.append(term)
        else: output.append(term)
    
    while len(stack):
        output.append(stack.pop())
    return ''.join(output)

word = input()
print(huwi(word))