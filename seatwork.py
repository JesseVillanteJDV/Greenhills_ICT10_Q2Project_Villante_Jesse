# Student club member checker
from pyscript import display, document

def student_club(e):
    document.getElementById("output").innerHTML = ''
    lastname = document.getElementById("last_name").value
    firstname = document.getElementById("first_name").value

    DMP_members = [('villante', 'jesse'), ('ortiz', 'josua'), ('estacio', 'raver'), ('valdez', 'santiago')]
    member_checker = (lastname.lower(), firstname.lower()) in DMP_members
    display_message = (
        f'Sorry, {firstname} {lastname}, your name is not on the list.',
        f'Congratulations, {firstname} {lastname}! You are now part of the Dark Mango Psychology Club.'
    )

    display(display_message[member_checker], target="outputseatwork")