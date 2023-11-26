from copy import deepcopy
import pandas as pd
import matplotlib.pyplot as plt
import random
import math

# draws a scatterplot such that each cluster's points are in different colors 
oldCentroids=[]
def draw_clustered_graph(k, X, clusters, centroids):
  colors = ['r', 'g', 'b', 'y', 'c', 'm']
  fig, ax = plt.subplots()
  for i in range(k):
    xpoints = []
    ypoints = []
    for j in range(len(X)):
      if clusters[j] == i:
        xpoints.append(X[j][0])
        ypoints.append(X[j][1])
    ax.scatter(xpoints, ypoints, s=7, c=colors[i])
  xpoints = []
  ypoints = []
  for c in centroids:
    xpoints.append(c[0])
    ypoints.append(c[1])
  ax.scatter(xpoints, ypoints, marker='*', s=200, c='#050505')
  plt.savefig("clustered_graph.png")

data = pd.read_csv('customers.csv')
annualIncome = data['Annual Income']#x
spendingScore = data['Spending Score']#y

plt.scatter(annualIncome,spendingScore,s=7)
plt.savefig('before.png')

k = 5
points = list(zip(annualIncome,spendingScore))
centroids = []
clusters=[0]*len(points)

for i in range(k):
  centroids.append(random.choice(points))
  
while centroids!=oldCentroids:
  for i in range(len(points)):
    x,y=points[i]
    minDistance=math.inf
    for j in range(len(centroids)):
      centroidJ=centroids[j]
      distance=math.sqrt((x-centroidJ[0])**2+(y-centroidJ[1])**2)
      if distance<minDistance:
        minDistance=distance
        clusters[i]=j
  #print(centroids)
  oldCentroids=deepcopy(centroids)
  for i in range(k):
    group=[]
    for j in range(len(points)):
      if clusters[j]==i:
        group.append(points[j])
    xSum=0
    ySum=0
    for l in range(len(group)):
      x,y=group[l]
      xSum+=x
      ySum+=y
    #print(xSum,group,i,k)
    averageX=xSum/len(group)
    averageY=ySum/len(group)
    centroids[i]=(averageX,averageY)
draw_clustered_graph(k,points,clusters,centroids)
#print(centroids)
