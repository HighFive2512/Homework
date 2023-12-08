import sys

with open(sys.argv[1], 'r') as file:
    advent_task_content = file.read().strip()
    for eachline in advent_task_content.split('\n'):
        print(eachline)
