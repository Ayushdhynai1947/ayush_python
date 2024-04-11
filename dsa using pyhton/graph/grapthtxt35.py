"  a graph consisits of two things "
"- a set V elments called node"
'''a set E of edgs such that each eage e is E is identified wuth a unique (unorder ) pair [u,v] of nodes is V ,denoted by e = [u,v]
    we indicate the parts of the graph by writing G =(V,E)'''
    
    
    
    
    
    
    
    
    
    
    
# impimentaion of grph using adjecent martix 

class Graph:
    def __init__(self,vno) -> None:
        self.vertex = vno
        self.adj_matrix =[[0]*vno for e in range(vno)]
        
    def add_edge(self,u,v,weight=1):
        if 0
        