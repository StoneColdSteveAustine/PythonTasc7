def rhythm(str):
    str = str.split()
    list = []
    for frase in str:
        result = 0
        for i in frase:
            if i in "аеёиоуыэюя":
                result += 1
        list.append(result)
    return len(list) == list.count(list[0])
print("Введите стихотворение")
str = input()
if rhythm(str):
    print("Парам пам-пам")
else:
    print("Пам парам")
