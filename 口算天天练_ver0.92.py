print("1.练习模式")
print("2.测试模式")
print("3.历史记录")
a=int(input())
if a == 1:
    print("模式未开发!")
    print("\n")
##elif a == 3:
##    f = open("sampleList.txt", "r")
##    table = f.read()
##    f.close()
##    print(table)
elif a == 2:
    print("现支持0到n的加减法")
    print("加法or减法(1/2)")
    sss=int(input())
    print("输入题目数量")
    n=int(input())
    print("输入最大加or被减数数")
    m=int(input())
    sum=0
    if(sss==1):
        for i in range(n):
            import random
            sum1 = (random.randint(0, m))
            sum2 = (random.randint(0, m))
            sum3 = sum1 + sum2
            print(sum1, " + ", sum2, " = ")
            ans = int(input())
            if sum3 == ans:
                print("正确!")
                sum += 1
            else:
                print("错误")
    elif(sss==2):
        for i in range(n):
            import random
            sum1 = (random.randint(0, m))
            sum2 = (random.randint(0, sum1))
            sum3 = sum1 - sum2
            print(sum1, " - ", sum2, " = ")
            ans = int(input())
            if sum3 == ans:
                print("正确!")
                sum += 1
            else:
                print("错误")
    print("总题数:",n)
    print("正确题数:",sum)
    SUM = str(sum)
    N = str(n)
    print("错误题数:",n-sum)
    ##name=input("你的姓名:")
    ##ipTable = [name+" 正确题数:"+SUM+"总题数:"+N]
    ##f = open(r'ip.txt', 'r')
    ##a = list(f)
    ##print(a)
    ##f.close()
else :
    print("模式未开发!")
