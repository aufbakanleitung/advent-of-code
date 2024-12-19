# --- Day 6a: Custom Customs ---
with open('input/aoc06_input.txt') as f:
    content = f.read().split('\n\n')
    forms = [set(line) for line in content]
    [sett.discard('\n') for sett in forms]

# For each group, count the number of questions to which anyone answered "yes".
# What is the sum of those counts?
form_sum = 0
for form in forms:
    form_sum += len(form)
print(form_sum)
