from database import Database
from query import Query
from setup import setup_database
from teacher_crud import TeacherCRUD
from teacher_cli import TeacherCLI
from configuracao import DB_URL, DB_USER, DB_PASSWORD

# Faz as criações iniciais no banco 
setup_database()

db = Database(DB_URL, DB_USER, DB_PASSWORD)
query = Query(db)

print("\n>>> Questão 1 <<<\n")

print("Professor Renzo:")
print(query.get_professor_renzo())

print("\nProfessores com nome iniciado por 'M':")
print(query.get_professores_m())

print("\nCidades:")
print(query.get_cidades())

print("\nEscolas com número entre 150 e 550:")
print(query.get_escolas_por_numero())

print("\n>>> Questão 2 <<<\n")

print("Idade mais jovem e mais velha:")
print(query.get_idade_mais_jovem_e_mais_velho())

print("\nMédia de população das cidades:")
print(query.get_media_populacao())

print("\nCidade com CEP específico:")
print(query.get_cidade_cep_especifico())

print("\nTerceira letra dos professores:")
print(query.get_terceira_letra_professores())

print("\n>>> Questão 3 <<<\n")

teacher_crud = TeacherCRUD(db)

print("Criando professor Chris")
teacher_crud.create("Chris Lima", 1956, "189.052.396-66")

print("\nLendo informações do professor Chris")
teacher_crud.read("Chris Lima")

print("\nAtualizando CPF do professor Chris")
teacher_crud.update("Chris Lima", "162.052.777-77")

print("\nLendo informações do professor Chris")
teacher_crud.read("Chris Lima")

print("\nIniciando CLI do Professor")
cli = TeacherCLI(teacher_crud)
cli.run()

db.close()