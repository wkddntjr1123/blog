from collections import defaultdict
import re

html = input()
re_div = re.compile(r'"[a-zA-Z_ 0-9]*"')
re_p1 = re.compile(r"<p>")
re_p2 = re.compile(r"</p>")
divs = []
ps = []
table = defaultdict(list)
for item in re_div.finditer(html):
    table[item.start()].append("title : " + html[item.start() + 1 : item.end() - 1])
for item in re_p1.finditer(html):
    ps.append([item.start()])
for i, item in enumerate(re_p2.finditer(html)):
    ps[i].append(item.end())

sorted_key = sorted(table.keys())
for start, end in ps:
    for k in sorted_key:
        if end < k:
            break
        selected = k
    # 문단 처리
    table[selected].append(re.sub("[ ]+", " ", re.sub(r"<[a-z /]*>", "", html[start:end]).strip()))

for k in sorted_key:
    print(*table[k], sep="\n")
