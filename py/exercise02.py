mark = ["Spade", "Heart", "Diamond", "Clover"]

def card(num):
    if num % 13 == 0:
        return "A"
    elif num % 13 == 10:
        return "J"
    elif num % 13 == 11:
        return "Q"
    elif num % 13 == 12:
        return "K"
    else:
        return num % 13 + 1

for i in range(52):
    print(i + 1, mark[i // 13], card(i))