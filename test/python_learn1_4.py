# tools.py --> we define the module including self-defined functions
import tools

def main():
    height:int = int(input("請輸入身高(cm):"))
    weight:int = int(input("請輸入體重(kg):"))

    bmi = tools.caculate_bmi(height, weight)

    print(bmi)
    print(tools.get_state(bmi))


if __name__ == '__main__':
    main()

# ask Gemini to modify into window version:
# enter: @python_learn1_4.py This is my bmi python code. I'd like to modifiy it into a window surface for users. Please use the tkinter package
# the modified version is in python_learn_1_5.py