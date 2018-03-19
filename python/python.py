import os

# python 四大資料結構
# 1.串列    []
print('====  1.串列  ====')
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

# count 計算串列值出現的次數
print(demo_list.count('a'))     #1
demo_list.append('a')
print(demo_list.count('a'))     #2

#join 用一個字串把 list 串起來
print(demo_list)                      #['a', 'c', 'f', 'test', '123', '456', 'a']
print("**".join(demo_list))           #"a**c**f**test**123**456**a"

#sort 排序串列  sort(reverse=True) 改為降冪排序
print(demo_list)
demo_list.sort()                #['123', '456', 'a', 'a', 'c', 'f', 'test']
print(demo_list)                    
demo_list.sort(reverse=True)    #['test', 'f', 'c', 'a', 'a', '456', '123']
print(demo_list)

#len 回傳長度
print(len(demo_list))           #7

# 2.Tuple   ('a', 'b')
print('====  2.Tuple  ====')
#宣告
demo_tuple = ()                 #()
print(demo_tuple)  
# 後面加逗號也可以宣告
demo_tuple = 'aa', 'bb'         #('aa', 'bb')
print(demo_tuple)

#tuple 同時指定多變數
a, b = demo_tuple
print(a)                        #aa
print(b)                        #bb

#使用 tuple 交換變數值的小技巧
a = 'aaa'
b = 'bbb'
print(a)                        #aaa
print(b)                        #bbb
a, b = b, a 
print(a)                        #bbb
print(b)                        #aaa

# 3.字典    {'a':'aaa', 'b':'bbb'}      key 值是唯一值
print('====  3.字典  ====')

#宣告
demo_dict = {}
demo_dict = dict()
print(demo_dict)

#放值
demo_dict = {"a":"aa"}
print(demo_dict)                #{'a': 'aa'}

#dict 各種轉換
demo_dict = dict([['a', 'b'], ['c', 'd']])
print(demo_dict)                #{'a': 'b', 'c': 'd'}
demo_dict = dict([('a', 'b'), ('c', 'd')])
print(demo_dict)                #{'a': 'b', 'c': 'd'}
demo_dict = dict((['a', 'b'], ['c', 'd']))
print(demo_dict)                #{'a': 'b', 'c': 'd'}
demo_dict = dict(['ab', 'cd'])
print(demo_dict)                #{'a': 'b', 'c': 'd'}
demo_dict = dict(('ab', 'cd'))
print(demo_dict)                #{'a': 'b', 'c': 'd'}

print(demo_dict['a'])           #b

#update 合併字典
print(demo_dict)                #{'a': 'b', 'c': 'd'}
demo_dict.update({"c":"c", "d":"d"})
print(demo_dict)                #{'a': 'b', 'c': 'c', 'd': 'd'}

#del 移除某一個key 值
del demo_dict["c"]
print(demo_dict)                #{'a': 'b', 'd': 'd'}

#clear 
demo_dict.clear()
print(demo_dict)                #{}

#in 檢查 key 是否存在
demo_dict = {'a':'b', 'c':'d'}
print('a' in demo_dict)         #True
print('b' in demo_dict)         #False

#get
print(demo_dict.get('d'))       #None
print(demo_dict.keys())         #dict_keys(['a', 'c'])
print(list(demo_dict.keys()))   #['a', 'c']
print(demo_dict.values())       #dict_values(['b', 'd'])
print(list(demo_dict.values())) #['b', 'd']
print(demo_dict.items())        #dict_items([('a', 'b'), ('c', 'd')])
print(list(demo_dict.items()))  #[('a', 'b'), ('c', 'd')]

# 4.集合    {'a', 'b'} set   不能重複   重複塞也只會有一個
print('====  4.集合  ====')
#宣告
demo_set = set()
print(demo_set)                 #set()
demo_set = {'a', 'b', 'c', 'd'} 
print(demo_set)                 #{'a', 'c', 'd', 'b'}
demo_set = set('abcd')
print(demo_set)                 #{'a', 'c', 'd', 'b'}
demo_set = set({'a':'aa', 'b':'bb'})        #只會留下 key 值
print(demo_set)                 #{'a', 'b'}

# in
print('a' in demo_set)          #True
print('c' in demo_set)          #False

#交集   下面兩句意思一樣
print({1, 2} & {2, 3})              #{2}
print({1, 2}.intersection({2, 3}))  #{2}

#聯集
print({1, 2} | {2, 3})              #{1, 2, 3}
print({1, 2}.union({2, 3}))         #{1, 2, 3}

#差集
print({1, 2} - {2, 3})              #{1}
print({1, 2}.difference({2, 3}))    #{1} 

#互斥
print({1, 2} ^ {2, 3})              #{1,3}
print({1, 2}.symmetric_difference({2, 3}))    #{1,3} 

#子集合 真子集合(除了完全包含還要有其他元素)
a = {1, 2, 3}
b = {1, 2}
print(a>a) 
print(a>=a)
print(a>b)
print(a<b)

# 其他轉換
print('====  其他轉換  ====')
# tuple to list
tp = ('aa', 'bb', 'c')
_list = list(tp)
print(_list)

#list to tuple
print(tuple(['val1', 'val2', 'val1']))      #('val1', 'val2', 'val1')

#切開字串
_list = []
_str = 'aaa.bbb.ccc.ddd'
_list = _str.split('.')
print(_list)                                #['aaa', 'bbb', 'ccc', 'ddd']