class Vertice(object):

    total_vertices = 0
    identificacao = 1

    def __init__(self, nome):
        self.nome = nome
        self.id = Vertice.identificacao
        Vertice.identificacao += 1
        self.grau = 0

    def __str__(self):
        return "Vertice: %s || Grau: %s || Identificação: %s" % (self.nome, self.grau, self.id)



class Aresta(object):

    total_arestas = 0
    identificacao = 1

    def __init__(self, vertice_a, vertice_b, peso=1):
        vertice_a.grau += 1
        vertice_b.grau += 1
        self.vertice_pai = vertice_a
        self.vertice_mae = vertice_b
        self.peso = peso
        self.id = Aresta.identificacao
        Aresta.identificacao += 1


    def __str__(self):
        return "Aresta %s || Entre os vertices %s e %s" % (
            self.id, self.vertice_pai.id, self.vertice_mae.id
        )

#
class Grafo(object):

    def __init__(self):
        self.v_list = []
        self.a_list = []

    def add_vertice(self, vertice_a):
        self.v_list.append(vertice_a)
        return "Vertice adicionado"

    def add_aresta(self, aresta_a):
        self.a_list.append(aresta_a)
        return "Aresta adicionada"

    def del_vertice(self, vertice_a):
        if vertice_a in self.v_list:
            self.v_list.remove(vertice_a)
            return "Vertice removido"
        else:
            return "Vertice não encontrado"

    def del_aresta(self, aresta_a):
        if aresta_a in self.a_list:
            self.a_list.remove(aresta_a)
            return "Aresta removida"
        else:
            return "Aresta não encontrada"