# Advent of Code: Python solutions
https://adventofcode.com/2020

## Lessons learned:
* assignment 2 - You can use the bitwise operator `^` to do a xor in python: 
```python
if bool(a) ^ bool(b):
```
* assignment 2 - Immediately assign split values to their variables for efficiency.
```python 
n1, n2, letter, x, passw = re.split('[-:\s]', line)
```
* assignment 3 - If you're using the `x` coordinate to calculate the `y` coordinate by, don't forget to divide y over x's step size `xn` to make them independent again (`x*yn/xn`). Though it's probably better never to make the two depend on each other in the first place.
```python    
for x in range(0, len(trees), xn):
    y = int(x*yn/xn) % len(trees[0])
```
* assignment 4 - This is a way to convert a list of lists with value pairs to a list of dictionaries, using list comprehension.
```python
    dict_list = [dict([(value_pair.split(":")) for value_pair in list]) for list in llist]
```
* assignment 4 - If you remove values from the list you're looping over the length will change and values will be skipped. Instead make a copy() of it and remove the values from there.
```python
list = [1,4,7,7,2,3,4,5]; copied_list = list.copy(); test = [3,4]  # Make three lists
[copied_list.remove(item) for item in list if item in test]        # Remove items in test from copied_list
```
* assignment 6 - This is how you sort a string.
```python
sorted_string = ''.join(sorted(unsorted_string))
```
* assignment 7 - In Regex look before a certain string with the `?=` positive lookahead and find all occurences with `re.findall()`.
```python
re.findall(r'(\d+)*\s*(\w+\s\w+)(?=\sbag)', line)
```
* assignment 7 - Recursion is very powerful, looks very clean, but it's really difficult to grasp.
```python
def find_bags(color): 
    teller = 0
    for bag in bags_dict[color]:
        teller += bags_dict[color][bag] + find_bags(bag) * bags_dict[color][bag]  # Recursively sum the contents of the bag
    return teller
```
