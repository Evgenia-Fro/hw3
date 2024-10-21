students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list=list(students)
print(students_list)
students2=sorted(students_list)
print(students2)
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
result = dict(zip(students2, grades))
print(result)
results = sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])
average_grades = {students2[0]: results[0], students2[1]: results[1], students2[2]: results[2], students2[3]: results[3], students2[4]: results[4]}
print(average_grades)