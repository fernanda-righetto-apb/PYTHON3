# Herança de Classe
# não permite que acesse de fora a classe -> dois underlines __
# consigo sobrescrever -> um underline _

# superclasse - classe pai e subclasses - classes filhas - herança entre classes => uma classe pai, e faz com que as classes filhas herdem características comuns

class Programa:
    def __init__(self,nome,ano):
        self._nome=nome.title()
        self.ano=ano
        self._likes=0

    # preparar entrada de informação
    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes+=1

    @property
    def nome(self):
        return self._nome

    # pra poder sobrescrever
    @nome.setter
    def nome(self,nome):
        self._nome=nome     


class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        # referencia a classe programa que quero herdar informações, herdar especificamente os métodos
        super().__init__(nome,ano)
        self.duracao=duracao

class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome,ano)
        self.temporadas=temporadas
        

filme1=Filme('star wars',1977,132)
filme1.dar_likes()
filme1.dar_likes()
print(f'Nome: {filme1.nome} - Ano: {filme1.ano} - Duração: {filme1.duracao} minutos - Likes: {filme1.likes}')

serie1=Serie('Greys Anatomy',2005,20)
serie1.dar_likes()
serie1.dar_likes()
serie1.dar_likes()
print(f'Nome: {serie1.nome} - Ano: {serie1.ano} - Temporadas: {serie1.temporadas} - Likes: {serie1.likes}')