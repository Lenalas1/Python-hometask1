name = input ( "Введите ваше имя ")
password = input ("Введите ваш пароль ")
age = int(input( "Введите ваш возраст "))
print ( "Ваши данные для входа: ", name, password, age)


a = int(input ("введите время в секундах: "))
hours = a//3600
minutes = ( a - hours*3600)//60
seconds = ( a - hours*3600)-minutes*60
print(f'{hours}:{minutes}:{seconds}')


s = int(input( "Ведите целое число: "))
print (s + int(str(s)*2) + int(str(s)*3))

a = int( input ("Введите выручку фирмы: "))
b = int( input ("Введите издержки фирмы: "))
if a > b:
    s = a - b
    m = s/a
    print ("Финансовый резудьтат - прибыль,ee величина ", s)
    print("Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)")
    print ("Рентабельность выручки", m)
    v = int(input("ВВедите количество сотрудников: "))
    w = s/v
    print("Прибыль фирмы в расчете на одного сотрудника ", w)

elif a < b:
    print ("Издержки больше выручки")

