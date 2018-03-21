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
