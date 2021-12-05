import re
# №2 ^[a-zA-Z]+([-]|[.]|[_]|[a-zA-Z]*)*[@][a-zA-Z]+([-]|[.]|[_]|[a-zA-Z]*)*[.][a-zA-Z]+$
# №5 ^(http://|https://)  [a-z]+[.][a-z]+
text = input("Введите номер задания (2,5,8): ")
if text == '2' or text == '8':
    if text == '2':
        a = "^[a-zA-Z]+([-]|[.]|[_]|[a-zA-Z]*)*[@][a-zA-Z]+([-]|[.]|[_]|[a-zA-Z]*)*[.][a-zA-Z]+$"
    else:
        a = "[0-9]{2}[.][0-9]{2}[.][0-9]{4}"
    while(True):
        inp = (input("\nВведите значение для проверки или end для завершения: "))
        if (inp == "end"):
            break
        result = re.match(a, inp)
        print(result[0] + " выражение подходит" if result else inp + " выражение не подходит")
else:
    a = "^(http://|https://)"
    while(True):
        inp = (input("Введите http ссылку для проверки или end для завершения: "))
        if (inp == "end"):
            break
        inp2 = re.split(a, inp)
        if inp2[1] == 'http://' or inp2[0] == 'https://':
            result = re.match("^[a-z]+[.][a-z]+", inp2[2])
            print("Ссылка подходит: " + result[0])
        else:
            print("Ссылка не подходит")