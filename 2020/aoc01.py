# Day 1: Report Repair
# https://adventofcode.com/2020/day/1
import math

expense_example = [1721, 979, 366, 299, 675, 1456]
expense_report = [int(line.rstrip('\n')) for line in open("input/aoc01_input.txt")]

def find_twosum(report, sumnr=2020):
    nr_list = []
    for ex in report:
        for ex2 in report:
            if ex + ex2 == sumnr:
                nr_list.append(ex)
                nr_list.append(ex2)
        report.remove(ex)
    return math.prod(nr_list)

# print(find_twosum(expense_report))


def find_threesum(report, sumnr=2020):
    nr_list = set()
    for ex in report:
        for ex2 in report:
            for ex3 in report:
                if ex + ex2 + ex3 == sumnr:
                    nr_list.add(ex)
                    nr_list.add(ex2)
                    nr_list.add(ex3)
        report.remove(ex)
    print(nr_list)
    return math.prod(nr_list)

print(find_threesum(expense_report))
