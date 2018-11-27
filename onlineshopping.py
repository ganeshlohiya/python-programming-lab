# Title : online Shopping
# Ganesh Lohiya
# M 36


from easygui import * # import easygui library
import sys
while 1:    # while loop
 msgbox("welcome to online shopping")    
 msg="which site would you prefer"   # msg to be viewed
 title="online shopping"             # title for choice box
 choices=["amazon","snapdeal","flipkart","myntra"] # choices to be made available
 choice=choicebox(msg, title, choices) 
 msgbox("you choose:" + str(choice), "please press ok")
 if choice=="amazon":     # using if loop, the rest of the code can be made by using the same format
  msg1="what would you like to purchase"
  title1="diwali sale"
  choices1=["electronics","clothing","groceries","furniture"]
  choice1=choicebox(msg1,title1,choices1)
  if choice1=="electronics":
   msg2="what type of product do you want"
   title2="electronic"
   choices2=["mobile","laptop","earphones","speakers"]
   choice2=choicebox(msg2,title2,choices2)
   if choice2=="mobile":
    msg3="which mobile do you want?"
    title3="mobiles"
    choices3=["samsung","one plus","i phone","mi"]
    choice3=choicebox(msg3,title3,choices3)
    if choice3=="samsung":
     msg4="choose your model"
     title4="samsung"
     choices4=["samsung galaxy s9+","samsung note 8","samsung galaxy a 8","samsung galaxy j 7"]
     choice4=choicebox(msg4,title4,choices4)
     if choice4=="samsung galaxy s9+":
       msgbox("vendor1 offers a price of 72000 Rs.\nvendor2 offers a price of 71500 Rs.\nvendor3 offers a price of 72500 Rs.")
     elif choice4=="samsung note 8":
       msgbox("vendor1 offers a price of 53000 Rs.\nvendor2 offers a price of 52500 Rs.\nvendor3 offers a price of 53500 Rs.")
     elif choice4=="samsung galaxy a 8":
       msgbox("vendor1 offers a price of 30000 Rs.\nvendor2 offers a price of 29500 Rs.\nvendor3 offers a price of 30500 Rs.")
     elif choice4=="samsung galaxy j 7":
       msgbox("vendor1 offers a price of 13000 Rs.\nvendor2 offers a price of 12500 Rs.\nvendor3 offers a price of 13500 Rs.")
     else:                            # end window will show 3 vendors offering their prices for the corresponding object
       sys.exit(0)
    elif choice3=="one plus":
     msg5="choose your model"
     title5="one plus"
     choices5=["one plus 3","one plus 3t","one plus 5","one plus 6"]
     choice5=choicebox(msg5,title5,choices5)
     if choice5=="one plus 3":
      msgbox("vendor1 offers a price of 28000 Rs.\nvendor2 offers a price of 27500 Rs.\nvendor3 offers a price of 28500 Rs.")
     elif choice5=="one plus 3t":
      msgbox("vendor1 offers a price of 25000 Rs.\nvendor2 offers a price of 25500 Rs.\nvendor3 offers a price of 24500 Rs.")
     elif choice5=="one plus 5":
      msgbox("vendor1 offers a price of 30000 Rs.\nvendor2 offers a price of 30500 Rs.\nvendor3 offers a price of 29500 Rs.")
     elif choice5=="one plus 6":
      msgbox("vendor1 offers a price of 36000 Rs.\nvendor2 offers a price of 35500 Rs.\nvendor3 offers a price of 36500 Rs.")
     else:
      sys.exit(0)
    elif choice3=="i phone":
     msg6="choose your model"
     title6="i phone"
     choices6=["i phone 6","i phone 6s","i phone 8","i phone x"]
     choice6=choicebox(msg6,title6,choices6)
     if choice6=="i phone 6":
      msgbox("vendor1 offers a price of 31000 Rs.\nvendor2 offers a price of 31500 Rs.\nvendor3 offers a price of 30500 Rs.")
     elif choice6=="i phone 6s": 
      msgbox("vendor1 offers a price of 30000 Rs.\nvendor2 offers a price of 30500 Rs.\nvendor3 offers a price of 29500 Rs.")
     elif choice6=="i phone 8":
      msgbox("vendor1 offers a price of 70000 Rs.\nvendor2 offers a price of 70500 Rs.\nvendor3 offers a price of 69500 Rs.")
     elif choice6=="i phone x":
      msgbox("vendor1 offers a price of 95000 Rs.\nvendor2 offers a price of 95500 Rs.\nvendor3 offers a price of 94500 Rs.")
     else:
      sys.exit(0)
    elif choice3=="mi":
     msg7="choose your model"
     title7="mi"
     choices7=["mi note 4","mi note 4 pro","mi note 5","mi not 5 pro"]
     choice7=choicebox(msg7,title7,choices7)
     if choice7=="mi note 4":
      msgbox("vendor1 offers a price of 13000 Rs.\nvendor2 offers a price of 12500 Rs.\nvendor3 offers a price of 13500 Rs.") 
     elif choice7=="mi note 4 pro":
      msgbox("vendor1 offers a price of 14000 Rs.\nvendor2 offers a price of 13500 Rs.\nvendor3 offers a price of 14500 Rs.")
     elif choice7=="mi note 5": 
      msgbox("vendor1 offers a price of 15000 Rs.\nvendor2 offers a price of 14500 Rs.\nvendor3 offers a price of 15500 Rs.")
     elif choice7=="mi note 5 pro":
      msgbox("vendor1 offers a price of 16000 Rs.\nvendor2 offers a price of 15500 Rs.\nvendor3 offers a price of 16500 Rs.")
     else:
      sys.exit(0)      
   elif choice2=="laptop":
    msg4="which laptop do you want?"
    title4="laptops"
    choices4=["dell vostro","apple mac book air","lenovo ideapad","micromax lapbook"]
    choice4=choicebox(msg4,title4,choices4)
    if choice4=="dell vostro":
     msgbox("vendor1 offers a price of 30300 Rs.\nvendor2 offers a price of 30800 Rs.\nvendor3 offers a price of 29800 Rs.")
    elif choice4=="apple mac book air": 
     msgbox("vendor1 offers a price of 63000 Rs.\nvendor2 offers a price of 62500 Rs.\nvendor3 offers a price of 63500 Rs.")
    elif choice4=="lenovo ideapad":
     msgbox("vendor1 offers a price of 45000 Rs.\nvendor2 offers a price of 44500 Rs.\nvendor3 offers a price of 45500 Rs.")
    elif choice4=="micromax lapbook":
     msgbox("vendor1 offers a price of 10500 Rs.\nvendor2 offers a price of 11000 Rs.\nvendor3 offers a price of 10000 Rs.")
    else:
     sys.exit(0)
   elif choice2=="earphones":
    msg8="which earphones do you want?"
    title8="earphones"
    choices8=["mi earphones","jbl earphones","boat earphones","sony earphones"]
    choice8=choicebox(msg8,title8,choices8)
    if choice8=="mi earphones":
     msgbox("vendor1 offers a price of 600 Rs.\nvendor2 offers a price of 650 Rs.\nvendor3 offers a price of 700 Rs.")
    elif choice8=="jbl earphones":
     msgbox("vendor1 offers a price of 800 Rs.\nvendor2 offers a price of 850 Rs.\nvendor3 offers a price of 750 Rs.")
    elif choice8=="boat earphones":
     msgbox("vendor1 offers a price of 1000 Rs.\nvendor2 offers a price of 1050 Rs.\nvendor3 offers a price of 950 Rs.")
    elif choice8=="sony earphones":
     msgbox("vendor1 offers a price of 1500 Rs.\nvendor2 offers a price of 1400 Rs.\nvendor3 offers a price of 1600 Rs.")
    else:
     sys.exit(0)
   elif choice2=="speakers":
    msg9="which speaker do you want?"
    title9="speakers"
    choices9=["jbl speakers","iball speakers","boat speakers","philips speakers"]
    choice9=choicebox(msg9,title9,choices9)
    if choice9=="jbl speakers":
     msgbox("vendor1 offers a price of 2700 Rs.\nvendor2 offers a price of 2600 Rs.\nvendor3 offers a price of 2800 Rs.")
    elif choice9=="iball speakers":
     msgbox("vendor1 offers a price of 900 Rs.\nvendor2 offers a price of 1000 Rs.\nvendor3 offers a price of 800 Rs.")
    elif choice9=="boat speakers":
     msgbox("vendor1 offers a price of 3000 Rs.\nvendor2 offers a price of 3100 Rs.\nvendor3 offers a price of 2900 Rs.")
    elif choice9=="philips speakers":
     msgbox("vendor1 offers a price of 2000 Rs.\nvendor2 offers a price of 1900 Rs.\nvendor3 offers a price of 2100 Rs.")
    else:
     sys.exit(0)
  elif choice1=="clothing":
   msg1="which cloth do you want"
   title1="clothes"
   choices1=["t-shirt","jeans","jacket","shorts"]
   choice1=choicebox(msg1,title1,choices1)
   if choice1=="t-shirt"
    msg2="which brand do you want"
    title2="t-shirt"
    choices2=["levis","adidas","wrogn","being human"]
    choice2=choicebox(msg2,title2,choices2)
    if choice2=="levis"
     msgbox("vendor1 offers a price of 870 Rs.\nvendor2 offers a price of 850 Rs.\nvendor3 offers a price of 900 Rs.")
    elif choice2=="adidas"
     msgbox("vendor1 offers a price of 2000 Rs.\nvendor2 offers a price of 1900 Rs.\nvendor3 offers a price of 1800 Rs.")
    elif choice2=="wrogn"
     msgbox("vendor1 offers a price of 1500 Rs.\nvendor2 offers a price of 1400 Rs.\nvendor3 offers a price of 1600  Rs.")
    elif choice2=="being human"
     msgbox("vendor1 offers a price of 1200 Rs.\nvendor2 offers a price of 1100 Rs.\nvendor3 offers a price of 1300 Rs.")
    else:
     sys.exit(0)
   elif choice1=="jeans":
    msg3="which brand do you want?"
    title3="jeans"
    choices3=["levis","diesel","wrangler","pepe jeans"]
    choice3=choicebox(msg3,title3,choices3)
    if choice3=="levis"
     msgbox("vendor1 offers a price of 3500 Rs.\nvendor2 offers a price of 3400 Rs.\nvendor3 offers a price of 3600 Rs.")
    elif choice3=="diesel"
     msgbox("vendor1 offers a price of 15000 Rs.\nvendor2 offers a price of 17000 Rs.\nvendor3 offers a price of 19000 Rs.")
    elif choice3=="wrangler":
     msgbox("vendor1 offers a price of 2500 Rs.\nvendor2 offers a price of 2700 Rs.\nvendor3 offers a price of 2900 Rs.")
