participants = int(4)
scores = "57 57 -57 57"
scores = list(map(int, scores.split()))


def runner_up_fn(input_scores):
    first, second = min(input_scores), min(input_scores)
    for i in sorted(input_scores):
        if i in input_scores:
            if i > first:
                first, second = i, first
            elif first > i > second:
                second = i
    return second


print(runner_up_fn(scores))
