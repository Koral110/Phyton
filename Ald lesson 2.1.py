while True:
        s = input("Ведите тип операции иии 0 для выхода из программы (+,-,*,/): ")
        if s == '0': break
        if s in ('+','-','*','/'):
                x = float(input("x="))
                y = float(input("y="))
                if s == '+':
                        print("%.2f" % (x+y))
                elif s == '-':
                        print("%.2f" % (x-y))
                elif s == '*':
                        print("%.2f" % (x*y))
                elif s == '/':
                        if y != 0:
                                print("%.2f" % (x/y))
                        else:
                                print("На ноль делить нельзя!!!")
        else:
                print("Неверный знак операции!!!")