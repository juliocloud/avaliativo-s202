from database import Database

class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        if self.read(name, silent=True):
            print(f"Erro: Professor {name} já existe no banco de dados.")
            return False

        try:
            query = "CREATE(:Teacher{name:$name, ano_nasc:$ano_nasc, cpf:$cpf})"
            parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
            self.db.execute_query(query, parameters)
            
            if self.read(name, silent=True):
                print(f"Professor {name} criado com sucesso!")
                return True
            else:
                print(f"Erro: Falha ao criar professor {name}.")
                return False
        except Exception as e:
            print(f"Erro ao criar professor: {str(e)}")
            return False

    def read(self, name, silent=False):
        try:
            query = "MATCH(t:Teacher{name:$name}) RETURN t"
            parameters = {"name": name}
            result = self.db.execute_query(query, parameters)
            
            if result:
                teacher = result[0]
                if not silent:
                    print(f"Professor encontrado:")
                    print(f"Nome: {teacher['t']['name']}")
                    # print(f"nome professor: {teacher['t']['nome']}")
                    print(f"Ano de Nascimento: {teacher['t']['ano_nasc']}")
                    print(f"CPF: {teacher['t']['cpf']}")
                return teacher
            
            if not silent:
                print(f"Professor {name} não encontrado.")
            return None
        except Exception as e:
            if not silent:
                print(f"Erro ao buscar professor: {str(e)}")
            return None

    def delete(self, name):
        if not self.read(name, silent=True):
            print(f"Erro: Professor {name} não encontrado.")
            print("verificando existencia professor >>>>>>>>>>>>>")
            return False

        try:
            query = "MATCH(t:Teacher{name:$name}) DETACH DELETE t"
            parameters = {"name": name}
            self.db.execute_query(query, parameters)
            
            if not self.read(name, silent=True):
                print(f"Professor {name} deletado com sucesso!")
                return True
            else:
                print(f"Erro: Falha ao deletar professor {name}.")
                return False
        except Exception as e:
            print(f"Erro ao deletar professor: {str(e)}")
            return False

    def update(self, name, newCpf):
        if not self.read(name, silent=True):
            print(f"Erro: Professor {name} não encontrado.")
            return False

        try:
            query = "MATCH(t:Teacher{name:$name}) SET t.cpf = $newCpf"
            parameters = {"name": name, "newCpf": newCpf}
            self.db.execute_query(query, parameters)
            
            teacher = self.read(name, silent=True)
            if teacher and teacher['t']['cpf'] == newCpf:
                print(f"CPF do professor {name} atualizado com sucesso!")
                return True
            else:
                print(f"Erro: Falha ao atualizar CPF do professor {name}.")
                return False
        except Exception as e:
            print(f"Erro ao atualizar professor: {str(e)}")
            return False 