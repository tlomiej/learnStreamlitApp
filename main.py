import streamlit as sl


sl.title("Hello world!")
sl.markdown('''---''')
sl.text('''curcilu wite sdf
        dsf
        slsd
        f

        ZeroDivisionErrorfs
        sdfsf''')
sl.text("curcilu wite sdfsf")
sl.text("curcilu wite sdfsf")

sl.subheader('Hi I am a co')
sl.header('I a header')
sl.text("curcilu wite sdfsf")

sl.markdown(''' **Hello** world
            
            - test
            - test
            
            
            ''')

for x in range(10):
    sl.latex(r"{}^2 + b^2 = c^2".format(x))