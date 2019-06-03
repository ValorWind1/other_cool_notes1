"""
decorators : @

they are use to *** extends the behavior***  of a function, without modifying the function

"""

def chant_dec(function):

    def function_wrapper():
        #code before function
        print("*chant*")

        function()

        # code after function
        print("*chant*")

    return function_wrapper


@chant_dec
def question():
    print("grant us eyes")

@chant_dec
def answer():
    print("join us subordinate!")


question()

answer()