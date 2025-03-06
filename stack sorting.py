def sort_stack(stack):
    tmp_stack = []
    while stack:
        num = stack.pop()
        while tmp_stack and tmp_stack[-1] < num:
            stack.append(tmp_stack[-1])
            tmp_stack.pop()

        tmp_stack.append(num)