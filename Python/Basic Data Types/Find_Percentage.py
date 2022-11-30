n = int(input('Numero de alunos: ')) #numero de aluno
student_marks = [] #notas dos alunos 0<M<100
student_data = {} #informação alunos

for _ in range(n):
    name = str(input('Digite o nome: \n'))
    for i in range(0, 3):
        scores = float(input('Digite as notas:'))
        student_marks.append(scores)
        med = round(float(sum(student_marks)/len(student_marks)), 2)
    student_data[name] = med


query_name = input('Digite o nome desejado: ')
print(student_data[query_name])
