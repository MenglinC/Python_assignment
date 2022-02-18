'''
@author: Wesley Wang 
@Date:Sat Oct 16 2021
@Function:Interaction with the users and make judgement
'''
# import the module that we create
import code_check as ck

# initialize
code_message ="Please enter code(digits only)(enter 0 to quit):"
code_input ="True"
Basic = []
Position =[]
UPC = []
NoN = []

# judge 
while code_input!="0":
    code_input =input(code_message) #accept the input from the users :string
    if code_input!="0":
        allfalse = [ck.Basic_code(code_input),ck.Positional_code(code_input),ck.UPC_code(code_input)] # the key part if all false 
        if ck.Basic_code(code_input):
            print(f'--code:{code_input} vaild Basic code.')
            Basic.append(code_input)
        if ck.Positional_code(code_input):
            print(f'--code:{code_input} vaild Position code.')
            Position.append(code_input)
        if ck.UPC_code(code_input):
            print(f'--code:{code_input} vaild UPC code.')
            UPC.append(code_input)
        if not any(allfalse): #if do not satisfy the all conditions abrove
            print(f'--code:{code_input} not Basic,Position or UPC code.')
            NoN.append(code_input)
            
# ouput:
print("\n\n")
print("Summary")
if Basic:
    str_Basic = ",".join(str(i) for i in Basic)
    print(f'Basic:{str_Basic}')
else:
    print("Basic:None")

if Position:
    str_Position = ",".join(str(i) for i in Position)
    print(f'Position:{str_Position}')
else:
    print("Position:None")

if UPC:
    str_UPC = ",".join(str(i) for i in UPC)
    print(f'UPC:{str_UPC}')
else:
    print("UPC:None")

if NoN:
    str_NoN = ",".join(str(i) for i in NoN)
    print(f'None:{str_NoN}')
else:
    print("None:None")

