#!/usr/bin/python

import math
import random
import numpy as np

def dist(x0,x1,y0,y1):
    return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)

#-----------------------------------------------------------------------------
def length(n1, n2):
    """Compute the distance between two nodes"""
    return dist(n1.x, n2.x,n1.y,n2.y)



#-----------------------------------------------------------------------------
#
class Node( object ):
    def __init__( self, id, x, y ):
        self.id  = id
        self.sid = None
        self.x   = x
        self.y   = y
        self.taken = False
        self.cluster = None

    def __str__( self ):
        out = str( self.id ) + " {} {}".format( self.x, self.y )
        return out

#-----------------------------------------------------------------------------
def dump( nodes, solution ):
    with open( 'solution.csv', 'w' ) as f:
        f.write( 'xx,yy,cl\n' )
        for n in solution:
            f.write( str( n.x ) + ',' + str( n.y ) + ',' + str( n.cluster ) + '\n' )
        n = solution[0]
        f.write( str( n.x ) + ',' + str( n.y ) + ',' + str( n.cluster ) + '\n' )

#-----------------------------------------------------------------------------
def id2node(nodes, idx0):
    return nodes[idx0]

def total_length(nodes, solution ):
    """Compute the total distrance travelled for the given solution"""
    if  isinstance(solution[0], Node):
        useidx=False
    else:
        useidx=True
    objective = 0
    for index in range(0, len(solution)):
        a=index
        b=(index+1) % len(solution)
        if useidx:
            na=id2node(nodes, solution[a])
            nb=id2node(nodes, solution[b])
        else:
            na=solution[a]
            nb=solution[b]
        objective += length(na, nb)
    return objective

#-----------------------------------------------------------------------------
if __name__ == '__main__':
    print("Done")

