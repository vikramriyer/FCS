#!/usr/bin/python

OUTPUT, STACK = [], []
precedence = {
                '+': 1, 
                '-': 1, 
                '*': 2, 
                '/': 2, 
                '^': 3
              }

def is_operand(char):
  if char.isalpha():
    return True
  return False

def check_precedence(char):
  '''
    check top and 
    return char if char has higher precedence
    return top
  '''
  operator = ""

  if STACK[-1] == '(':
    STACK.append(char)
  if precedence[STACK[-1]] >= precedence[char]:
    operator = STACK.pop()
    STACK.append(char)
  else:
    STACK.append(char)

  return operator

def is_empty():
  if len(STACK) == 0:
    return True
  return False

def calc_infix_to_postfix(expr):
  '''
    if the char is a operand i.e. an alphabet, then append to the output list
    if the char is a '(' 
    if the char is a '('
    else which means the char is a operator, we compare with top and check 
    for precedence and append to the output list and pop the element
  '''

  for char in expr:
    if is_operand(char):
      OUTPUT.append(char)
    elif char == '(':
      STACK.append(char)
    elif char == ')':
      while not is_empty() and STACK[-1] != '(':
        temp = STACK.pop()
        OUTPUT.append(temp)

      if (not is_empty() and STACK[-1] == '('):
        print "Error in expression!"
        exit(0)
    else:
      if not is_empty():
        OUTPUT.append(check_precedence(char))
      else:
        STACK.append(char)

  while not is_empty():
    OUTPUT.append(STACK.pop())

def main():
  calc_infix_to_postfix('a*(b-c)')
  evaluate_postfix()

if __name__ == '__main__':
  main()
  OUTPUT = filter(None, OUTPUT)
  print OUTPUT
  if ['a','b','c','*','+'] == OUTPUT:
    print "The postfix conversion is successful."
    print "Postfix Expression: {}".format(OUTPUT)
  else:
    print "Error in the covnersion."


'''
Stage 1: works for a+b*c and simple expressions without '(' or ')' => done
Stage 2: should work for associativity, now works only for precedence => done
Stage 3: should work for 'Stage 1' cases as well => not done
'''