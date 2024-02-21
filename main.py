from src.graph import Graph
from src.algorithm import BasicAS, EAS, RankBasedAS, MMAS, ACS
from src.utils import readData
import random
import numpy
position, names = readData(r"data\J&T_Coordinates.csv")
numVertices = len(position)
print(numVertices)
verticesPosition = numpy.asarray(position)
graph = Graph(numVertices=numVertices, position=verticesPosition)
graph.setNames(names=names)
aco = ACS(graph=graph, configPath=r"config\config.yml")
bestRoute, bestScore = aco.optimize()
print("Best route: ", bestRoute)
print("Best score: ", bestScore)
graph.visualizeCircular(route=bestRoute, path="./map/" + str(aco) + ".html")
with open("result.txt", mode="a") as f:
    f.write(str(aco) + "," + str(bestScore) + "\n")
