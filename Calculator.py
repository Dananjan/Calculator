history_list=[]
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  print("8.History  : ? ")
  

  # take input from the user
  choice = str(input("Enter choice(+,-,*,/,^,%,#,$,?): "))
  print(choice)
  list_other=['$','#']
  list_arithmatic=['+','-','*','/','^','%']
  if choice in list_other:
    if choice=='$':
      continue
    else:
      #program ends here
      print("Done. Terminating")
      exit()
  elif choice in list_arithmatic:
      a=input("Enter first number: ")
      print (a)
      if '$' in str(a):
        continue
      b=input("Enter second number: ")
      print(b)
      if '$' in str(b):
        continue
      if a=='#' or b=='#':
        print("Done. Terminating")
        exit()
      try:
        x=float(a)
        y=float(b)
        if choice=='+':
          print(x,'+',y,'=',(x+y))
          o=str(x)+' + '+str(y)+" = "+str(x+y)
          history_list.append(o)
        elif choice=='-':
          print(x,'-',y,'=',(x-y))
          o=str(x)+' - '+str(y)+" = "+str(x-y)
          history_list.append(o)
        elif choice=='*':
          print(x,'*',y,'=',(x*y))
          o=str(x)+' * '+str(y)+" = "+str(x*y)
          history_list.append(o)
        elif choice=='/':
          if y==0:
            print("float division by zero")
            print(x,'/',y,'= None')
            o=str(x)+' / '+str(y)+" = "+'None'
            history_list.append(o)
          else:
            print(x,'/',y,'=',(x/y))
            o=str(x)+' / '+str(y)+" = "+str(x/y)
            history_list.append(o)
        elif choice=='^':
            print(x,'^',y,'=',x^y)
            o=str(x)+' ^ '+str(y)+" = "+str(x^y)
            history_list.append(o)
        elif choice=='%':
            print(x,'%',y,'=',x%y)
            o=str(x)+' % '+str(y)+" = "+str(x%y)
            history_list.append(o)
      except:
        print("Not a valid number,please enter again")
  elif choice=="?":
    if len(history_list)>0:
      for element in history_list:
          print(element)
    else:
      print("No past calculations to show")
  else:
    print ("Unrecognized operation")
    
