# -*- coding: utf-8 -*-
# @Time:6/24/2021 5:22 PM
# @Author:xiaoyuqing
# @File: MyGraph.py
'''
封装图构建与深度优先遍历方法
'''
from pythonds.graphs import Graph, Vertex
import os
import time
path_dir =str(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
strTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
cases_filename = 'cases_%s.txt' % strTime
cases_dir = path_dir + '\\data\\Cases\\%s' % cases_filename

class MyGraph(Graph):
    #在构建函数中创建图
    def __init__(self, data = None):
        super().__init__()
        self.vertexs = list(data.keys())
        self.time =0

        #定义传入data结构为嵌套字典
        if data:
            l_vertexs = list(data.keys())
            #edge:{nbr1:weight1, nbr2:weight2,...}
            l_egdes = list(data.values())
            #添加顶点
            for vertex in l_vertexs:
                self.addVertex(vertex)
            #添加边
            for vertex in l_vertexs:
                edge = data[vertex]
                nbrs = list(edge.keys())
                for nbr in nbrs:
                    weight = edge[nbr]
                    self.addEdge(vertex, nbr, weight)
                    print('graph is building: %s -> %s -> %s' % (vertex, weight, nbr))
        else:
            print('请传入构图所需数据！')

    def dfs(self):
        #获取顶点值列表
        vertices= self.getVertices()
        #定义顶点对象列表
        vertexList = []
        for vt in vertices:
            #根据顶点值获取顶点类对象，存入列表
            vertexList.append(self.getVertex(vt))
        for avertex in vertexList:
            route = []
            if avertex.getColor() == 'white':
                self.dfs_recursive(avertex, route)

    #深度优先遍历递归方式
    def dfs_recursive(self, startvertex, route):
        question = startvertex.id
        for nextvertex in startvertex.getConnections():
            weight = startvertex.getWeight(nextvertex)
            path = '%s->%s' % (question, weight)
            route.append(path)
            self.dfs_recursive(nextvertex, route)
            route.pop()
        startvertex.setColor('black')
        route.append(question)
        route_str = '->'.join(route)
        if not startvertex.getConnections():
            with open(cases_dir, 'a+', encoding='utf-8') as f:
                f.writelines(route_str + '\n' + '\n')
            print('traversing graph: %s' % route_str + '\n')
        if len(route) >= 1:
            route.pop()

if __name__ == '__main__':
    testdata ={'v0':{'v1':1,'v2':2,'v3':3}, 'v1':{'v4':4,'v5':6}, 'v2':{'v4':7,'v5':8,'v6':9}}
    g = MyGraph(testdata)
    g.dfs()
