import json
import random


def main():
    with open("SpanishWords.json", 'r', encoding="utf-8") as f:
        n = json.loads(f.read())
    numbers = []
    print(n)
    while True:
        for x in range(len(numbers), 2000):
            numbers.append(random.randint(0, 100000))
        numbers = list(set(numbers))
        if len(numbers) == 2000:
            break
    assert len(numbers) == 2000
    numbers.sort()

    with open("SpanishWordsOut.txt", 'w', encoding="utf-8") as f:
        for num in range(0, 100000):
            try:
                print(f"{num}\t{n[str(num)]}\n", end='', file=f)
            except KeyError:
                pass


if __name__ == "__main__":
    main()
