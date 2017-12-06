from scipy.spatial import cKDTree as KDTree
from numpy import ndarray

class KDicTree(dict):
    '''
    Wrapper around the scipy.spatial.KDTree for labelled points.
    Use like dict to register or update points:
    
    tree = KDicTree({'1':(0,0), 2:(2,2), '3':(45,45)})
    tree['1'] = (1, 1)
    tree['2'] = (5, 5)
    tree['3'] = (50, 50)
    
    Then use KDTree querys:
    
    tree.query_ball_point( (3, 3), 10 )
        ['1', 2, '2']

    Parameters
    ----------
    data : labelled (N,K) dict
        The data points to be indexed, labelled in a dictionary.
    leafsize : int, optional
        The number of points at which the algorithm switches over to 
        brute-force. Has to be positive.
    
    See Also
    --------
    scipy.spatial.KDTree
    scipy.spatial.cKDTree
    '''
    
    def __init__(self, data, leafsize=16):   
        self.tree = None
        self.ids = [] # maps tree to dict keys
        self.altered = True
        self.leafsize = leafsize
        super().__init__(data)
    
    def __setitem__(self, key, point):
        '''Set point for self[key]'''
        super().__setitem__(key, point)
        self.altered = True
    
    def __delitem__(self, key):
        '''Delete self[key].'''
        super().__delitem__(key)
        self.altered = True
    
    def build_tree(self):
        '''Gets called automatically by a query.'''
        if not self.altered: return
        self.tree = KDTree(list(self.values()), leafsize=self.leafsize)
        self.ids = list(self.keys())
        self.altered = False

    def map_ids(self, ids):
        '''Maps the result of Querys to dict keys.'''
        if isinstance(ids, (tuple, list, ndarray)):
            return tuple(map(self.map_ids, ids))
        return self.ids[ids]
    
    def query(self, x, k=1, eps=0, p=2, distance_upper_bound=float("inf")):
        '''Query the kd-tree for nearest neighbors.'''
        self.build_tree()
        dists, ids = self.tree.query(x, k, eps, p, distance_upper_bound)
        return (dists, self.map_ids(ids))
    
    def query_ball_point(self, x, r, p=2., eps=0):
        '''Find all points within distance r of point(s) x.'''
        self.build_tree()
        return self.map_ids(self.tree.query_ball_point(x, r, p, eps))
    
    def query_pairs(self, r, p=2., eps=0):
        '''Find all pairs of points within a distance r.'''
        self.build_tree()
        return [tuple(self.map_ids(pair))
                for pair in self.tree.query_pairs(r, p=p, eps=eps)]

