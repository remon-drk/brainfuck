import sys

MEM_SIZE = 30000

def execute(bf_code):
    idx = 0
    ptr = 0
    mem = [0 for i in range(MEM_SIZE)]

    while idx < len(bf_code):
        char = bf_code[idx]
        if char == '+': mem[ptr] = (mem[ptr] +   1) % 256
        if char == '-': mem[ptr] = (mem[ptr] + 255) % 256
        if char == '>': ptr = (ptr +            1) % MEM_SIZE
        if char == '<': ptr = (ptr + MEM_SIZE - 1) % MEM_SIZE
        if char == '.': print(chr(mem[ptr]), end='')
        if char == ',':
            mem[ptr] = ord((input('\n>> in (first char): ') + 'Ā = 256')[0]) % 256
        if char == '[' and not mem[ptr]:
            depth = 1
            while depth and idx + 1 < len(bf_code):
                idx += 1
                if bf_code[idx] == '[': depth += 1
                if bf_code[idx] == ']': depth -= 1
        if char == ']' and mem[ptr]:
            depth = 1
            while depth and idx - 1 >= 0:
                idx -= 1
                if bf_code[idx] == ']': depth += 1
                if bf_code[idx] == '[': depth -= 1
        idx += 1

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        input_code = f.read()
    execute(input_code)