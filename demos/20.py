setList = set(("cat", "dog", "duck"))

print(setList)

# 增加元素
# setList.add("fish")

# print(setList)

# 移除元素
# setList.remove("dog")
# print(setList)

# 删除元素
# setList.discard("cat")
# print(setList)
# 使用discard和remove都可以删除set当中的元素，
# 区别就是remove的元素在set当中没有的话会报错，而discard不会。

# 移除元素
# difference_update() 方法与 difference() 方法的区别在于
# difference() 方法返回一个移除相同元素的新集合，而
# difference_update() 方法是直接在原来的集合中移除元素
# setList.difference_update(("cat", "dog"))
# print(setList)

# 更新set
# setList.update(("fish", "bird"))
# print(setList)

# 随机移除pop
setList.pop()
print(setList)
