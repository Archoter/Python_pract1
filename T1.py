import math

def func(x:float, e:float) -> float:
    k = 1
    z = 1
    while k <= e:
        z = z * math.pow((1 - ( x / ( k * math.pi ))), 2)
        k = k + 1
    save_in_file(x, e, x * z)
    return x * z

def get_inputX() -> float:
    while True:
        try:
            return float(input("x = "))
        except Valuefloat as exc:
            print("Not X")

def get_inputE() -> float:
    while True:
        try:
            return float(input("e = "))
        except Valuefloat as exc:
            print("Not E")

def print_output(y:float):
    print(f"func = {y}")

def save_in_file(x:float, e:float, p:float):
    file = open("h.txt", "a+")
    file.write("x = " + str(x) + ", e = " + str(int(e)) + ", func = " + str(p) + "\n")
    file.close()

def read_file():
    file = open("h.txt", "r+")
    print(file.read())
    file.close()
    
def main():
    file = open("h.txt", "w+")
    file.close()
    while True:
        print("1. Выполнение функции")
        print("2. История")
        print("0. Выход")
        cmd = input("Выберите пункт: ")
        if cmd == "1":
            P = func (get_inputX(), get_inputE())
            print_output(P)
        elif cmd == "2":
            read_file()
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")

if __name__ == "__main__":
    main()
