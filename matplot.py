import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating two lines plot
x = np.arange(1,11)
y1 = 3*x
y2 = 2*x
plt.plot(x,y1,color='g',linestyle=':',linewidth=5)
plt.plot(x,y2,color='r',linestyle='-',linewidth=3)
plt.title("Two Line plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# Creating two different subplot or line plot in same region
plt.subplot(2,1,1)
plt.plot(x,y1,color='g',linestyle=':',linewidth=5)


plt.title("1st sub plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)


plt.subplot(2,1,2)
plt.plot(x,y2,color='r',linestyle='-',linewidth=4)

plt.title("2nd sub plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

plt.show()



# Creating Vertical Bar plot
student = {"Saumya":90, "Atul":80, "Aparna":95, "Rohan":65}
names = list(student.keys())
marks= list(student.values())
plt.title('Vertical Bar Plot')
plt.xlabel('Name of the students')
plt.ylabel('Marks of the students')
plt.grid(True)
plt.bar(names,marks,color='g')
plt.show()

# Creating horizontal bar plot
plt.title('Horizontal Bar Plot')
plt.xlabel('Marks of the students')
plt.ylabel('Name of the students')
plt.grid(True)
plt.barh(names,marks,color='g')
plt.show()


# Creating a simple scatter plot
x = [10,20,30,40,50,60,70,80,90]
y = [8,1,7,2,0,3,7,3,2]
z = [7,2,5,6,9,1,4,5,3]

plt.scatter(x,y,marker='*',color='g', s=100)
plt.scatter(x,z,marker='.',color='r', s=200)

plt.show()


# Creating two different scatter sub plots in the same region
plt.subplot(1,2,1)
plt.scatter(x,y,marker='.',c='g',s=100)

plt.subplot(1,2,2)
plt.scatter(x,z,marker='*',c='r',s=200)

plt.show()




# Histogram 
data = [2,2,2,4,5,6,5,8,4,9,3,6,5,2,8,7,7,5,5,6,4]
plt.hist(data,color='b',bins=2)
plt.show()


# Creating histogram with a iris dataset
iris = pd.read_csv('iris.csv')  # Loading the iris dataset
print(iris.head())
plt.hist(iris['SepalLengthCm'],color='g',bins=30)
plt.show()




# Creating BOX PLOT 
one=[1,2,3,4,5,6,7,8,9]
two=[1,2,3,4,5,4,3,2,1]
three=[6,7,8,9,8,7,6,5,7,8]

data = list([one,two,three])
plt.boxplot(data)
plt.show()


# Creating violin plot
data = list([one,two,three])
plt.violinplot(data,showmedians=True)
plt.show()




# Creating Pie chart
fruits = ['Apple','Mango','Guava','Pomegranate','Grapes']
quantity = [50,60,45,85,95]

plt.pie(quantity,labels=fruits, autopct='%0.1f%%', colors=['yellow','blue','red','green','grey'])
plt.show()

# Creating Doughnut Chart
fruits = ['Apple','Mango','Guava','Pomegranate','Grapes']
quantity = [50,60,45,85,95]


plt.pie(quantity,labels=fruits, radius=1)
plt.pie([100],colors=['w'], radius=0.5)
plt.show()