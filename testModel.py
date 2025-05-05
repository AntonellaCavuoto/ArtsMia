from model.model import Model

myModel = Model()
myModel.buildGraph()
# print("N nodi", myModel.getNumNodes(), "; N Edges:", myModel.getNumEdges())

myModel.getInfoConnessa(1234)
