text = open("subInfo.txt").read()


def findCount(sub):
    count = 0
    terms = open(sub).readlines()
    terms = [t.strip().lower() for t in terms]
    for t in terms:
        if t in text:
            count += 1
    return count


subArr = []
subArr.append((findCount("biology_terms.txt"), "biology_terms.txt"))
subArr.append((findCount("chemistry_terms.txt"), "chemistry_terms.txt"))
subArr.append((findCount("History_terms.txt"), "History_terms.txt"))
subArr.append((findCount("physics_terms.txt"), "physics_terms.txt"))
subArr.append((findCount("math_terms.txt"), "math_terms.txt"))
subArr = sorted(subArr)[::-1]
print(subArr)
print(subArr[0][1])
