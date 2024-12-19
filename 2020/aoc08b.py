# --- Day 8: Handheld Halting ---
content = [line.rstrip('\n') for line in open("input/aoc08_example.txt")]

instructions = []
for line in content:
    operation, argument = line.split()
    instructions.append([operation, int(argument), False])  # Add is_run boolean
print("first inst:", instructions)
# Immediately before any instruction is executed a second time, what value is in the accumulator?
acc = 0
loc = 0

def read_instruction(inst):
    global acc, loc
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
        if loc == len(instructions):
            print(f"Success!: {instructions[loc][0]}, loc: {loc}, acc: {acc}")
            break

fix_instructions = [['nop', 0, True], ['acc', 1, False], ['jmp', 4, False], ['acc', 3, False], ['jmp', -3, False], ['acc', -99, False], ['acc', 1, False], ['nop', -4, False], ['acc', 6, False]]

test_code(fix_instructions)

# Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
# What is the value of the accumulator after the program terminates?
def flip_inst(inst):
    if inst[0] == "jmp":
        inst[0] = "nop"
    elif inst[0] == "nop":
        inst[0] = "jmp"
    return inst

# i=0
# while loc is not len(instructions)+2:
#     if i != 0:
#         instructions[i-1] = flip_inst(instructions[i-1])
#     instructions[i] = flip_inst(instructions[i])
#     print("flipped: ", instructions)
#     test_code(instructions)
#     i += 1

# nop +0  | 1
# acc +1  | 2, 8(!)
# jmp +4  | 3
# acc +3  | 6
# jmp -3  | 7
# acc -99 |
# acc +1  | 4
# jmp -4  | 5
# acc +6  |