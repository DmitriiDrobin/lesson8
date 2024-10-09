grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
def average_of_lists(i):
    averages = []
    for sublist in i:
        if sublist:
            avg = sum(sublist) / len(sublist)
            averages.append(avg)
        else:
            averages.append(0)
    return averages
a = average_of_lists(grades)
# a = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])] - Изначально я планировал так, но мало ли какой список оценок попадется
l = list(students)
l.sort()
d = dict(zip(l, a))
print(d)