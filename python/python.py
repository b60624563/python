import os


# python 四大資料結構
# 1.串列    []
print('1.串列')
# 兩種宣告意思一樣
demo_list = []
demo_list = list()

# 把字串一個一個切開
demo_list = list("abcd")        #['a', 'b', 'c', 'd']
print(demo_list)

# 再串列結尾多串一個值
demo_list.append("test")        #['a', 'b', 'c', 'd', 'test']
print(demo_list)

#移除串列指定的值
demo_list.remove('b')           #['a', 'c', 'd', 'test']
print(demo_list)

#取得指定位置的值
print(demo_list[0])             #a
print(demo_list[-1])            #test     (最後一個值)

#取得指定區間
print(demo_list[0:4:1])         #有點像迴圈取直  for(int i=0; i<4; i++)  並且逐步取出值

#合併兩個串列
demo_list2 = ['123', '456', '7']
demo_list.extend(demo_list2)    #['a', 'c', 'd', 'test', '123', '456', '7']
print(demo_list)

#insert 串列(可以指定位置  直接插入指定位置)
demo_list.insert(3,"f")         #['a', 'c', 'd', 'f', 'test', '123', '456', '7']
print(demo_list)                

#del 指定刪除值的位置
del demo_list[2]                #['a', 'c', 'f', 'test', '123', '456', '7']
print(demo_list)

#pop 取得串列的一個值並移除  沒有給定位置會由(-1)開始拋出也就是最後一筆
print(demo_list.pop())          #回傳 7    
print(demo_list)                #['a', 'c', 'f', 'test', '123', '456']

#index()    沒有的會噴  有的話會回是在串列的第幾個    如果有重複則會回傳第一個的位置
print(demo_list.index('a'))     #0

# in   可以用 in 來測試串列是否有這個值
print('a' in demo_list)         #True
print('aaaa' in demo_list)      #False

# 2.Tuple   ('a', 'b')
print('2.Tuple')

# 3.字典    {'a':'aaa', 'b':'bbb'}
print('3.字典')

# 4.集合    {'a', 'b'}
print('4.集合')

# 其他轉換
print('其他轉換')
# tuple to list
tp = ('aa', 'bb', 'c')
_list = list(tp)
print(_list)

#切開字串
_list = []
_str = 'aaa.bbb.ccc.ddd'
_list = _str.split('.')
print(_list)