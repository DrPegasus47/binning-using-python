min_limit = lambda data: data - (data % 10) #lambda function to return the lower range of a number (returns 40 for 49, 20 for 24 and so on)
max_limit = lambda data: data + (10 - (data % 10)) #lambda function to return the upper range of a number (returns 50 for 49, 30 for 24 and so on)

list = [48, 32, 12, 35, 9, 59, 12, 15, 22, 18, 32, 50, 49] #list of ages, can be user entered or DataFrame attribute
min_age, max_age, age_dict = [], [], {}
#print(f"{list}, max: {max(list)}, min: {min(list)}")
for x in range(min_limit(min(list)), min_limit(max(list)) + 1, 10):
  min_age.append(x + 1) #list with all the lower limits of the bins
for x in range(max_limit(min(list)), max_limit(max(list)) + 1, 10):
  max_age.append(x) #list with all the upper limits of the bins
for x, y in zip(min_age, max_age):
  age_dict[(x, y)] = [] #creating a list for the said bin
  for ele in list: #traverses list of ages
    if ele in range(x, y + 1): #checking if edge belongs to the bin
      age_dict[(x, y)].append(ele) #appends to the bin list if element belongs to the bin

for x in age_dict:
  print(f"{x[0]} - {x[1]} : {age_dict[x]}") #prints each age bin and the constituent age value
