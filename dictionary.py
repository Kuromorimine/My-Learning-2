# dict ={
#     "name" : "Hero", #key=name nameเก็บค่าHero
#     "age":18,
#     "gender":"male",
#     "color" : ["red","green","blue"]
# }
# print(dict)
# print(dict["name"]) #หาdict key=name
# print(dict["age"])
# print(dict["gender"])
# print(dict["color"][0]) #ระบุตำแหน่งlist


# #dict ซ้อน dict
# dict ={
#     "name" : {
#         "01": "khem",
#         "02": "ungpao",
#         "03": "nope",
#     }
# }
# print(dict["name"])
# print(dict["name"]["01"])

# dict ={
#     "name" : "khem"
# }
# dict["age"]=18 #การเพิ่มโดย append
# print(dict)

# dict = {
#     "name" : "khem",
#     "age" : 18,
#     "gender" : "male"
# }
# print(dict.keys()) #หาkeys เข้าไป
# print(dict.values()) #หาvalues


# import pandas as pd
# x=[1,2,3]
# df = pd.Series(x)
# print(df)


# import pandas as pd
# x=[1,2,3,4,5]
# df = pd.Series(x,index=["day1","day2","day3","day4","day5"])

# print(df)


# import pandas as pd
# x = {
#     "name" : "best",
#     "age" : "17",
#     "gender" : "male"
# }
# df= pd.Series(x)
# print(df)


#Pactices !!!!--------------------------------------------------------------------------------------------------------------------------

# #เอาแค่values 1 ตัวออกมาต้องทำยังไง
# dict={
#     "name" :"best",
#     "age" : "17",
#     "gender" : "male"
# }
# print(dict["name"])

# #ถ้าในdict มีlist เราจะprint valuesในlist 1 ตัว ยังไง
# dict={
#     "color" :["red","green","blue"]
# }
# print(dict["color"][0])

# #เราจะsearch เพื่อเช็คว่ามีข้อมูลใน dict รึเปล่า ใช้ifนะ
# x= input("อยากหาอะไร")

# dict ={
#     "name" : "best",
#     "age" : "17",
#     "gender" : "male"
# }
# if x in dict:
#     print(x+"is in dict")
#     print(dict[x])
# else:
#     print("it's not in dict")

# #เราจะเช็คว่ามีข้อมูลนี้อยู่ในvaluesรึเปล่า

# x= input("อยากหาอะไร : ")

# dict={
#     "name" : "best",
#     "age" : "17",
#     "gender" :"male"
# }
# if x in dict.values():
#     print(x,"is in dict")
# else:
#     print("it's not in dict")


# #print Smith
# jane = {
#   "people" : [
#     {
#        "firstName": "Joe",
#        "lastName": "Jackson",
#        "gender": "male",
#        "age": 28,
#        "number": "7349282382"
#     },
#     {
#        "firstName": "James",
#        "lastName": "Smith",
#        "gender": "male",
#        "age": 32,
#        "number": "5678568567"
#     },
#     {
#        "firstName": "Emily",
#        "lastName": "Jones",
#        "gender": "female",
#        "age": 24,
#        "number": "456754675"
#     }
#   ]
# }
# print(jane["people"][1]["lastName"])

# #ให้เช็คว่ามีผู้ชาย กี่คน ผู้หญิงกี่คน
# male=0
# female=0
# jane = {
#   "people" : [
#     {
#        "firstName": "Joe",
#        "lastName": "Jackson",
#        "gender": "male",
#        "age": 28,
#        "number": "7349282382"
#     },
#     {
#        "firstName": "James",
#        "lastName": "Smith",
#        "gender": "male",
#        "age": 32,
#        "number": "5678568567"
#     },
#     {
#        "firstName": "Emily",
#        "lastName": "Jones",
#        "gender": "female",
#        "age": 24,
#        "number": "456754675"
#     }
#   ]
# }
# # print(len("people"))
# for i in range(len("people")-3):
#     if jane["people"][i]["gender"] == "male":
#         male = male+1
#     else:
#         female = female +1
# print(male , female)


#print ชื่อและนามสกุล
# jane = {
#   "people" : [
#     {
#        "firstName": "Joe",
#        "lastName": "Jackson",
#        "gender": "male",
#        "age": 28,
#        "number": "7349282382"
#     },
#     {
#        "firstName": "James",
#        "lastName": "Smith",
#        "gender": "male",
#        "age": 32,
#        "number": "5678568567"
#     },
#     {
#        "firstName": "Emily",
#        "lastName": "Jones",
#        "gender": "female",
#        "age": 24,
#        "number": "456754675"
#     }
#   ]
# }


# # #ให้เรา print dataทั้งหมดที่ อยู่ในdict  โดยsort ตามnumber-----------------------------------------------------------------------------
# import pandas as pd
# jane = {
#   "people 1" : 
#     {
#        "firstName": "Joe",
#        "lastName": "Jackson",
#        "gender": "male",
#        "age": 28,
#        "number": "7349282382"
#     },"people 2":
#     {
#        "firstName": "James",
#        "lastName": "Smith",
#        "gender": "male",
#        "age": 32,
#        "number": "5678568567"
#     },"people 3":
#     {
#        "firstName": "Emily",
#        "lastName": "Jones",
#        "gender": "female",
#        "age": 24,
#        "number": "456754675"
#     }
# }
# list=[]
# # print(jane["people 1"]["number"])
# for i in range(3):
#     list.append(jane[str("people "+str(i+1))]["number"])
# list.sort()
# # print(list[2])
# for a in range(3): 
#     if list[a] in jane["people "+str(a+1)].values():
#        print(jane["people "+str(a+1)])

