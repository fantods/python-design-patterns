# defines a skeleton of a base algorithm
# deferring definition of exact steps to subclasses
# used in Django class based views

# Pros:
# client can override parts of algorithm without issue
# put duplicated code into superclass

# Cons:
# can be limited by provided skeleton
# harder to maintain when more steps exist

def get_text(): 
    return "plain-text"

def get_pdf():
    return "pdf"

def get_csv():
    return "csv"

def convert_to_text(data):
    print("CONVERTING")
    return f"{data} as text format"

def saver():
    print("SAVING")

def template_function(getter, converter=False, to_save=False):
    data = getter()
    if len(data) <= 3 and converter:
        data = converter(data)
    else:
        print("Skipping conversion")
    
    if to_save:
        saver()
    
    print(f"{data} was processed")


template_function(get_text, to_save=True)
# Skipping conversion
# SAVING
# plain-text was processed
template_function(get_pdf, converter=convert_to_text)
# CONVERTING
# pdf as text format was processed
template_function(get_csv, to_save=True)
# Skipping conversion
# SAVING
# csv was processed