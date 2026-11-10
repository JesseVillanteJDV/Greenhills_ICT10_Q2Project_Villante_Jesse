from pyscript import display, document
#all the non-metal elements with their info
elements = {
    'Na':['Sodium', 11, 22.990],
    'Mg':['Magnesium', 12, 24.305],
    'Al':['Aluminum', 13, 26.982],
    'Fe':['Iron', 26, 55.845],
    'Cu':['Copper', 29, 63.546],
    'Au':['Gold', 79, 196.967],
    'H':['Hydrogen', 1, 1.008],
    'He':['Helium', 2, 4.0026],
    'Li':['Lithium', 3, 6.941],
    'C':['Carbon', 6, 12.011],
    'N':['Nitrogen', 7, 14.007],
    'O':['Oxygen', 8, 15.999],
    'I':['Iodine', 53, 126.904],
    'Og':['Oganesson', 118, 294],
    'Ts':['Tennessine', 117, 294],
    'Ar':['Argon', 18, 39.948],
    'Ne':['Neon', 10, 20.179],
    'Rn':['Radon', 86, 220],
    'At':['Astatine', 85, 210],
    'Kr':['Krypton', 36, 83.798],
    'Se':['Selenium', 34, 78.971],
    'Br':['Bromine', 35, 79.904],
    'Cl':['Chlorine', 17, 35.453],
    'P':['Phosphorus', 15, 30.974],
    'F':['Fluorine', 9, 18.998],
}

#finds the element based on whats inputed
def search_element(event):
    symbol = event.target.value.capitalize()
    element = elements.get(symbol, ['No Element Like That', '-', '-'])

    #(Ai helped me here) this clears the previous result
    output_div = document.querySelector("#outputskillstest")
    output_div.innerHTML = ""

    #gives the new result
    display(f'Element Symbol: {symbol}', target='outputskillstest')
    display(f'Element Name: {element[0]}', target='outputskillstest')
    display(f'Atomic Number: {element[1]}', target='outputskillstest')
    display(f'Atomic Mass: {element[2]}', target='outputskillstest')