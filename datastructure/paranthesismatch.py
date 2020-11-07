from stack import Stack

def is_match(t,p):
    if t=="(" and p==")":
        return True
    elif t=="[" and p=="]":
        return True
    elif t=="{" and p=="}":
        return True
    else:
        return False

    

def is_balanced(para_string):
    s=Stack()
    balanced=True
    index=0
    while index<len(para_string) and balanced:
        paran=para_string[index]
        if paran in "{[(":
            s.push(paran)
        else:
            if s.is_empty():
                balanced=False
            else:
                top=s.pop()
                if not is_match(top,paran):
                    balanced=False
        index+=1

    if s.is_empty() and balanced:
        return True
    else:
        return False


print(is_balanced("()"))
print(is_balanced("({[({()})]})"))
print(is_balanced("("))
print(is_balanced(""))
print(is_balanced("([]"))
print(is_balanced("([{)"))
