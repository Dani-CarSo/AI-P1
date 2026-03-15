#LAB Modulo 2- Sección 3
# Own 
# Python essentials 2

def mysplit(strng):
    if strng.strip() == "":
        return []
    
    result = []
    word = ""
    in_word = False

    for char in strng:
        if in_word:
            if char != " ":
                word += char
            else:                    
                result.append(word)  
                word = ""            
                in_word = False      
        else:
            if char != " ":
                in_word = True
                word += char
            
    if word != "":
        result.append(word)
    
    return result

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))



        
