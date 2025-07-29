from self.tools import calculate_bmi as a1
from self.tools import get_state as a2

def main():
    height:int = int(input("請輸入身高(cm):"))
    weight:int = int(input("請輸入體重(kg):"))

    bmi = a1(height, weight)

    print(bmi)
    print(a2(bmi))


if __name__ == '__main__':
    main()