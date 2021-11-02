# import numpy as np

# aray1=np.array([0,1,2,3,4,5,6])
# aray2=np.array([[0,1,2,3],[4,5,6]])

# print(aray1)
# print(aray2)

# import numpy as np
  
# aray2=np.array([[1,2,3],[4,5,6]])  #แสดง 1 - 6 โดยที่ไม่มีกรอบ

# for a in range(2):
#     for i in range(3):
#         print(aray2[a,i])

# import numpy as np

# aray2=np.array([[1,2,3],[4,5,6]]) 
# aray3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])   #แสดง 1- 9 โดยที่ไม่ให้มีกรอบ
# for a in range(2):
#     for i in range(3):
#         print(aray2[a,i])

# for a in range(3):
#     for i in range(3):
#         print(aray3[0,a,i])

# import numpy as np
# aray2=np.array([[1,2,3],[4,5,6]]) 
# aray3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])  
# print(aray2.ndim) #ndim คือ การระบุมิติ
# print(aray3.ndim)

# import numpy as np  #slicing array หลายมิติ
# aray1=np.array([1,2,3])
# aray2=np.array([[1,2,3],[4,5,6]]) #2มิติ
# aray3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])  #3มิติ
# #หา5
# print(aray2[1,1])

# #หา9
# print(aray3[0,2,2])

# import numpy as np  

# aray3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])  #3มิติ
# #output
# #0[1,2,3]
# #00[4,5,6]
# #000[7,8,9]
# s="0"
# for i in range(3):
#     for a in range(i+1):
#         print(s,end="")
#     print(aray3[0,i])
# print()


# import numpy as np  

# aray3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])  #3มิติ
# #output
# #000[1,2,3]
# #00[4,5,6]
# #0[7,8,9]
# s="0"
# for i in range(3):
#     for a in range(3-i):
#         print(s,end="")
#     print(aray3[0,i])
# print()

# import numpy as np  

# aray3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])  #3มิติ
# #output
# #0[1,2,3]
# #00[4,5,6]
# #000[7,8,9]
# #000[7,8,9]
# #00[4,5,6]
# #0[1,2,3]
# s="0"
# for i in range(3):
#     for a in range(i+1):
#         print(s,end="")
#     print(aray3[0,i])
# for c in range(3):
#     for b in range(3-c):
#         print(s,end="")
#     print(aray3[0,int(2-c)])

# import numpy as np  

# aray3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])  #3มิติ#เอาแบบไม่มีกรอบ
# #output
# #0 1 2 3 
# #00 4 5 6 
# #000 7 8 9 
# #000 7 8 9 
# #00 4 5 6 
# #0 1 2 3 
# s="0"
# for i in range(3):
#     for a in range(i+1):
#         print(s,end="")
#     for e in range(3):
#         print(aray3[0,i,e],end=" ") #คำสั่งend=""คือการที่จะให้สิ่งที่เราprintมา ให้อยู่กับบรรทัด ล่าสุด
#     print()
   
# for c in range(3):
#     for b in range(3-c):
#         print(s,end="")
#     for f in range(3):
#         print(aray3[0,int(2-c),int(f)],end=" ")
#     print()

# import numpy as np
# aray2=np.array([[1,2,3],[4,5,6]])
# aray3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])

# print(aray2.shape)#อันที่1คือlenชั้นแรก  อันที่2คือด้านในlenนั้นๆมีกี่อัน ถ้ามีอันที่3ก็ต้องlenอันที่3ด้วย
# print(aray3.shape)

# import numpy as np
# aray2=np.array([[1,2,3],[4,5,6]])
# for x in np.nditer(aray2):  ##นำสมาชิกด้านในออกมาทั้งหมด
#     print(x)


# import numpy as np
# # aray2=([1,2,3,4,5,6])#list ไม่มีคำสั่งreshape ต้องใช้ array เท่านั้น
# aray1=np.array([[2,3,4,5],[6,7,8,9]])

# # x=aray2.reshape(2,3)#อันที่1คือจำนวนlist อันที่2 คือ จำนวนสมาชิกในlist
# # print(x.reshape)
# print(aray1.reshape(4,2))

# import numpy as np
# from numpy import random

# x= random.randint(100,size=(3,5))
# print(x)