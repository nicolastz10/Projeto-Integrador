##Tarefacil

dias_da_semana = {
    'segunda feira': [],
    'terca feira': [],
    'quarta feira': [],
    'quinta feira': [],
    'sexta feira': [],
    'sabado': [],
    'domingo': []
}

organizadorUser = []

def registerUser():
    UserName = input("Digite seu nome completo:")
    UserEmail = input("Digite seu E-mail:")
    UserPassword = input("Crie sua senha:")

    newUser = {}
    newUser['Name'] = UserName
    newUser['Email'] = UserEmail
    newUser['Password'] = UserPassword

    organizadorUser.append(newUser)

def adicionar_tarefa(dia, tarefa):
    if dia.lower() in dias_da_semana:
        dias_da_semana[dia.lower()].append(tarefa)

    else:
        print("Dia da semana inadequado.")


def minha_rotina(dia):
    if dia.lower() in dias_da_semana:
        tarefas = dias_da_semana[dia.lower()]
        if tarefas:
            print("Tarefas para {dia}:")
            contador = 1

            for tarefa in tarefas:
                print(contador, ") ", tarefa)
                contador += 1

        else:
            print("Não há tarefas agendadas para {dia}.")
    else:
        print("Dia da semana inadequado!")


while True:
    print("\nOrganizador de rotina ")
    print('1 Cadastrar Usuario')
    print("2. Adicionar tarefa")
    print("3. Mostrar rotina de um dia")
    print("4. Sair")

    Option = int(input("Digite sua opção:"))

    if Option == 1:
        registerUser()

    if Option == 2:
        dia = input("Digite o dia da semana para adicionar a tarefa: ")
        tarefa = input("Digite sua tarefa:")
        adicionar_tarefa(dia, tarefa)

    if Option == 3:
        dia = input("Digite o dia da semana para mostrar a rotina:")
        minha_rotina(dia)

    if Option == 4:
        print("Obrigado meu nobre.")
        break


