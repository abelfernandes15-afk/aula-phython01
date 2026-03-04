
aluno ={}
# entrada de dados 
aluno['nome']= input('digite o nome do aluno:')
aluno['nota'] = float(input('digite nota'))
aluno['curso']= input('digite o curso do aluno')
# saida de dados 
print(f'o nome do aluno e: {aluno ['nome']}')
print(f'o curso do aluno e :{aluno['curso']}')
print(f'aprovado' if aluno ['nota']>= 18 else 'reprovado')