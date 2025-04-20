file = input("enter a file name:")
fill = open (file)
count = dict()
for lines in fill: 
     x = lines.split()
    #split the lines into words based on space.
     #print(x)
     for words in x:
        count[words] = count.get(words,0)+1
    # for every word, if not in dictionary, give default value of 0 and add one to it. 
#print(count)
lstt = list()
for key,value in count.items():
    newtup = (value,key)
    lstt.append(newtup)
lstt = sorted(lstt, reverse = True)
# make a list of tuples using the key, value pairs in the dictionary. Every tuple consist of a key and their respected value. The list is also sorted from greatest to smallest with regards to values. That's why the order was reversed to sort with values. 

#print(lstt)

for x,y in lstt[:10]:
  print(y,x)
# Print the top 10 values of the list of tuples and reverse the order again from value, key to key, value.
        
         