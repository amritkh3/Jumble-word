"""
1.import random and generate random number from 1 to 5 and assign it ot a variable play.
2.ask user to input the 5 digit word and assign it to variable ui
3.assign 5 variable with name var1 ,var2 ,var3,var4, var5 and give them the value with
jumbled index no of ui
4.use if condition when the play(random number)is 1 print var1 and ask second player
to guess the word and assign it to a variable ui1.
5.use while conditin uner if statement
    if ui is equal to ui the n print congratulation and break.
    else ask user to guess the number for two more time
    here ,tries refer to no of tries
6.use elif when the play is 2 ,3 ,4 and 5 and repeat same steps for all situations .   
   
"""

import random
play=random.randint(1,5)
ui=input("enter any word ")
var1=ui[3]+ui[0]+ui[2]+ui[4]+ui[1]
var2=ui[0]+ui[4]+ui[3]+ui[1]+ui[2]
var3=ui[1]+ui[4]+ui[2]+ui[0]+ui[3]
var4=ui[2]+ui[1]+ui[3]+ui[0]+ui[4]
var5=ui[4]+ui[2]+ui[3]+ui[1]+ui[0]
if play==1:
     print(var1)
     tries=0
     while tries<3: 
         ui1=input("guess your word ")
         if ui1!=ui:
              print("sorry, its not the right word")
         else:
              print("congratulation, you guess the right word")
              break
         tries=tries+1
elif play==2:
     print(var2)
     tries=0
     while tries<3:
         ui1=input("guess your word ")
         if ui1!=ui:
              print("sorry, its not the right word")
         else:
              print("congratulation, you guess the right word")
              break
         tries=tries+1
elif play==3:
     print(var3)
     tries=0
     while tries<3:
          ui1=input("guess your word ")
          if ui1!=ui: 
               print("sorry, its not the right word")
          else:
             print("congratulation, you guess the right word")
             break
          tries=tries+1
elif play==4:
     print(var4)
     tries=0
     while tries<3:
         ui1=input("guess your word ")
         if ui1!=ui:
              print("sorry, its not the right word")
         else: 
               print("congratulation, you guess the right word")
               break
         tries=tries+1 
else:
      print(var5)
      tries=0
      while tries<3:
          ui1=input("guess your word ")
          if ui1!=ui:
               print("sorry, its not hte right word")
          else:
               print("congratulation,you guess the right word")
               break
          tries=tries+1    
            
            
     
