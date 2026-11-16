"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 7
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number is one or more'

    assert conclusion == 'Number is one or more'

def test_if_elif_nested():
    """IF nested statement"""

    number = -1000
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
        if number < -100:
         conclusion = 'Number is also less than -100'
        elif number < -10:
            conclusion='Number is smaller than -10 but bigger than -100'

    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        if number <0.5:
            conclusion = 'Number is smaller than 0.5 too'
        elif number < 0.8 & number > 0.7:
            conclusion ='Number is between 0.7 and 0.8'
        else : 
            conclusion ='Number is bigger than 0.5 but smaller than one'
    else:
        conclusion = 'Number bigger than or equal to one'
        if number >100 : 
            conclusion ='Number is bigger than 100'
        else:
            conclusion = 'Number is smaller than 100 '

    assert conclusion == 'Number is also less than -100'

def test_if_elif():

    expected = 'i like apples'
    

    if expected == 'i like apples':
        number = 12
    elif expected =='i like dogs':
        number = 74
    elif expected =='i like cats':
        number = 86
    elif expected =='i like oranges':
        number = 53
    elif expected =='i like juice':
        number = 21
    elif expected =='i like planes':
        number = 51
    assert number == 12


def test_if_nested():

    number = 58
    

    if number >0:
        minimum =0
        if number >10:
            minimum = 10
            if number >20:
                minimum = 20
                if number > 30:
                    minimum = 30
                    if number > 40:
                        minimum = 40
                        if number > 50:
                            minimum = 50
                            if number > 60:
                                minimum = 60
                                if number > 70:
                                    minimum = 70
                                    if number > 80:
                                        minimum = 80
    
    
    
    assert minimum == 50

test_if_elif()
print('test 1 passed')
test_if_elif_nested()
print('test 2 passed')
test_if_nested()
print('test 3 passed')
test_if_statement()
