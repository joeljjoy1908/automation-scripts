# identifying the phone number (india)
# Enter any sentence and find the mobile number from that
def isNumber(num):
    if num.isdecimal() :
        return True
    elif not num.isdecimal():
        return False
        
ph = input("Enter the sentence : ")
for i in range(len(ph)):
    val = ph[i:i+10]
    if len(val)== 10:
       if isNumber(val):
           print("The phone number found is : ",val) 

print("Done")