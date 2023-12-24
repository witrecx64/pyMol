import mol_basic

while True:
    text = input('mol++: ')
    result, error = mol_basic.run(text)
    
    
    if error: print(error.as_string())   
    else: print(result) 