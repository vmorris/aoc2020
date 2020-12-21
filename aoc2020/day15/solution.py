from aoc2020.util import list_rindex


def speak_number(number, data):
    print(f"initial numbers: {data}")
    print(f"spoken number {number}")
    turn = 1
    spoken = dict()
    last_spoken = data[0]
    while turn <= number:
        print(f"turn {turn}; spoken {spoken}")
        if turn <= len(data):
            to_speak = data[turn - 1]
            spoken[to_speak] = (turn, None)
        else:
            last_turn, prev_turn = spoken[last_spoken]
            print(
                f"\tlast spoken: {last_spoken}; last said turn {last_turn}; previously on turn {prev_turn}"
            )
            if prev_turn is None:
                to_speak = 0
                try:
                    to_speak_last_turn = spoken[to_speak][0]
                except KeyError:
                    to_speak_last_turn = None
                print(f"\t{last_spoken} not said before last turn")
                spoken[to_speak] = (turn, to_speak_last_turn)
            else:
                print(f"\t{to_speak}")
                to_speak = turn - prev_turn - 1
                spoken[to_speak] = (turn, last_turn)
            # print(
            #    f"\t{last_spoken} was previously spoken on turn {next2last_spoken_index}"
            # )
            #    to_speak = turn - prev_spoken_index - 1
            # print(f"\tsay {to_say}")
            #    spoken[to_speak] = turn
        print(f"\tsay {to_speak}")
        last_spoken = to_speak
        turn += 1
    # print(f"{last_spoken}")
    return last_spoken


def solve_part1(data):
    return speak_number(2020, data)


def solve_part2(data):
    return speak_number(30000000, data)


if __name__ == "__main__":  # pragma: no cover
    data = [8, 0, 17, 4, 1, 12]
    print(solve_part1(data))
    print(solve_part2(data))
