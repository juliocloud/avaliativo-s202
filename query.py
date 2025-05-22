class Query:
    def __init__(self, database):
        self.db = database

    # Questão 1 ----------------------
    def get_professor_renzo(self):
        query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        results = self.db.execute_query(query)
        return [(result["ano_nasc"], result["cpf"]) for result in results]

    def get_professores_m(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
        results = self.db.execute_query(query)
        return [(result["name"], result["cpf"]) for result in results]

    def get_cidades(self):
        query = "MATCH (c:City) RETURN c.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_escolas_por_numero(self):
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS name, s.address AS address, s.number AS number"
        results = self.db.execute_query(query)
        return [(result["name"], result["address"], result["number"]) for result in results]
    
    # Questão 2 ----------------------
    def get_idade_mais_jovem_e_mais_velho(self):
        query = """
        MATCH (t:Teacher)
        RETURN min(t.ano_nasc) AS mais_jovem, max(t.ano_nasc) AS mais_velho
        """
        results = self.db.execute_query(query)
        return [(result["mais_jovem"], result["mais_velho"]) for result in results]

    def get_media_populacao(self):
        query = """
        MATCH (c:City)
        RETURN avg(c.population) AS media_populacao
        """
        results = self.db.execute_query(query)
        return [result["media_populacao"] for result in results]

    def get_cidade_cep_especifico(self):
        query = """
        MATCH (c:City {cep: '37540-000'})
        RETURN replace(c.name, 'a', 'A') AS nome_modificado
        """
        results = self.db.execute_query(query)
        return [result["nome_modificado"] for result in results]

    def get_terceira_letra_professores(self):
        query = """
        MATCH (t:Teacher)
        RETURN substring(t.name, 2, 1) AS terceira_letra
        """
        results = self.db.execute_query(query)
        return [result["terceira_letra"] for result in results]