from binary_search_tree import Pair, BinarySearchTree

def test0():
    tree = BinarySearchTree()
    print(tree.is_empty())
    tree.insert_key(20)
    tree.insert(Pair(30,"SHIT"))
    tree.insert_key(40)
    tree.insert_key(10)
    print(tree)
    print(tree.is_in(10))
    print(tree.is_in(50))

    print(tree.is_empty())
    print(tree.get(30))
    print(tree.get(5))
    """
    # For testing _before/_after_/_first/_last
    for pair in tree:
        print(pair.key, end=' ')
    print()
    for pair in reversed(tree):
        print(pair.key, end=' ')
    print()
    """

test0()




