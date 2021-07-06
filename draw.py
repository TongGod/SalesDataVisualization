import json

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 1.brandorder――柱状
def brandorder():
    plt.figure(figsize=(13, 9))
    with open("./json/brandOrder.json", 'r') as load_f:
        brandorder_list = json.load(load_f)
    x, y = [], []
    for br in brandorder_list:
        if br[1] > 1000:
            x.append(br[0])
            y.append(br[1])
    plt.bar(x, y, color='pink')
    ax1 = plt.gca()
    ax1.set_facecolor('#E6E6E6')
    plt.grid(b=True, color='#FFFFFF')
    for key, spine in ax1.spines.items():
        if key == 'right' or key == 'top' or key == 'left' or key == 'bottom':
            spine.set_visible(False)
    plt.legend(("各品牌用户数",))
    plt.xticks(rotation=30)
    plt.xlabel("品牌", size=18)
    plt.ylabel("用户数", size=18)
    plt.savefig("./img/brandorder.png")
    print("brandorder图保存成功！")
    plt.close()


# 2.brandsumofprice――柱状
def brandsumofprice():
    plt.figure(figsize=(13, 9))
    with open("./json/brandSumOfPrice.json", 'r') as load_f:
        brandsumofprice_list = json.load(load_f)
    x, y = [], []
    for br in brandsumofprice_list:
        if len(str(br[0])) > 7:
            x.append(br[0][:7] + "\n" + br[0][7:])
        else:
            x.append(br[0])
        y.append(br[1])

    plt.bar(x, y, color='pink')
    ax2 = plt.gca()
    ax2.set_facecolor('#E6E6E6')
    plt.grid(b=True, color='#FFFFFF')
    for key, spine in ax2.spines.items():
        if key == 'right' or key == 'top' or key == 'left' or key == 'bottom':
            spine.set_visible(False)

    plt.legend(("各品牌销售数据",))
    plt.xticks(rotation=30)
    plt.xlabel("品牌", size=18)
    plt.ylabel("销售额（千万）", size=18)
    plt.title("平台每月销量", size=18)
    plt.savefig("./img/brandsumofprice.png")
    print("brandsumofprice图保存成功！")
    plt.close()


# 3.categorysumofprice――柱状
def categorySumOfPrice():
    plt.figure(figsize=(13, 9))
    with open("./json/categorySumOfPrice.json", 'r') as load_f:
        categorySumOfPrice_list = json.load(load_f)
    x, y = [], []
    for br in categorySumOfPrice_list:
        x.append(br[0])
        y.append(br[1])
    plt.bar(x, y, color='#F781F3')
    plt.legend(("类别",))
    plt.savefig("./img/categorySumOfPrice.png")
    print("categorySumOfPrice图保存成功！")
    plt.close()


# 4.categoryuser――柱状
def categoryUser():
    plt.figure(figsize=(13, 9))
    with open("./json/categoryUser.json", 'r') as load_f:
        categoryUser_list = json.load(load_f)
    x, y = [], []
    for br in categoryUser_list:
        x.append(br[0])
        y.append(br[1])
    plt.bar(x, y)
    plt.legend(("类别",))
    plt.savefig("./img/categoryUser.png")
    print("categoryUser图保存成功！")
    plt.close()


# 5.hourorder――折线
def hourorder():
    plt.figure(figsize=(13, 9))
    with open("./json/HourOrder.json", 'r') as load_f:
        hourorder_list = json.load(load_f)
    x, y = [], []
    for br in hourorder_list:
        x.append(br[0])
        y.append(br[1])
    plt.plot(x, y, color='red')
    plt.xlabel("时间", size=18)
    plt.ylabel("用户购买量", size=18)
    plt.xticks(range(0, 25))
    plt.savefig("./img/hourorder.png")
    print("hourorder图保存成功！")
    plt.close()


# 6.monthorder――折线
def monthorder():
    with open("./json/MonthOrder.json", 'r') as load_f:
        monthorder_list = json.load(load_f)
    x, y = [], []
    for br in monthorder_list:
        x.append(br[0])
        y.append(br[1])
    plt.plot(x, y, color='pink')
    plt.xlabel("月份", size=18)
    plt.ylabel("销量", size=18)
    plt.savefig("./img/monthorder.png")
    print("monthorder图保存成功！")
    plt.close()


# 7.monthsumofprice――折线
def monthsumofprice():
    with open("./json/MonthSumOfPrice.json", 'r') as load_f:
        monthsumofprice_list = json.load(load_f)
    x, y = [], []
    for br in monthsumofprice_list:
        x.append(br[0])
        y.append(br[1])
    plt.title("每月消费总金额（单位/元）", size=18)
    ax3 = plt.gca()
    ax3.set_facecolor('#E6E6E6')
    plt.grid(b=True, color='#FFFFFF', axis='y')
    for key, spine in ax3.spines.items():
        if key == 'right' or key == 'top' or key == 'left' or key == 'bottom':
            spine.set_visible(False)
    plt.plot(x, y, color='pink')
    plt.savefig("./img/monthsumofprice.png")
    print("monthsumofprice图保存成功！")
    plt.close()


# 8.monthuser――折线
def monthuser():
    with open("./json/MonthUser.json", 'r') as load_f:
        monthuser_list = json.load(load_f)
    x, y = [], []
    for br in monthuser_list:
        x.append(br[0])
        y.append(br[1])
    plt.title("每月消费人数", size=18)
    ax4 = plt.gca()
    ax4.set_facecolor('#E6E6E6')
    plt.grid(b=True, color='#FFFFFF', axis='y')
    for key, spine in ax4.spines.items():
        if key == 'right' or key == 'top' or key == 'left' or key == 'bottom':
            spine.set_visible(False)
    plt.plot(x, y, color='pink')
    plt.savefig("./img/monthuser.png")
    print("monthuser图保存成功！")
    # plt.close()
    plt.show()


if __name__ == '__main__':
    # brandorder()
    # brandsumofprice()
    # categorySumOfPrice()
    # categoryUser()
    # hourorder()
    # monthorder()
    # monthsumofprice()
    monthuser()
