import collections

def split(s):
    stack = []
    side = []
    for i in range(len(s)):
        current = s[i]
        if (i - 1) >= 0:
            prev = s[i - 1]
        else:
            prev = None
        if (i + 1) <= len(s) - 1:
            next = s[i + 1]
        else:
            next = None
        if current == '#' and (prev is None or prev == '.'):
            side = list()
            side.append(i)
        if current == '#' and (next is None or next == '.'):
            side.append(i + 1)
            stack.append(side)
    return stack


def size(part):
    return part[1] - part[0]


def is_square(board):
    parts = []
    for line in board:
        p = split(line)
        if len(p) > 0:
            parts += p
    return parts.count(parts[0]) == size(parts[0]) and len(parts) == size(parts[0])


def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        board = list()
        for j in range(N):
            line = input()
            board.append(line)
        result = is_square(board)
        if result:
            answer = 'YES'
        else:
            answer = 'NO'
        print("Case #{0}: {1}".format(i + 1, answer))


if __name__ == '__main__':
    main()