#問題名:mission7
#概要:ランダムな整数のリストを作成し、その中の最大値を求めるプログラムを作成してください。
import random
#最大値をみつける関数
def max_value(numbers):
    for n in numbers:
        if n > max:
            max = n
    return max


max=0

rand_list=[random.randint(1,100) for i in range(10)]
print("最大値は"+str(max_value(rand_list))+"です。")