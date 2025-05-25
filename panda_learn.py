import pandas as pd
reviews=pd.read_csv("M:\python练习\code\yanshi.CSV")

#显示文件规模
print(reviews.shape)

#显示前五行数据
#print(reviews.head())

#print(reviews)

s1=reviews.y
#print(s1)

# 显示 y 列的统计信息
print(reviews['y'])

#显示第一行数据,
s2=reviews.iloc[0]
print(s2)
s3=reviews.loc[0]
print(s3)

#先行后列
s4=reviews.iloc[:3,0]
print(s4)

#相同的操作
print(reviews.iloc[[0,1,2],0])

#同样从后往前一样的操作
print(reviews.y.iloc[-2:])

#loc的操作范式
print(reviews.loc[0,'y'])

#注意loc存在数据集的索引，相当于一个大的词典。iloc忽略了索引，相当于一个大的矩阵
print(reviews.loc[:3,['x1','x2']])

#都选0到10，iloc是0到9，loc是0到10
print(reviews.iloc[0:2,0])
print(reviews.y.loc[0:2])

#set_index(title)方法也可以同样操作,是将第一列换位该标签
print(reviews.set_index('x5'))

#条件选择
s5=reviews.y==0.27
print(s5)
print(reviews.loc[s5])
s6=(reviews.y>0.27)&(reviews.x1>0.26)
print(reviews.loc[s6])
s7=(reviews.y>0.270)|(reviews.x1<0.2)
print(reviews.loc[s7])

#isin()方法
s8=reviews.y.isin([0.27,0.28])
print(reviews.loc[s8])

#分配数据
reviews['y']='维度'
print(reviews['y'])


#使用renge函数
reviews['x1']=range(len(reviews))
print(reviews['x1'])