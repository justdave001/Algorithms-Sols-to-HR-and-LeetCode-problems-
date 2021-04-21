
grades_count = int(input().strip())
grades = []
for i in range(grades_count):
    item = int(input().strip())
    grades.append(item)

def grading(grades):
   for j in grades:
       
       if j%5 != 0 and (((j-(j%5)+5)-j)<3) and j>=38:
           newj = grades.index(j)
           grades[newj] =(grades[newj] - (grades[newj]%5))+5
       
       else:
           newj = grades.index(j)
           grades[newj] = grades[newj]
   listToStr = ' '.join(map(str, grades))
   for k in grades:
     print(k)
if __name__ == "__main__":
     grading(grades)
