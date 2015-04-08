# M.Celeste PYTHON to HTML Conversion 
# Is there a better way to create a header?


def generate_HTML(header,title, description):
    text_1 = ''' 
    <div> 
        ''' + header
    text_2 = '''
    </div>
    
    <p class="one">
        ''' + title
    text_3 = '''
    </p>
    <div class="description">
        ''' + description
    text_4 = '''
    </div>
</div>'''
    full_text = text_1 + text_2 + text_3 + text_4
    return full_text

def make_HTML(concept):
    header = concept[0]
    title = concept[1]
    description = concept[2]
    return generate_HTML(header,title, description)



STAGE_TWO_UNIT_TWO = [ ['<h1>Stage 2: Unit 2 </h1>','<h3>Why Python!<h3>', '<p>Python is better for writing programs than a natural language like English. <br> The problem with natural languages is that they are <b> ambiguous </b>. Hence, not everyone will interpret the same phrase the same way. <br> Another problem with natural language is that they are very <b> verbose </b>. You want your programs to be short so it is less work to write them, and so that it is easier to read and understand them. <p/>'],
                             ['','<h3>Grammer in python<h3/>', '<p> Compared to a natural language, programming languages adhere to a <b> strict grammatical structure</b>.<br> When programming language grammar is not followed the interpreter will return a <b>SyntaxError</b> message. This means that the structure of the code is inconsistent with the rules of the programming language.<p/>'],
                             ['','<h3>"Backus-Naur Form</h3>', '<p>The notation we used to describe the grammar is known as <b> Backus-Naur Form </b>, which was introduced in the 1950s by John Backus, the lead designer of the Fortran programming language at IBM.<br> The purpose of Backus-Naur Form is to describe a programming language in a <b> simple and concise manner</b>.<p/>'] ]

STAGE_TWO_UNIT_THREE = [ ['<h1>Stage 2: Unit 3 </h1>','<h3>Variables<h3>', '<p>A <b> variable </b> is a name that refers to a value. In Python, we can use any sequence of letters and numbers and underscores (_)when we want to make a variable name, so long as it does not start with a number.<p>To introduce a new variable, we use an assignment statement:<b> Name = Expression </b></p><br><p><b> Variables Can Vary </b> - The value a variable refers to can change. When a variable name is used, it always refers to the last value assigned to that variable<p/>'],
                             ['',',h3> Comments <h3>','We use the hash mark (#) to introduce a comment. After the hash, we can write anything we want. The rest of the line is treated as a comment. The comment is not interpreted by the Python interpreter, but it is useful for humans reading the code. <p/>'],
                             ['','<h3>"Strings</h3>', '<p>A <b>string</b> is a sequence of characters surrounded by quotes, either single or double.The only requirement is that the string must start and end with the same kind of quote.<p/>'],
                             ['','<h3>"Functions</h3>', '<p><b> Procedures or Functions </b> - a way to package code so it can be reused with different inputs.</p>'],
                             ['','<h3>"IF/OR Statements</h3>', '<p>An if statement provides a way to control what code executes based on the result of a test expression.</p>'],
                             ['','<h3>"While Loops</h3>', '<p>Loops are a way of executing something over and over.</p>']]
                             
STAGE_TWO_UNIT_FOUR = [ ['<h1>Stage 2: Unit 4 </h1>','<h3>Strutured Data <h3>', '<p>A string is considered a kind of structured data because you can break it down into its characters and you can operate on sub-sequences of a string. This unit introduces <b> lists </b>, a more powerful and general type of structured data. Compared to a string where all of the elements must be characters, in a list the elements can be anything you want such as characters, strings, numbers or even other lists!<p/>'],
                             ['',',h3> Lists <h3>','<p>Elements are characters surround by a singled or double quotes, immutable, and will not change the value of the string</p>'],
                             ['','<h3>"Nested List</h3>', '<p>All of the elements in our lists have been of the same type: strings, numbers, etc. However, there are no restrictions on the types of elements in a list. Elements of a list can be any type you want, you can also mix and match different types of elements in a list.<p/>'],
                             ['','<h3>"Mutations</h3>', '<p><b>Mutation</b> means changing the value of an object. Lists support mutation. This is the second main difference between strings and lists.</p>'],
                             ['','<h3>"Aliasing</h3>', '<p><b>Aliasing </b>is when there are two names that refer to the same object. Aliasing is very useful, but also can be very confusing since one mutation can impact many variables. If something happens that changes the state of the object, it affects the state of the object for all names that refer to that object.</p>'],
                             ['','<h3>"List Operations</h3>', '<p>A list object has a number of member methods. These can be grouped arbitrarily into transformations, which change the list, and information, which returns a fact about a list.There are many built-in operations on lists. Use the Python Reference for help!</p>']]
def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML
    

print make_HTML_for_many_concepts(STAGE_TWO_UNIT_TWO)
print make_HTML_for_many_concepts(STAGE_TWO_UNIT_THREE)
print make_HTML_for_many_concepts(STAGE_TWO_UNIT_FOUR)



