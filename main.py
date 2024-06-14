import time
import streamlit as sl
import pandas as pd

form =sl.form("Form1")
form.text_input('Label 1')
form.form_submit_button("Submit")

col1, col2= sl.columns(2)
col1.text_input('test 1')
col2.text_input('test 2')


with sl.sidebar:
    with sl.echo():
        sl.write("This code will be printed to the sidebar.")

    with sl.spinner("Loading..."):
        time.sleep(5)
    sl.success("Done!")

#sl.sidebar.write('SIdebar')


table= pd.DataFrame({"Col 1": [1,2,3,4,5], "Col 2": [18,28,38,48,58], "Col 1": [1,2,3,4,5]})
sl.slider('Slider')
sl.table(table)
sl.dataframe(table)
textInput = sl.text_input('Input')
sl.write(textInput)

sl.metric(label='Temperature', value="30C", delta="-3C")
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


sl.json({"a": "b"})

sl.code("""SELECT field1 FROM table GROUP BY field1""", "sql")

sl.write("## ooo")