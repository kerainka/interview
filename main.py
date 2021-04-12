class Stack:
    stack_list = []

    def empty(self):
        return len(self.stack_list) == 0

    def push(self, element):
        self.stack_list.append(element)

    def pop(self):
        return self.stack_list.pop()

    def peek(self):
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)


def is_pair(a, b):
    if a == '{' and b == '}':
        return True
    if a == '(' and b == ')':
        return True
    if a == '[' and b == ']':
        return True
    return False


def is_balanced(str_input):
    stack = Stack()
    for si in str_input:
        if si == '{' or si == '(' or si == '[':
            stack.push(si)
        else:
            if stack.empty():
                return False
            last = stack.pop()
            if not is_pair(last, si):
                return False
    return stack.empty()


s = input('Введите последовательность: ')

if is_balanced(s):
    print('Сбалансированно')
else:
    print('Несбалансированно')
