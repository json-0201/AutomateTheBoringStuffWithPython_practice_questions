'''
Write a program to find out how often a streak of six heads or a streak
of six tails comes up in a randomly generated list of heads and tails.
'''
import random

def main():
    streak_num = 0
    for i in range(10000):
        flip_list = flip(100)
        if streak(flip_list):
            streak_num += 1

    print(f"Chance of streak: {(streak_num / 100):.2f}%")   #f"{num:.2f}" -> 2 decimals
    return 0

# Flip a coin "n" times and generate a list
def flip(n: int) -> list:
    result = []

    for i in range(n):
        if random.randint(0, 1) == 1:
            result.append("H")
        else:
            result.append("T")
    
    return result


# Check if a list contains 6 "H" or "T" in a row
def streak(list_val: list) -> bool:
    string_val = "".join(list_val)  # "text".join(list) -> convert list to string
    if "HHHHHH" in string_val or "TTTTTT" in string_val:
        return True
    else:
        return False


if __name__ == "__main__":
    main()