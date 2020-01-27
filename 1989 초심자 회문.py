## reversed 사용
T = int(input())
for i in range(T):
    word = list(map(str, input()))
    if 3 <= len(word) <= 10:
        reverse_word = list(reversed(word))
        print(reverse_word)
        if reverse_word == word:
            result = 1
        else:
            result = 0
    print(f"#{i+1} {result}")

# reversed 사용하지 않고
T = int(input())
for i in range(T):
    word = list(map(str, input()))
    if 3 <= len(word) <= 10:
        reverse_word = list(range(len(word)))
        for j in range(len(word)):
            reverse_word[-1-j] = word[j]
        if reverse_word == word:
            result = 1
        else:
            result = 0
    print(f"#{i+1} {result}")
