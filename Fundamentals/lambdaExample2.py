
#regular funcation
#def average(sequence):
#    return sum(sequence)/len(sequence)

def printResult(function):
    operations_function = operations[function]
    print(f"{function} : ",operations_function(grades))

#lambda function
total = lambda seq: sum(seq)
average = lambda seq: sum(seq) / len(seq)
top = lambda seq: max(seq)

operations = {
    "average": average,
    "total": total,
    "top": top
}

students = [
    {"name":"Itamar","grades":(67,80,45,99)},
    {"name":"Bonny","grades":(34,80,45,99)},
    {"name":"Claide","grades":(67,78,45,99)},
    {"name":"Maximus","grades":(67,80,66,99)},
    {"name":"Ota","grades":(67,33,45,44)}
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print("==================")
    print(f"Student: {name}")
    print(average(grades))
    print(total(grades))
    print(top(grades))

    #or

    print("<improved>")

    printResult("average")
    printResult("total")
    printResult("top")