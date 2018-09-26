# study-python-1
Fist import python project from PyCharm.

Repl.it: [https://repl.it/@mrcutejacky/study-python-1]

### 重點整理
1. 宣告函式必須在前，使用在後。
2. 字串相加之前，必須先把其他型別轉成字串才能相加。

### 程式碼
```python
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
print("您的BMI為: " + str(bmi))

# 把bmi四捨五入到小數點第二位，同時轉成str印出來
print("您的BMI為(四捨五入到小數第二位): " + str(round(bmi, 2)))
```

### 結果
```console
這是一個BMI程式
請輸入身高(cm):  175
請輸入體重(kg):  80
您的BMI為: 26.122448979591837
您的BMI為(四捨五入到小數第二位): 26.12
```
