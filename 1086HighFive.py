def highFive(points = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]):
    students = set()
    for point in points:
        students.add(point[0])

    scores = {}
    for point in points:
        if point[0] in scores.keys():
            scores[point[0]] += point[1]
        else:
            scores[point[0]] = point[1]

    print(scores)

    res = []
    for k, v in scores.items():
        res.append([k,scores[k]/5])
    print(res)


highFive()