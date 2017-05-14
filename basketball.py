def split_to_commands(players):
    sorted_players = sorted(players, key=lambda item: (item[1], item[2]), reverse=True)
    return [[player[0], pos + 1, 0] for pos, player in enumerate(sorted_players[::2])], \
           [[player[0], pos + 1, 0] for pos, player in enumerate(sorted_players[1::2])]


def exchange(on_field, on_bench):
    for player in on_field:
        player[2] += 1
    on_field = sorted(on_field, key=lambda item: (item[2], item[1]))
    on_field, temp_field = on_field[:-1], on_field[-1:]
    on_bench, temp_bench = on_bench[1:], on_bench[:1]
    on_field += temp_bench
    on_bench += temp_field
    on_bench = sorted(on_bench, key=lambda item: (item[2], item[1]))
    return on_field, on_bench


def play(M, P, players):
    first_command, second_command = split_to_commands(players)
    first_size = len(first_command)
    second_size = len(second_command)

    first_field = first_command[:P]
    second_field = second_command[:P]

    first_bench = first_command[P:]
    second_bench = second_command[P:]

    for i in range(M):
        if first_size > P:
            first_field, first_bench = exchange(first_field, first_bench)
        if second_size > P:
            second_field, second_bench = exchange(second_field, second_bench)

    return ' '.join(sorted([player[0] for player in first_field + second_field]))


def main():
    T = int(input())
    for t in range(T):
        N, M, P = [int(num) for num in input().split()]
        players = []
        for p in range(N):
            line = input().split()
            name = line[0]
            rate, height = int(line[1]), int(line[2])
            players.append((name, rate, height))
        print('Case #{0}: {1}'.format(t + 1, play(M, P, players)))


if __name__ == '__main__':
    main()