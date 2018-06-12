import sys

my_file = open(sys.argv[1], 'rb')      #Take the file name as a command line argument  
file = my_file.read()
txt= file
						
txt=txt.strip()						
my_file.close()							
        
string=""						#Convert ASCII to Hex and split to 4 Hex digits	
for a in str(txt): 
	string=string+str(hex(ord(a)))[2::]				 
string=string+"0a"
           
count= 0								
string2=""							
for b in str(string):
	count=count+1
	string2=string2+b
	if count%4==0:
		string2=string2+" "


my_file = open(sys.argv[1], 'r')                        #replace spaces with a dots
file = my_file.read()
rep = str.replace(file, ' ', '.')

       
print("000000 : "+string2,"\n",rep, sep ="  ")
                    

#This was the best I could come up with.

