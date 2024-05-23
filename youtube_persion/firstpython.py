
#colors=["red","blue","green","white"]
#numbers=[1,2,55,74,32]
#for color in colors:
    #print(color.count('e'))
#print("pink" in colors)    
#for index,color in enumerate(colors):
    #print(index,color)
#print('//'.join(colors))
#message='red//blue//green//white'
#print(message.split('//'))
#colors_tup=('red','blue','blak','green')
#print(dir(colors_tup))
#print(colors_tup.index('blak'))
#colors_set1={'red','blue','black','green'}
#print(type(colors_set))
#numbers=[44,34,54,65,44,54]
#print(len(numbers))
#print(set(numbers))
#print(len(set(numbers)))
#colors_set2={'red','blue','white'}
#print(colors_set1.union(colors_set2))
#print(colors_set1 & colors_set2)
#print(colors_set1 - colors_set2)
#print(colors_set1.difference(colors_set2))
#car={'brand':'ford','model':'mostang','year':'1997','color':['red','blue']}
#car['brand']='porsh'
#car.update({'brand':'porshe','model':'makan'})
#del car['model']
#car.pop('brand')
#print(car.values())
#for key,value in car.items():
    #print(key,'_____',value)
#name='maryam'
#languge='python'
#x=300
#if x<200:
# print('increas')
#elif 200<x<250:
# print("it's ok") 
#else:
# print('decrees') 
#num1=float(input("adad aval ra vared kon:"))
#num2=float(input("adad dovom ra vared kon:"))
#oper=input("amaliat ra vared kon:")
#print(num1,num2,oper)
#print("natije:")
#if oper=='+':
 #   print(num1+num2)
#elif oper=='*':
 #   print(num1*num2)
#elif oper=='/':
 #   print(num1/num2)
#elif oper=='-':
 #   print(num1-num2)
#else:
 #   print("amaliate vared shode motabar nist")        
# itemsdata=open("test","r")        
#  #print(itemsdata.readlines())
# for item in itemsdata.readlines():
#      print(item)
# itemsdata.close()
# with open("test2","w") as itemsdata:
#     itemsdata.write("\nitem 5\nitem 7")
#     filedata=itemsdata.readlines()
# for item in filedata:
#     print(item)
# import math
# import os
# filename="IMG_1768.JPG"
# print(os.path.join(path,filename))
# import mypakeyg
# print(mypakeyg.fun(13,2))
# class students:
#     def __init__(self,firstname,lastname,year,score):
#         self.firstname=firstname
#         self.lastname=lastname
#         self.year=year
#         self.score=score
# from studentcla import student
# student1=student("artin","mousavi",1997,17)
# student2=student("mahan","hashempoor",2010,19)
# print(student1.firstname)
# print(student1.lastname)
# print(student1.fullname())
from question import question
question_prompts=["what is 12+13?\n(a)15\n(b)23\n(c)25\n\n",
                  "what is 24*2?\n(a)21\n(b)48\n(c)100\n\n"
                  ,"what is 41-9?\n(a)32\n(b)11\n(c)30\n\n"]

questions=[question(question_prompts[0],"c"),
           question(question_prompts[1],"b"),
           question(question_prompts[2],"a")]
def takequize():    
    score=0
    for question in questions:
        user_answer=input(question.prompt)
        if user_answer==question.answer:
            score=score+1
    print("your score: ",score)        
takequize()    