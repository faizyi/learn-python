#mutable
# info = {
#     "name" : "faiz",
#     "subject": ["phy", "chem"],
#     "topic" : ("dict", "set"),
#     "age": 35,
#     "is_adult" : True,
#     2 : 2,
#     2.2 : 2.3,
#     "sum": 2+2,
# }
# info["name"] = "noor"
# info["firstName"] = "Faiz"
# print(type(info), info)

# null_dict = {}
# null_dict["name"] = "faiz"
# print(null_dict)


#nesting dict
students = {
    "name" : "Faiz",
    "sub": {
        "phy" : 23,
        "chem" : 35
    }
}
# print(students["sub"]["phy"])
# print(len(students))

#Methods
#keys()
# print(len(list(students.keys())))

#Values()
# print(list(students.values()))

#items()
# print(list(students.items()))
# pairs = list(students.items())
# print(pairs[0])

#update
# students.update({"city" : "New York"})
# print(students)
# new_dict = {"city" : "New York", "name" : "Faiz Noor", "score" : {22:22, 33:33}}
# students.update(new_dict)
# print(students)


# print(students["name2"])
# print(students.get("name2"))