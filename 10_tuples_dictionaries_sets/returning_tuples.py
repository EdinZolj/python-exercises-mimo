# Tuples are useful because they allow us to return multiple values from a function, like the highest and lowest scores from a list.

def get_score_data(scores_list):
    highest_score = max(scores_list)
    lowest_score = min(scores_list)
    return highest_score, lowest_score

score = [12, 25, 100, 30]
data = get_score_data(score)
print(data)


def get_score_data(scores_list):
    highest_score = max(scores_list)
    lowest_score = min(scores_list)
    return highest_score, lowest_score

score = [12, 25, 100, 30]
data = get_score_data(score)

highest = data[0]
smallest = data[1]

print(f"smallest score: {smallest}")
print(f"highest score: {highest}")
