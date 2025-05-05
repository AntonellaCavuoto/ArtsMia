from database.DAO import DAO
from model.model import Model

listObjects = DAO.getAllNodes()
myModel = Model()
myModel.buildGraph()

edges = DAO.getAllArchi(myModel.getIdMap())

print(len(listObjects))
print(len(edges))
