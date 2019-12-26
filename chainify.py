dyads = "*+-/%@"
monads = list(map(chr, range(ord("A"), ord("Z") + 1)))
nilads = "1234567890"

source = input()[::-1]
arities = []
for char in source:
    if char in dyads:
        arities.append((2, char))

    elif char in monads:
        arities.append((1, char))

    else:
        arities.append((0, char))

exprs = []
expr = []
patterns = ["020", "021", "022", "02", "10", "11", "12", "20", "21", "22",
            "102", "110", "111", "112", "120", "121", "122",
            "202", "210", "211", "212", "220", "221", "222"]
pattern = ""
while len(arities):
    if pattern in patterns and pattern + str(arities[-1][0]) not in patterns:
        exprs += [pattern, expr]
        expr = []
        pattern = ""
        
    pattern += str(arities[-1][0])
    expr.append(arities[-1][1])
    arities.pop()

if expr and pattern in patterns:
    exprs += [pattern, expr]
    expr = []
    pattern = ""

print(exprs)