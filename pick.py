import pickle

l = [1,2,3,4,5]

file = open("write_data.txt","wb")

pickle.dump(l,file)

file.close()
