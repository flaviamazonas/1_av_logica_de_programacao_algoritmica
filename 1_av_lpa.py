def calcular_resumo_turma ():

    qtd_turmas = int(input("Quantas turmas existem na faculdade? "))

    linha = '-' * 50
    print(linha)

    for turma in range(1, qtd_turmas + 1):
        
        nome_turmas = input("\n Informe o nome da turma: ")
        print(f"\n TURMA {nome_turmas}")

        qtd_disciplinas = int(input("Quantas disciplinas são cursadas nesta turma? "))
        qtd_alunos = int(input("Quantos alunos estão nesta turma?  "))

        maior_media_turma = 0
        menor_media_turma = float ('inf')
        media_geral_turma = 0
        soma_media_turma = 0
        qtd_alunos_aprovados = 0
        qtd_alunos_reprovados = 0
        qtd_alunos_na_final = 0
        somatorio_media_geral = 0

        for disciplina in range(1, qtd_disciplinas + 1):

            media_geral_disciplina = 0
            maior_media_disciplina = 0
            menor_media_disciplina = float ('inf')
            qtd_alunos_reprovados_disciplina = 0
            qtd_alunos_final_disciplina = 0
            qtd_alunos_aprovados_disciplina = 0
            
            nomeDisciplina = input("\n Informe o nome da disciplina: ")

            for aluno in range(1, qtd_alunos + 1):

                nota1av = float(input(f"\n Qual a nota da 1° avaliação do aluno {aluno} na disciplina {nomeDisciplina} : "))

                nota2av = float(input(f"Qual a nota da 2° avaliação do aluno {aluno} na disciplina {nomeDisciplina} : "))

                media_aluno = (nota1av + nota2av) / 2

                media_geral_turma = soma_media_turma /qtd_disciplinas
                
                soma_media_turma += media_geral_disciplina

                media_geral_disciplina += media_aluno

                if media_aluno > maior_media_disciplina:
                    maior_media_disciplina = media_aluno

                if media_aluno < menor_media_disciplina:
                    menor_media_disciplina = media_aluno

                if media_aluno < 4:
                    qtd_alunos_reprovados_disciplina += 1

                elif media_aluno < 7:
                    qtd_alunos_final_disciplina += 1

                else:
                    qtd_alunos_aprovados_disciplina += 1

            somatorio_media_geral += (media_geral_disciplina / qtd_alunos)

            print("\n RESUMO DA DISCIPLINA ")
            print(f"Disciplina: {nomeDisciplina}")
            print(f"Quantidade total de alunos: {qtd_alunos}")
            print(f"A média na disciplina é: {media_geral_disciplina / qtd_alunos:.2f}")
            print(f"A maior média da disciplina foi: {maior_media_disciplina:.2f}")
            print(f"A menor média da disciplina foi: {menor_media_disciplina:.2f}")
            print(f"Quantidade de alunos reprovados: {qtd_alunos_reprovados_disciplina}")
            print(f"Quantidade de alunos na final: {qtd_alunos_final_disciplina}")
            print(f"Quantidade de alunos aprovados: {qtd_alunos_aprovados_disciplina}")

            soma_media_turma += media_geral_disciplina
            
            if maior_media_disciplina > maior_media_turma:
                maior_media_turma = maior_media_disciplina

            if menor_media_disciplina < menor_media_turma:
                menor_media_turma = menor_media_disciplina

            qtd_alunos_reprovados += qtd_alunos_reprovados_disciplina
            qtd_alunos_na_final += qtd_alunos_final_disciplina
            qtd_alunos_aprovados += qtd_alunos_aprovados_disciplina

        print(f"\n RESUMO DA TURMA: {nome_turmas}")
        print(f"A média geral da turma é: {somatorio_media_geral / qtd_disciplinas:.2f}")
        print(f"A maior média da turma é: {maior_media_turma:.2f}")
        print(f"A menor média da turma é: {menor_media_turma:.2f}")
        print(f"Quantidade de alunos reprovados na turma: {qtd_alunos_reprovados}")
        print(f"Quantidade de alunos na final da turma: {qtd_alunos_na_final}")
        print(f"Quantidade de alunos aprovados na turma: {qtd_alunos_aprovados}")

        soma_media_turma += soma_media_turma
        if maior_media_turma > maior_media_turma:
            maior_media_turma = maior_media_turma

        if menor_media_turma < menor_media_turma:
            menor_media_turma = menor_media_turma

        qtd_alunos_reprovados += qtd_alunos_reprovados
        qtd_alunos_na_final += qtd_alunos_na_final
        qtd_alunos_aprovados += qtd_alunos_aprovados

calcular_resumo_turma ( )