import re

line = "Wk12: A.St.Brown (RB, IND) 22 car, 143 yds"
pattern = r"Wk(\d+): ([\w.]+) \(([A-Z]+), ([A-Z]+)\) (\d+) car, (\d+) yds, (\d+) TD"
match = re.search(pattern, line)
print(match.groups())




