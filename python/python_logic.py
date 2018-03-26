print('邏輯部分')



for i in range(1, 3):
    if i%2==0:
        print("雙數:" + str(i))
    else:
        print("單數:" + str(i))

test = ('a')

if test:
    print("true")
else:
    print("false")

count = 0
while(count<2):
    count = count + 1
    # input
    _in = ''
    #_in = input(str(count) + "_請輸入指令:")
    if(_in == 'break'):
        break

    elif(_in == 'continue'):
        continue
    else:
        print('else')


demo_list = {'aa', 'bb', 'ccc'}
for i in demo_list:
    print(i)
    
else:
    print('else')



print('***************')
print('測試 break')

for i in range(1, 10):
    print(i)
    if i==9:
        break
else:
    print('完整執行完回圈才會進 else 如果有 break 就不會看到這行')


# zip 用法   多值回圈  執行次數為最短的迴圈

a_array = ['a', 'aa', 'aaa']
b_array = ['b', 'bb', 'bbb']
c_array = ['c', 'cc', 'ccc', 'cccc']

for a, b, c in zip(a_array, b_array, c_array):
    print(a + b + c)

for i in range(1,30,7):
    print(i)

# 生成式   變數 for i in 迭代像目 if 條件
temp_list = list(i for i in range(1, 11 , 3) if i != 4)
print(temp_list)