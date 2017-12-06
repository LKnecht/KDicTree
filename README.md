Wrapper around the scipy.spatial.KDTree for labelled points.

## Usage

Use like dict to register or update points:

```
tree = KDicTree({'1':(0,0), 2:(2,2), '3':(45,45)})
tree['1'] = (1, 1)
tree['2'] = (5, 5)
tree['3'] = (50, 50)
```

Then use KDTree querys:

```
tree.query_ball_point( (3, 3), 10 )
<map object at ...>
list(<map object at ...>)
['1', 2, '2']
```

## Parameters

data : labelled (N,K) dict
The data points to be indexed, labelled in a dictionary.
leafsize : int, optional
The number of points at which the algorithm switches over to 
brute-force. Has to be positive.

## See Also

scipy.spatial.KDTree
scipy.spatial.cKDTree