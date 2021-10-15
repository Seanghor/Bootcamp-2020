# My code
def grade(score):
    if score in range(90, 101):
        rank = 'A'
    elif score in range(80, 90):
        rank = 'B'
    elif score in range(70, 80):
        rank = 'C'
    elif score in range(60, 70):
        rank = 'D'
    elif score <= 0:
        rank = 'F'
    else:
        rank = 'invalid rank'

    return rank
print(grade(100))

result = grade(100)
print(type(result))


# China code
