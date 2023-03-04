# 208 L1E1
'''
1. Ask user for totalcost
2. Cal + display service charge
3. Cal + display GST
4. Display total cost
5. Ask no. of people
6. Cal + display amt. each person needs to play
'''

#######################
### INPUT VALIDATION ##
######################

###########
## FLOAT ##
###########

def parse_float(input):
        try:
                float(input)
                return True
        except:
                return False

#############
## INTEGER ##
#############

def parse_int(input):
        try:
                int(input)
                return True
        except:
                return False

############
### MAIN ###
###########

#####################
## GETTING VALUES ##
#####################

amt = input("How much was the meal? (no dollar sign): ") # Receipt cost
while not parse_float(amt): 
        totalamt = input("How much was the meal? (no dollar sign): ") # If not float / int ask again
amt = float(amt) # If pass get float

totalgst = input("How much GST is there? (%): ") # Amt of GST
while not parse_float(totalgst):
        totalgst = input("How much GST is there? (%): ") # If not float / int ask again
totalgst = 1 + (float(totalgst)/100) # If pass get float

totalsvc = input("How much SVC is there? (%): ") # Amt of SVC
while not parse_float(totalsvc):
        totalsvc = input("How much SVC is there? (%): ")# If not float / int ask again
totalsvc = 1 + (float(totalgst)/100) # If pass get float

##################
## CALCULATING ##
#################

withsvc = amt * totalsvc # Amount with service charge
withgst = withsvc * totalgst # Amount with GST
totalamt = round(withgst, 3)

print(f"Total cost: {round(totalamt, 2)}") #total cost
print(f"Total GST: {round(totalamt-amt, 2)}") #GST total cost
print(f"Total SVC: {round(amt*totalsvc-amt, 3)}") #SVC total cost
nopeople = input("Number of people: ")
while not parse_int(nopeople):
        nopeople = input("Number of people: ")
nopeople = int(nopeople)
amtperperson = round(withgst / nopeople, 2)
print(amtperperson)