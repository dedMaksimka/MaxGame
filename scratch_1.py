def dist(dot1, dot2):
    return ((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2) ** 0.5


def cos(a, b, c):
    return (b ** 2 + a ** 2 - c ** 2) / (2 * b * a)


def count(dotA, dotB, dotC):
    a = dist(dotA, dotB)
    b = dist(dotB, dotC)
    c = dist(dotC, dotA)
    cosa = cos(a, b, c)
    cosb = cos(b, c, a)
    if cosa <= 0 or cosb <= 0 or abs(cosa) == 1 or abs(cosb) == 1:
        return min(a, c)
    else:
        return a * (1 - cosa ** 2) ** 0.5


coors = []
for _ in range(int(input())):
    coors.append([int(i) for i in input().split()])
dot5g = [int(i) for i in input().split()]

minR = count(dot5g, coors[0], coors[-1])
for i in range(len(coors) - 1):
    t = count(dot5g, coors[i], coors[i + 1])
    # print(coors[i], coors[i + 1], t)
    minR = min(minR, count(dot5g, coors[i], coors[i + 1]))
print(f"{minR:.3f}")
