alist = []

for i in range(int(input("Enter number of students: "))):
    name = input("Enter name: ")
    score = float(input("Enter score: "))
    alist.append([name, score])


second_highest = sorted(set([score for name, score in alist]))[1]


names_with_second = sorted([name for name, score in alist if score == second_highest])


print('\n'.join(names_with_second))
