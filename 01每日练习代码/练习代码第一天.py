"""第一天学习Python的练习"""
# name = "马晟原"
# age = 25
# address = "昭通"
# area = "AI智能体"
# print(f"我叫{name},今年{age},居住在{address},正学习Python并向{area}方向努力!")

# cm = input("请输入厘米数：")
# cm = float(cm)
# m = cm * 0.01
# print(f"{cm}厘米 = {m:.2f}米")

# score = input("请输入你的考试分数：")
# score = float(score)
# if score > 90:
#     grade = "优秀"
# elif score >= 80:
#     grade = "良好"
# elif score >=60:
#     grade = "及格"
# else:
#     grade = "不及格"
# print(f"你的分数为{score},成绩等级为{grade}")

# name = "马晟原"
# age = 25
# address = "昭通"
# hobby = "围棋"
# print(f"我的名字是{name},今年{age}岁了，家乡在{address},最大的兴趣爱好是{hobby}")

# g = input("请输入重量：")
# g = float(g)
# kg = g / 1000
# print(f"{g}克 = {kg}千克")

# weight = input("请输入你的体重：")
# weight = float(weight)
# if weight >= 70:
#     grade = "偏重"
# elif 60 <= weight <70:
#     grade = "标准"
# elif weight <60:
#     grade = "偏廋"
# print(f"你的体重为{weight},体重等级为{grade}")

# name = "马晟原"
# xingbie = "男"
# age = 25
# zhuanye = "化学工程与工艺"
# print(f"我的名字是{name},性别是{xingbie},年龄是{age},专业是{zhuanye}")

# mm = input("请输入长度：")
# mm = float(mm)
# cm = mm / 10
# print(f"{mm}毫米 = {cm}厘米")

# age= input("请输入年龄：")
# age = float(age)
# if age >= 18:
#     grade = "成年人"
# elif 12 <= age <=17:
#     grade = "青少年"
# else:
#     grade = "儿童"
# print(f"你的年龄是{age},年龄阶段是{grade}")

# name = "马晟原"
# jiguan = "云南昭通"
# shengao = 183
# hobby = "围棋"
# print(f"我的名字是{name},籍贯在{jiguan},身高是{shengao},爱好是{hobby}")

# jin = input("请输入重量:")
# jin = float(jin)
# gongjin = jin / 2
# print(f"{jin}斤 = {gongjin}公斤")

# wendu = input("请输入温度:")
# wendu = float(wendu)
# if wendu > 30:
#     grade = "炎热"
# elif 20 <= wendu <= 30:
#     grade = "舒适"
# else:
#     grade = "凉爽"
# print(f"你的温度是{wendu},温度等级是{grade}")

# name = "马晟原"
# xingzuo = "天蝎座"
# shengao = 183
# hobby = "围棋"
# print(f"我的名字叫{name},星座是{xingzuo},身高是{shengao},喜欢的运动是{hobby}")

# inch = input("请输入长度：")
# inch = float(inch)
# cm = inch * 2.54
# print(f"{inch}英寸 = {cm}厘米")

# score = input("请输入你的成绩：")
# score = float(score)
# if score >= 95:
#     grade = "学霸"
# elif 85 <= score <=94:
#     grade = "良好"
# elif 60 <= score <= 84:
#     grade = "及格"
# else:
#     grade = "不及格"
# print(f"你的成绩是{score},成绩等级是{grade}")

# name = "马晟原"
# csnf = 2000
# xznf = 2026
# where = "昭通"
# nl = xznf - csnf
# print(f"我的名字是{name}，年龄是{nl},家乡是{where}")

# km = input("请输入里程：")
# km = float(km)
# li = km * 2
# print(f"{km}公里 = {li:.1f}里")

# zl = input("请输入重量：")
# zl = float(zl)
# if zl <= 2:
#     grade = "运费8元"
# elif 2 < zl <= 5:
#     grade = "运费15元"
# else:
#     grade = "运费25元"
# print(f"你的快递重量为{zl}kg,所以运费为{grade}")

# kg = input("请你输入体重：")
# m = input("请你输入身高：")
# kg = float(kg)
# m = float(m)
# BMI = kg / (m * m)
# if BMI < 18.5:
#     grade = "偏瘦"
# elif 18.5 <= BMI < 24:
#     grade = "正常"
# elif 24 <= BMI <28:
#     grade = "偏重"
# else:
#     grade = "肥胖"
# print(f"你的BMI指数为{BMI:.2f},所以你的体型为{grade}")

# t = input("请输入你的用水情况：")
# t = float(t)
# if t <= 10:
#     grade = t * 3
# else:
#     grade = (t - 10) * 4 + 10 * 3
# print(f"你一用水{t}吨,所以水费为{grade}元")

# cj = input("请输入你的成绩：")
# cj = float(cj)
# if cj >= 90:
#     grade = "优秀"
# elif 80 <= cj <= 89:
#     grade = "良好"
# elif 60 <= cj <=79:
#     grade = "中等"
# else:
#     grade = "较差"
# if cj >= 60:
#     jg = "及格"
# else:
#     jg = "不及格"
# print(f"你的成绩为{cj},成绩等级为{grade},{jg}")

# gl = input("请输入你的公里数：")
# gl = float(gl)
# if gl <= 3:
#     grade = 8
# elif gl > 3:
#     grade = 8 + (gl - 3) * 1.5
# print(f"你的公里数为{gl}公里,所以收费{grade:.2f}元")

# year = input("请输入你的年份：")
# year = int(year)
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     res = "闰年"
# else:
#     res = "平年"
# print(f"所以{year}是{res}")

# yj = input("请输入原价：")
# yj = float(yj)
# if yj >= 500:
#     grade = yj * 0.8
# elif 300 <= yj < 500:
#     grade = yj * 0.9
# else:
#     grade = yj * 1
# print(f"你的原价为{yj}元,所以实付金额为{grade:.2f}元")

# yj = input("请输入原价：")
# yj = float(yj)
# hy = input("你是否为会员")
# hy = int(hy)
# if yj >= 1000:
#     grade = yj - 200
# elif 500 <= yj < 1000:
#     grade = yj - 80
# elif 300 <= yj < 500:
#     grade = yj - 30
# else:
#     grade = yj
# if hy == 1:
#     hyj = grade *0.9
# elif hy == 0:
#     hyj = grade
# print(f"你的满减价为{grade:.2f}元,会员价为{hyj:.2f}元")

# 带入合法性检查
while True:
    try:
        yj = float(input("请输入购物原价："))
        if yj < 0:
            print("价格不能为负数，请重新输入！")
            continue
        break
    except:
        print("输入格式错误，请输入数字！")

while True:
    try:
        hy = int(input("是否为会员（1=是，0=否）："))
        if hy == 1 or hy == 0:
            break
        else:
            print("只能输入 1 或 0，请重新输入！")
    except:
        print("输入格式错误,请输入整数 1 或 0！")

if yj >= 1000:
    grade = yj - 200
elif 500 <= yj < 1000:
    grade = yj - 80
elif 300 <= yj < 500:
    grade = yj - 30
else:
    grade = yj
if hy == 1:
    hyj = grade * 0.9
else:
    hyj = grade
print(f"原价：{yj:.2f} 元")
print(f"满减后价格：{grade:.2f} 元")
print(f"最终实付价格：{hyj:.2f} 元")