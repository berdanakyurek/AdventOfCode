def find_middle(lis):
    return lis[len(lis) // 2]


def is_valid(lis, rules):
    rev = lis[::-1]

    for rule in rules:
        try:
            index0 = len(lis) - 1 - rev.index(rule[0])
            index1 = lis.index(rule[1])
        except ValueError:
            continue
        if index0 > index1:
            return False

    return True


def correct_order(lis, rules):
    graph = {}
    for rule in rules:
        if rule[0] not in lis:
            continue
        if rule[1] not in lis:
            continue

        if graph.get(rule[1]):
            graph[rule[1]].append(rule)
        else:
            graph[rule[1]] = [rule]

        if not graph.get(rule[0]):
            graph[rule[0]] = []

    result = []

    while len(graph) > 0:
        for key in list(graph.keys()):
            if len(graph[key]) == 0:
                result.append(key)
                del graph[key]
                for key2 in graph.keys():
                    for rule in graph[key2]:
                        if rule[0] == key:
                            graph[key2].remove(rule)

    return result



lines = open("rules.txt").readlines()
rules = []
for line in lines:
    a, b = line.strip().split('|')
    rules.append((int(a), int(b)))

lines = open("lists.txt").readlines()
lists = []
for line in lines:
    lists.append(list(map(int, line.strip().split(','))))

result = 0
result2 = 0
for lis in lists:
    if is_valid(lis, rules):
        result += find_middle(lis)
    else:
        result2 += find_middle(correct_order(lis, rules))

print(result)
print(result2)
