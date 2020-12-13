from multiprocessing import Process

from aoc2020.util import get_input_day13


def route_complete(time, buses):
    results = dict()
    for bus in buses:
        try:
            _t = int(time)
            _b = int(bus)
        except ValueError:
            continue
        pct_complete = (_t % _b) / _b
        results[_b] = pct_complete
    return results


def next_bus(time, buses):
    t = int(time)
    while True:
        for bus in buses:
            try:
                b = int(bus)
            except ValueError:
                continue
            if t % b == 0:
                return (b, t)
        t += 1


def solve_part1(earliest, buses):
    bus, time = next_bus(earliest, buses)
    return bus * (time - int(earliest))


def validate_subsequent_departs(time, buses):
    for index, bus in buses:
        if (time + index) % bus != 0:
            return False
    return True


def check_range(start_time, end_time, buses):
    # print(f"checking {start_time}:{end_time}")
    time = start_time
    while time <= end_time:
        for index, bus in buses:
            if index == 0 and time % bus == 0:
                if validate_subsequent_departs(time, buses):
                    print(f"FOUND {time}")
                    return time
        time += 1


def range_generator(start, end):
    step = end
    while True:
        yield range(start, end)
        start = end
        end += step


def solve_part2(start_time, buses):
    indexed_buses = list()
    for index, bus in enumerate(buses):
        try:
            bus = int(bus)
        except ValueError:
            continue
        indexed_buses.append((index, bus))
    while True:
        result = validate_subsequent_departs(start_time, indexed_buses)
        if result:
            return start_time
        start_time += 1
    # num_procs = 12
    # step = 100000
    # my_gen = range_generator(start_time, step)
    # while True:
    #    if start_time % 100000000 == 0:
    #        print(f"checking {start_time}")
    #    procs = list()
    #    for i in range(num_procs):
    #        start = start_time + (i * step)
    #        end = start_time + (i * step) + step
    #        p = Process(target=check_range, args=(start, end, indexed_buses))
    #        procs.append(p)
    #    [p.start() for p in procs]
    #    results = [p.join() for p in procs]
    #    if any(results):
    #        return results
    #    start_time = start_time + (step * num_procs)


if __name__ == "__main__":  # pragma: no cover
    earliest, buses = get_input_day13("aoc2020/day13/input")
    print(solve_part1(earliest, buses))
    print(solve_part2(100000000000000, buses))
