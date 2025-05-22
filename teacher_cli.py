class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Digite um comando: ")
            if command == "quit":
                print("Até logo!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")


class TeacherCLI(SimpleCLI):
    def __init__(self, teacher_crud):
        super().__init__()
        self.teacher_crud = teacher_crud
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)

    def create_teacher(self):
        name = input("Digite o nome: ")
        ano_nasc = int(input("Digite o ano de nascimento: "))
        cpf = input("Digite o CPF: ")
        self.teacher_crud.create(name, ano_nasc, cpf)

    def read_teacher(self):
        name = input("Digite o nome: ")
        self.teacher_crud.read(name)

    def update_teacher(self):
        name = input("Digite o nome: ")
        new_cpf = input("Digite o novo CPF: ")
        self.teacher_crud.update(name, new_cpf)

    def delete_teacher(self):
        name = input("Digite o nome: ")
        self.teacher_crud.delete(name)

    def run(self):
        print("Bem-vindo ao CLI do Professor!")
        print("Comandos disponíveis: create, read, update, delete, quit")
        super().run() 