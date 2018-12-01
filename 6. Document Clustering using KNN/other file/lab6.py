from pprint import pprint

class VectorSpaceModel(object):

    def __init__(self, doclist, termlist):
        self.docs = [doc.lower().strip(' ') for doc in doclist]
        self.terms = [term.lower() for term in termlist]
        self.tfmatrix = self.getTFMatrix(self.docs, self.terms)
        self.distmat = self.getEDMatrix()

    def getTFMatrix(self, docs, terms):
        tfmatrix = []
        for doc in docs:
            row = []
            for term in terms:
                x = doc.count(term)
                row.append(x)
            tfmatrix.append(row)
        return tfmatrix
    
    def getEuclideanDistance(self, v1, v2):
        n = len(v1)
        d = 0
        for i in range(n):
            d += (v1[i] - v2[i]) ** 2
        d = round(d ** 0.5, 2)
        return d
    
    def getEDMatrix(self):
        edmatrix = []
        for i in self.tfmatrix:
            row = []
            for j in self.tfmatrix:
                d = self.getEuclideanDistance(i, j)
                row.append(d)
            edmatrix.append(row)
        return edmatrix

    def getAverage(self, matrix):
        min = 99999
        max = 0
        for i in matrix:
            for j in i:
                if (j==0):
                    continue
                if (j<min):
                    min = j
                if (j>max):
                    max = j
        avg = round((min+max)/2, 2)
        return avg

    def getNeighbors(self, distmat):
        avg = self.getAverage(distmat)
        neighbors = {}
        ndocs = len(distmat)
        for i in range(ndocs):
            x = {}
            dsorted = sorted(distmat[i])
            dmin = 0
            for dist in dsorted:
                if dist!=0:
                    dmin = dist
                    break
            if dmin > avg:
                neighbors[str(i)] = x 
                continue
            for j in range(ndocs):
                if distmat[i][j]==dmin:
                    x[str(j)] = dmin
            neighbors[str(i)] = x
        return neighbors
    
    def getClusters(self, distmat):
        neighbors = self.getNeighbors(distmat)
        clusters = []
        for key in neighbors.keys():
            docid = int(key)
            if len(clusters)==0:
                cluster = [docid] + [int(x) for x in neighbors[key].keys()]
                clusters.append(cluster)
                continue
            for cluster in clusters:
                if docid in cluster:
                    
            
            



                
        
                    

        
doclist = ['Electric automotive maker Tesla Inc. is likely to introduce its products in India sometime in the summer of 2017', 'Automotive major Mahindra likely to introduce driverless cars', 'BMW plans to introduce its own motorcycles in India', 'Just drive, a self-drive car rental firm uses smart vehicle technology based on IOT', 'Automotive industry going to hire thousands in 2018', 'Famous cricket player  Dhoni brought his priced car Hummer which is an SUV', 'Dhoni led india to its second world cup victory' ,'IoT in cars will lead to more safety and make driverless vehicle revolution possible', 'Sachin recommended Dhoni for the indian skipper post']
termlist = ['Automotive', 'Car', 'Motorcycles', 'Self-drive', 'IOT', 'hire', 'Dhoni']

vsm = VectorSpaceModel(doclist, termlist)
print(vsm.docs)
print(vsm.terms)
for i in vsm.tfmatrix:
    print(i)
for i in vsm.distmat:
    print(i)
pprint(vsm.getNeighbors(vsm.distmat))