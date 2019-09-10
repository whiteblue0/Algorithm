def preorder(node):
    if node != 0:
        print("{}".format(node),end=" ")
        preorder(tree[node][0])
        preorder(tree[node][1])

def interorder(node):
    if node != 0:
        interorder(tree[node][0])
        print("{}".format(node), end=" ")
        interorder(tree[node][1])

def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print("{}".format(node), end=" ")

V,E = 13, 12
data = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

tree = [[0]*3 for _ in range(V+1)]

for i in range(E):
    n1 = data[i*2]
    n2 = data[i*2 + 1]
    if not tree[n1][0]:
        tree[n1][0] = n2
    else:
        tree[n1][1] = n2
    tree[n2][2] = n1

for i in range(V):
    print(i,tree[i])


preorder(1)
print()
interorder(1)
print()
postorder(1)
