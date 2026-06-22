from model.model import Model

mymodel=Model()
mymodel.buildGraph(4000)
print(mymodel.getGraphDetails())
#print(mymodel.getAllEdges())