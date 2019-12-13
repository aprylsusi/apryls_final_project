from apryls_final_project import __version__

def test_version():
    assert __version__ == '0.1.0'

    
from apryls_final_project.sad_attempt import judgy_python

def test_str4():
    #First test that a 4 character animal name will go result in "Interesting..." and not "Very original"
        assert judgy_python('cats')=='Interesting...'
        assert judgy_python('cats')=='Very original'

def test_str12():
    #Second test that a 12 character animal name will result in "I guess that's cool" and not "Are you even trying?"
        assert judgy_python('PIET-MY-VROU')=="I guess that's cool"
        assert judgy_python('PIET-MY-VROU')=="Are you even trying?"
        
def test_int7():
    #Third test that an integer of length 7 will give the result "Please enter a text response" and not "Very original"
        assert judgy_python(1234567)=="Please enter a text response"
        assert judgy_python(1234567)=="Very original"
        
def test_boo5():
    #Fourth test that a Boolean of length 5 will give the result "Please enter a text response" and not "Interesting..."
        assert judgy_python(False)=="Please enter a text response"
        assert judgy_python(False)=="Interesting..."
        