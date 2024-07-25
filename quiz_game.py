from random import shuffle
qas = [
    ("what is the capital of india:", "New Delhi"),
    ("Whais the capital of Pakistan:", "Islamabad"),
    ("Whais the capital of Neapal:", "Kathmandu"),
    ("Whais the capital of Iran:", "Tehran"),
    #("Whais the capital of Srilanka:", "Columbo"),
    #("Whais the capital of Bangladesh:", "Dhaka"),
    #("Whais the capital of Russia:", "Mosco"),
    #("Whais the capital of :England", "London"),
    #("Whais the capital of china:", "Beijing"),
    #("Whais the capital of japan:", "Tokyo"),
]
shuffle(qas)
numRight = 0
for question,  right_ans in qas:
    ans = input(question + ' ')
    if ans.title() == right_ans:
        print("Right!")
        numRight +=1
    else:
        print("No the answer is", right_ans)
print(f"You gave {numRight} right answers and {len(qas) - numRight} wrong answers")
