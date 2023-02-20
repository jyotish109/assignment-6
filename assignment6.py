from functools import reduce
#******************* Q1 ************************
l=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
l.sort(key = lambda x: x[1])
print(list(l))

#******************* Q2 **************************
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqrt=lambda l: l**2
print(list(map(sqrt,l)))

#****************** Q3 ******************************
l= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tpl=lambda l: str(l)  
print(tuple(map(tpl,l)))

#***************** Q4 ********************************
l=[]
[l.append(i) for i in range(1,26)] #use of comprehension
print(l)
print(reduce(lambda x,y: x*y,l))

#******************* Q5 ******************************
l=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
print(list(filter(lambda x:x%2==0 and x%3==0,l)))

#********************* Q6 *****************************
string=['python', 'php', 'aba', 'radar', 'level']
print(list(filter(lambda x:  (x == "".join(reversed(x))), string  )))
