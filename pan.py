import pandas as pd
# Python Series Object = which is a one dimensional data structure in Pandas
# Series Object from list
a = pd.Series([1,2,3,4])
print(a)
print(type(a))

# Changing index into alphabetical index
a = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])
print(a) 

# Series object from dictionary
a = pd.Series({'a':10 , 'b':20, 'c':30})
print(a)

# Changing index positions
a = pd.Series({'a':10 , 'b':20, 'c':30}, index = ['b','c','d','a'])
print(a)


# Extracting individual elements
a = pd.Series([1,2,3,4,5,6,7,8,9])
print(a[3])
print(a[:4])
print(a[-3:])

# Adding two Series Objects
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([10,20,30,40,50])
print(s1+s2)

# Adding scaler values to the Series object
s1 = pd.Series([1,2,3,4,5])
print(s1+1)
print(s1 * 2)
print(s1 / 2)


# Pandas Dataframes  = It is 2 Dimensional datastructure consists of rows and columns
# DataFrame using dictionary
d = pd.DataFrame({'Name':['Ankit','Saumya','Atul'], 'Marks': [90,80,70]})
print(d)

                #     Name  Marks
                # 0   Ankit     90
                # 1  Saumya     80
                # 2    Atul     70



iris = pd.read_csv('iris.csv')
print(iris.head())      # It gives first five records 
                #    Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
                # 0   1            5.1           3.5            1.4           0.2  Iris-setosa
                # 1   2            4.9           3.0            1.4           0.2  Iris-setosa
                # 2   3            4.7           3.2            1.3           0.2  Iris-setosa
                # 3   4            4.6           3.1            1.5           0.2  Iris-setosa
                # 4   5            5.0           3.6            1.4           0.2  Iris-setosa

print(iris.tail())      # It gives last 5 records
print(iris.shape)       # It gives the no of rows and columns
print(iris.describe())  # It gives the general information




print(iris.head())
print(iris.iloc[5:11,3:])   # It gives the rows 5 - 10 and columns 3 - 5

                #    PetalLengthCm  PetalWidthCm      Species
                # 5             1.7           0.4  Iris-setosa
                # 6             1.4           0.3  Iris-setosa
                # 7             1.5           0.2  Iris-setosa
                # 8             1.4           0.2  Iris-setosa
                # 9             1.5           0.1  Iris-setosa
                # 10            1.5           0.2  Iris-setosa



print(iris.loc[1:10,("PetalLengthCm","Species")])
                #     PetalLengthCm      Species
                # 1             1.4  Iris-setosa
                # 2             1.3  Iris-setosa
                # 3             1.5  Iris-setosa
                # 4             1.4  Iris-setosa
                # 5             1.7  Iris-setosa
                # 6             1.4  Iris-setosa
                # 7             1.5  Iris-setosa
                # 8             1.4  Iris-setosa
                # 9             1.5  Iris-setosa
                # 10            1.5  Iris-setosa


# Dropping columns
print(iris.drop('Species',axis = 1))
#       Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
# 0      1            5.1           3.5            1.4           0.2
# 1      2            4.9           3.0            1.4           0.2
# 2      3            4.7           3.2            1.3           0.2
# 3      4            4.6           3.1            1.5           0.2
# 4      5            5.0           3.6            1.4           0.2
# ..   ...            ...           ...            ...           ...
# 145  146            6.7           3.0            5.2           2.3
# 146  147            6.3           2.5            5.0           1.9
# 147  148            6.5           3.0            5.2           2.0
# 148  149            6.2           3.4            5.4           2.3
# 149  150            5.9           3.0            5.1           1.8

# [150 rows x 5 columns]


# Dropping rows
print(iris.drop([2,3,4,5],axis = 0))

#       Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm         Species
# 0      1            5.1           3.5            1.4           0.2     Iris-setosa
# 1      2            4.9           3.0            1.4           0.2     Iris-setosa
# 6      7            4.6           3.4            1.4           0.3     Iris-setosa
# 7      8            5.0           3.4            1.5           0.2     Iris-setosa
# 8      9            4.4           2.9            1.4           0.2     Iris-setosa
# ..   ...            ...           ...            ...           ...             ...
# 145  146            6.7           3.0            5.2           2.3  Iris-virginica
# 146  147            6.3           2.5            5.0           1.9  Iris-virginica
# 147  148            6.5           3.0            5.2           2.0  Iris-virginica
# 148  149            6.2           3.4            5.4           2.3  Iris-virginica
# 149  150            5.9           3.0            5.1           1.8  Iris-virginica

# [146 rows x 6 columns]



# More Pandas Functions
print(iris.min())
# Id                         1
# SepalLengthCm            4.3
# SepalWidthCm             2.0
# PetalLengthCm            1.0
# PetalWidthCm             0.1
# Species          Iris-setosa
# dtype: object
print(iris.max())
# Id                          150
# SepalLengthCm               7.9
# SepalWidthCm                4.4
# PetalLengthCm               6.9
# PetalWidthCm                2.5
# Species          Iris-virginica
# dtype: object

print(iris.mean())
# Id               75.500000
# SepalLengthCm     5.843333
# SepalWidthCm      3.054000
# PetalLengthCm     3.758667
# PetalWidthCm      1.198667
# dtype: float64

print(iris.median())
# Id               75.50
# SepalLengthCm     5.80
# SepalWidthCm      3.00
# PetalLengthCm     4.35
# PetalWidthCm      1.30
# dtype: float64


def half(s):
    return s*0.5

print(iris.head())

a = iris[['SepalWidthCm','PetalLengthCm']].apply(half)
print(a)



# More Functions in Pandas
print(iris['Species'].value_counts())     # value_counts()       counts the cateogorical data
print(iris.sort_values(by='PetalWidthCm'))