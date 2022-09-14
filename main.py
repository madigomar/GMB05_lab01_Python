import math

print('Лабораторная работа №1')
print('Гомар Мади ВТиП-302')

def main():
    try:
        a = float(input("Введите A="))
        b = float(input("Введите B="))
        x = float(input("Введите X="))
        try:
            if x >= 8:
                y = (pow(a,2) + 4 * pow(x,2) + pow(b,2))/2*x
                print("Y = ",y)
            else:
                y = pow(a,2) - 2 * pow(x,2)
                print("Y = ", y)
        except:
            print("Нет решения!")
    except:
        print("Неверные входные данные!")
    input("Нажмите Enter для выхода")

if __name__ == '__main__':
    main()