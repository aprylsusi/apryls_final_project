#User defined function incorporating 
#12/11/19
def judgy_python (animal):
    """Tell Python what your favorite animal is and it will give you excellant feedback on your choice.
        First created on 12/5/2019."""
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