#Tell python your favorite animal and get an opinion and your lottery numbers
def judgy_python (animal):
    name_length = 0    
    for i in animal: 
        name_length += 1    
    If 0 <= name_length <=1: 
        return "Are you even trying?"
    Elif 2 <= name_length <= 3:
        return "Embarassing choice"
    Elif 4 <= name_length <= 6:
        return "Interesting..."
    Elif 7 <= name_length <= 10:
        return "Very original"
    Elif 11 <= name_length <= 15:
        return "I guess that's cool"
    Else:
        return "That's not even real"

judgy_python("bat")



def judgy_python (animal):
    name_len = len(animal)    
    if name_len <= 1: 
        response="Are you even trying?"
    elif name_len <= 3:
        response="Embarassing choice"
    elif name_len <= 6:
        response="Interesting..."
    elif name_len <= 10:
        response="Very original"
    elif name_len <= 15:
        response="I guess that's cool"
    else:
        response="That's not even real"
    return response
judgy_python("bat")
judgy_python("23")


#12/11/19
def judgy_python (animal):
    name_type= type(animal)
    if name_type==str:
        name_len = len(animal)
        if name_len <= 1: 
            response="Are you even trying?"
        elif name_len <= 3:
            response="Embarassing choice"
        elif name_len <= 6:
            response="Interesting..."
        elif name_len <= 10:
            response="Very original"
        elif name_len <= 15:
            response="I guess that's cool"
        else:
            response="That's not even real"
    else:
        response= "Please enter a text response"
    return response 

#judgy_python('carttoogf')
judgy_python(23)