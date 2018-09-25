print("這是一個BMI程式")

# 宣告一個bmi函式，計算bmi，並回傳結果。
# height 單位為cm
# weight 單位為kg
def bmi_generator(height, weight):
    return weight / pow(height / 100, 2)

# 取得使用者輸入的參數，並將string轉為float
height = float(input("請輸入身高(cm): "))
weight = float(input("請輸入體重(kg): "))

# 呼叫bmi來計算BMI的值
bmi = bmi_generator(height, weight)

# 把bmi轉成str，並印出來
print("您的BMI為" + str(bmi))