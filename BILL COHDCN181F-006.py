import sys

#Creating variables 
Disc =0
Dis_v = 0
tot = 0
count = 0

#Making a better output window using print options
print("\n")
print("\t\t\t--------BILL GENERATOR---------\n\n")
print('Enter your prices to the list and press "ENTER KEY" to quit the list \n\n\n')

price= input("Enter your item price : ")

#Use a while loop To print the price list 

while price:
    count = count +1 
    no = price
    try:
        no= float(price)
        if no < 0 :
            print("You entered a Minus Number, Please check the value")
        else :
            tot = tot + no
            
    except ValueError:                  #Error handling for invalid inputs
        error = sys.exc_info()[1]
        print ("Invalid input")

    price= input("Enter your item price: ")
    


#For calculate discount, We are using selections using if/elif                 
if tot >= 5000:
    Net_Tot = tot - (tot*0.15)
elif tot >= 3000:
    Net_Tot = tot - (tot*0.10)
elif tot >= 1000:
    Net_Tot = tot - (tot*0.05)
else:
    Net_Tot = tot 



#Print total amount and Net total

print("\n")
print("Total : ",tot)
print("Net Total :",Net_Tot)


#save Net total to a file called Sample.txt

f=open("Sample.txt", 'a+')
f.write("\n")
f.write(str(Net_Tot))
f.write("\n")
f.close()

                
          
                 
                 

    
