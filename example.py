from KDicTree import KDicTree

tree = KDicTree({"Hans": (0,0,0),
                 "Juergen": (5, 5, 0),
                 "Dietram": (3.1415, -.1, 2),
                 "The Joke": (100, 100, 100)})

distances, neighbours = tree.query( [(0,0,0), (80,80,1)], k=2)

print("* Distances (type: {}):\n{}\n".format(type(distances),
                                           distances))
print("* Neighbours (type: {}):\n{}\n".format(type(neighbours),
                                            neighbours))

ball_matches = tree.query_ball_point( (20, 20, 10), 50)

print("* Ball point matches (type: {}):\n{}\n".format(type(ball_matches),
                                                    ball_matches))


pairs_matches = tree.query_pairs(20)

print("* Pairs (type: {}):\n{}\n".format(type(pairs_matches),
                                       pairs_matches))

print("Ball point querys with updating positions:")
for x in range(-25, 25, 5):
    y, z = x, x
    tree["The Joke"] = (x, y, z)
    tree["Juergen"] = (tree["Juergen"][0]+abs(x*.045),
                       tree["Juergen"][1], tree["Juergen"][2])
    tree["Hans"] = (0,0,100) if x % 10 == 0 else (0,0,0)

    print("x = {} : \t{}".format(x, tree.query_ball_point( (0,0,0), 10.5)))
