import self

def main():
    height:int = int(input("請輸入身高(cm):"))
    weight:int = int(input("請輸入體重(kg):"))

    bmi = self.tools.calculate_bmi(height, weight)

    print(bmi)
    print(self.tools.get_state(bmi))


if __name__ == '__main__':
    main()

# self.tools.test()