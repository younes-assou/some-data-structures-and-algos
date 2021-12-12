# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    opening_brackets_index = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            opening_brackets_index.append(i+1)

        if next in ")]}":
            # Process closing bracket, write your code here
            try:
                last = opening_brackets_stack.pop()
                opening_brackets_index.pop()
            except: return i+1
            if not are_matching(last,next):
                return i+1
    if len(opening_brackets_stack)==0: return 'Success'
    else: return opening_brackets_index[-1]

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
