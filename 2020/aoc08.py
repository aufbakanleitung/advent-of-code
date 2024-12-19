# --- Day 8: Handheld Halting ---
content = [line.rstrip('\n') for line in open("input/aoc08_example.txt")]

instructions = []
for line in content:
    operation, argument = line.split()
    instructions.append([operation, int(argument), False])  # Add is_run boolean

print(instructions)

# Immediately before any instruction is executed a second time, what value is in the accumulator?
acc = 0
loc = 0

def read_instruction(inst):
    global acc
    global loc
    # print(f"input: {inst}")
    if inst[0] == "nop":
        inst[2] = True
        loc += 1
    if inst[0] == "acc":
        acc += inst[1]
        inst[2] = True
        loc += 1
    if inst[0] == 'jmp':
        inst[2] = True
        loc += inst[1]


def test_code(instructions):
    while instructions[loc][2] is False:
        read_instruction(instructions[loc])
        print(f"{instructions[loc][0]}, loc: {loc}, acc: {acc}")


test_code(instructions)
# nop +0  | 1
# acc +1  | 2, 8(!)
# jmp +4  | 3
# acc +3  | 6
# jmp -3  | 7
# acc -99 |
# acc +1  | 4
# jmp -4  | 5
# acc +6  |

