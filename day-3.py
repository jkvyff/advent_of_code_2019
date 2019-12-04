with open('day-3-input.txt', 'r') as text:
    input = [x.split(',') for x in text.read().strip().split('\n')]

def wireHash(wire):
    wirePath = {}
    x, y, count = 0, 0, 0
    directions =  {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
    for part in wire:
        for _ in range(int(part[1:])):
            offset = directions[part[0]]
            x += offset[0]
            y += offset[1]
            count += 1
            wirePath[(x, y)] = count
    return wirePath

first, second = [wireHash(input[0]), wireHash(input[1])]
intersect = first.keys() & second.keys()

closestIntersect = min([point for point in intersect], key=lambda x: abs(x[0]) + abs(x[1]))
manhattan = abs(closestIntersect[0]) + abs(closestIntersect[1])

shortestPathIntersect = min(intersect, key=lambda x: first[x] + second[x])
steps = first[shortestPathIntersect] + second[shortestPathIntersect]

print("Part One:", manhattan)
print("Part Two:", steps)