rm = input("Insira seu RM ")
idade = input("Insira sua idade ")
if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno de RM {}".format(rm))
    print("Mais informações serão enviadas para seu email cadastrado!")
else:
    autorizado = input("Você possui autorização dos responsáveis para participar? S - SIM ou N = NÃO ")
    if autorizado == 'S':
        print('Sua participação foi autorizada, aluno de RM {}".format(rm)')
        print("Mais informações serão enviadas para o email dos responsáveis!")
    else:
        print("Sua participação não foi autorizada por causa da sua idade")