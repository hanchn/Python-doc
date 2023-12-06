person = {
    "name": "John",
    "height": "165cm",
    "tel": "123123123",
    "gender": "male",
    "adress": "suzhou...",
}

# 增加体重
person["weight"] = "70kg"
print(person["weight"])
# 修改名字
person["name"] = "Jack"
print(person["name"])
# 删除体重
del person["weight"]
print(person)
# 清空字典
person.clear()
print(person)
# 删除字典
# del person
# print(person)
