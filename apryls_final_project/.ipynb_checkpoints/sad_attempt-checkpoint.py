#User defined function incorporating a user generated function, if-then-else and return statements, and length and type functions
#12/12/19
def judgy_python (animal):
    """Tell Python what your favorite animal is and it will give you excellant feedback on your choice.
        First created on 12/5/2019."""
    name_type= type(animal)
    #Only give a response if a text string is entered, otherwise, request a text string
    if name_type==str:
        name_len = len(animal)
        #Give feedback on animal selection based on the length of the name
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
        #If the lenth is 16 or above, there's a pretty good chance that an animal wasn't actually entered
        #In the event that it actually is a real animal name, it's still fun to question it.
        else:
            response="That's not even real"
    #For responses that are not text strings
    else:
        response= "Please enter a text response"
    return response 

#These were just for testing and to show how to call the function
#judgy_python('carttoogf')
#judgy_python(23)