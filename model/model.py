import networkx as nx

from database.DAO import DAO
from model.aeroporto import Aeroporto


class Model:
    def __init__(self):
        self._graph=nx.Graph()
        self._aeroporti=[]
        self._idMapA={}


    def buildGraph(self, dist_min):
        self._graph.clear()
        self._aeroporti=DAO.get_all_airports()
        for a in self._aeroporti:
            self._idMapA[a.ID]=a
        #self._graph.add_nodes_from(self._aeroporti) --> SE FACESSI COSì PRENDEREI PIU' NODI DI QUELLI REALI
        archi=DAO.get_all_edges(dist_min, self._idMapA)
        #LASCIO CREARE I NODI DAGLI ARCHI
        for a in archi:
            self._graph.add_edge(a[0], a[1], weight=a[2])
    def getAllEdges(self):
        dettagli=[]
        for a in self._graph.edges(data=True):
            dettagli.append((a[0], a[1], a[2]["weight"]))
        return dettagli

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)
