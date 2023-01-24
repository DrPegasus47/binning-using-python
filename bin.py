min_limit = lambda data: data - (data % 10)
max_limit = lambda data: data + (10 - (data % 10))


list = [48, 32, 12, 35, 9, 59, 12, 15, 22, 18, 32, 50, 49]
min_age, max_age, age_dict = [], [], {}
#print(f"{list}, max: {max(list)}, min: {min(list)}")
for x in range(min_limit(min(list)), min_limit(max(list)) + 1, 10):
  min_age.append(x + 1)
for x in range(max_limit(min(list)), max_limit(max(list)) + 1, 10):
  max_age.append(x)
for x, y in zip(min_age, max_age):
  age_dict[(x, y)] = []
  for ele in list:
    if ele in range(x, y + 1):
      age_dict[(x, y)].append(ele)

for x in age_dict:
  print(f"{x[0]} - {x[1]} : {age_dict[x]}")

