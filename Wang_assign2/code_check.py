'''
@author:Wesley Wang 
@Date:Sat Oct 16 2021
@function:Consist of the functions that determine if the input code is vaild and which type
'''

# Basic code judgement
def Basic_code(code_input):
    code = code_input.strip() #remove potential indent
    code_last = code[-1] #the last chr is make sense
    lent = len(code) #the maximum for while cycle
    sum_code = 0
    i = 0
    while i < (lent-1):
        sum_code = sum_code + int(code[i])
        i = i+1
    sum_modulo = str(sum_code % 10 ) #calculate the modulo
    if code_last == sum_modulo :
        return True
    else:
        return False
        
# Positional code judgement
def Positional_code(code_input):
    code = code_input.strip()
    code_last = code[-1]
    sum_code = 0
    i = 0
    lent = len(code)
    while i < (lent-1) :
        i = i + 1
        sum_code = sum_code + i*int(code[i-1]) 
    sum_modulo = str(sum_code % 10 )
    if code_last == sum_modulo :
        return True
    else:
        return False

# UPC code judgement
def UPC_code(code_input):  
    code = code_input.strip()
    code_last = code[-1]
    sum_code = 0
    i = 0
    lent = len(code)
    while i < (lent-1) :
        i = i + 1
        if i % 2 ==1: # odd 
            sum_code = sum_code + 3*int(code[i-1])
        else: #even
            sum_code = sum_code + 1*int(code[i-1])
                   
    sum_modulo = str(sum_code % 10 )
    if sum_modulo == code_last:
        if sum_modulo == "0":
            return True
        else:
            return False
    else:
        cosum = str(int(sum_modulo)+int(code_last))
        if cosum == "10":
            return True
        else:
            return False

