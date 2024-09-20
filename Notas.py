# Notas dos Alunos
Camila = float(input('Qual foi a nota da Camila? '))
Junior = float(input('Qual foi a nota do Junior? '))
Carlos = float(input('Qual foi a nota do Carlos? '))
Kleber = float(input('Qual foi a nota do Kleber? '))
Sophia = float(input('Qual foi a nota da Sophia? '))
Everton = float(input('Qual foi a nota do Everton? '))
Carla = float(input('Qual foi a nota da Carla? '))
Kaique = float(input('Qual foi a nota do Kaique? '))
Otavio = float(input('Qual foi a nota do Otávio? '))
Daniela = float(input('Qual foi a nota da Daniela? '))
Maria = float(input('Qual foi a nota da Maria? '))
Vitoria = float(input('Qual foi a nota da Vitória? '))
Jesus = float(input('Qual foi a nota do Jesus? '))
Amirah = 5

def verificar_nota(nome, nota):
    if nota < 4:
        print(f'{nome}: Aluno Reprovado')
    elif nota < 6:
        print(f'{nome}: Recuperação')
    else:
        print(f'{nome}: Aprovado')

# Verificando as notas
verificar_nota('Camila', Camila)
verificar_nota('Junior', Junior)
verificar_nota('Carlos', Carlos)
verificar_nota('Kleber', Kleber)
verificar_nota('Sophia', Sophia)
verificar_nota('Everton', Everton)
verificar_nota('Carla', Carla)
verificar_nota('Kaique', Kaique)
verificar_nota('Otávio', Otavio)
verificar_nota('Daniela', Daniela)
verificar_nota('Maria', Maria)
verificar_nota('Vitória', Vitoria)
verificar_nota('Jesus', Jesus)
verificar_nota('Amirah', Amirah)
