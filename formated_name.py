def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid input"
    formated_fname = f_name.title()
    formated_lname = l_name.title()
    return (f"{formated_fname} {formated_lname}")

print(format_name(input("What is your first name?"), input("what is your second_name?:")))