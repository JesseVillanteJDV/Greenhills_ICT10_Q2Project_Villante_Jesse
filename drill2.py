from pyscript import display, document

grade7 = {'Kaiser Chua', 'John Smith', 'Josua Oritz'}
grade8 = {'Brent Something', 'Ukwatte Hanz', 'Sancho Mercado'}
grade9 = {'Nayeon Kim', 'Eliana Daclan', 'Kristine Manabat'}
grade10 = {'Jesse Villante', 'Zangief Briones', 'Cedric Visorde', 'Mohammad Calaca'}

members = grade7 | grade8 | grade9 | grade10
def add_member(event):
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value
    members.add(first + " " + last)

    document.getElementById("outputdrill").innerHTML = f"{members} Total Members: {len(members)}"