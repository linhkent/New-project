import mlab
from food import Food

mlab.connect()

# 1. Create

# 1.1 Create a food data
f = Food(title = "banh sai", link = "<<link sai>>")  # link is image's link
# 1.2 Save it
# f.save()

# 2. Read

# 2.1 Get cursor
# Lazy loading
f_objects = Food.objects()  # lazy loading  # same as list
# 2.2 Process cursor
# f_first = f_objects[0]   # actual data transfering
# print(f_first.title)
# print(f_first.link)

# print(len(f_objects))  # dev dem
# print(f_objects.count())  # cursor dem

# for f in f_objects:
#     # print(f)
#     print(f.title)
#     print(f.link)
#     print("----------")

# 3. Update

# f = f_objects[3]
# f.update(set__title="banh rat rat ngon", set__link="<<link ngon>>")
# f.reload()  # dong bo du lieu
# print(f.title)

# 4. Delete
# f.delete()

# delete by id
# f = f_objects.with_id("5c4d7df7adc4772af8987e1f")
# if f != None:
#     f.delete()
#     print("OK")
# else:
#     print("Not Found")

f = f_objects.with_id("5c4d7df7adc4772af8987e1f")

print(f.title)
print(f.link)