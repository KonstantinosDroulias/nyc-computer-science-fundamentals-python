scores = {
    'a': 2,
    'b': 1,
    'c' : 6,
    'd': 0,
}

ordered_score = list(sorted(scores.items(),
                            key=lambda item: item[1],
                            reverse=True))

for i in range(3): 
    print(ordered_score[i])
