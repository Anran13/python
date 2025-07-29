from self.tools import caculate_bmi, get_state


def main():
    height:int = int(input("請輸入身高(cm):"))
    weight:int = int(input("請輸入體重(kg):"))

    bmi = caculate_bmi(height, weight)

    print(bmi)
    print(get_state(bmi))


if __name__ == '__main__':
    main()