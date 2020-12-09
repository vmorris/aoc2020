from aoc2020.util import get_input


class Machine:
    def __init__(self, change=None):
        self.program_counter = 0
        self.accumulator = 0
        self.instruction_register = None
        self.memory = list()
        self.history = list()
        self.loop_detected = False
        self.change = change
        self.running = False

    def run(self):
        self.running = True
        while True:
            try:
                self.fetch()
            except IndexError:
                self.running = False
                return self.accumulator
            if not self.loop_detected:
                self.execute()
            else:
                break
        if self.change is None:
            return self.accumulator

    def load_program(self, program):
        self.memory = program

    def fetch(self):
        if self.program_counter in self.history:
            self.loop_detected = True
        self.instruction_register = self.memory[self.program_counter]

    def execute(self):
        self.history.append(self.program_counter)
        opcode, operand = self.instruction_register.split(" ")
        operand = int(operand)
        if self.change == self.program_counter:
            if opcode == "nop":
                opcode = "jmp"
            elif opcode == "jmp":
                opcode = "nop"
        if opcode == "nop":
            self.nop()
        elif opcode == "acc":
            self.acc(operand)
        elif opcode == "jmp":
            self.jmp(operand)
        else:
            raise NotImplementedError(opcode)

    def nop(self):
        self.program_counter += 1

    def acc(self, value):
        self.accumulator += value
        self.program_counter += 1

    def jmp(self, value):
        self.program_counter += value


def solve_part1(entries):
    machine = Machine()
    machine.load_program(entries)
    result = machine.run()
    return result


def solve_part2(entries):
    for i in range(len(entries)):
        machine = Machine(change=i)
        machine.load_program(entries)
        result = machine.run()
        if not machine.running:
            return result


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2020/day08/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
