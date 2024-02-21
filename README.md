# Ant Colony Optimization
#### This is an implementation of Ant Colony Optimization Algorithm.
### **Reference**: Marco Dorigo, Thomas Stützle. *Ant Colony Optimization*. 2004.
### **DOI**: https://doi.org/10.7551/mitpress/1290.001.0001
### **ISBN electronic**: 9780262256032
## **Install**
```
pip install -r requirements.txt
```
```
python main.py
```
## **Change the configuration**
### You can change the configuration in *config/config.yml*
## **Traveling Salesman Problem (TSP)**
### One of the applications of ACO is solving TSP, which is a non-polynomial-hard optimization problem. In this case, we consider that a shipping unit needs to transport goods from one big warehouse to smaller warehouses. 
### ***Input***:
#### Set of coordinates of warehouses, including start point, such that the first coordinates is start point
### ***Output***:
#### List of ordering points, called route, such that the shipper needs to follow that route and a .html file shows the map like that:
![](/images/map.png) 
