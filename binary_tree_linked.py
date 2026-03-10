from binary_tree_abc import Position, BinaryTree


class BinaryTreeLinked(BinaryTree):
    ##############################################################################
    # Private helper classes and methods.
    ##############################################################################
    class _Node:
        def __init__(self, parent, element, left=None, right=None):
            self.parent: BinaryTreeLinked._Node = parent
            self.element: object = element
            self.left: BinaryTreeLinked._Node | None = left
            self.right: BinaryTreeLinked._Node | None = right

        def __str__(self) -> str:
            return f"ELEMENT: {self.element}"

    def _validate_pos(self, pos: Position):
        if pos is None or pos.handle is None:
            raise IndexError("Invalid position")

    def _representation(self, node: _Node | None) -> str:
        if node is None:
            return "-"
        left = self._representation(node.left)
        right = self._representation(node.right)
        return "(" + str(node.element) + " " + left + " " + right + ")"

    ##############################################################################
    # Public methods (implementing the BinaryTree Abstract Base Class interface).
    ##############################################################################

    def __init__(self):
        self._root: BinaryTreeLinked._Node | None = None

    def __str__(self):
        return self._representation(self._root)

    def clear(self):
        self._root = None

    def add_root(self, element: object) -> Position:
        node = self._Node(None, element, None, None)
        self._root = node
        return Position(node)

    def add_left_child(self, pos: Position, element: object) -> Position:
        self._validate_pos(pos)

        new: BinaryTreeLinked._Node = self._Node(pos.handle, element)
        pos.handle.left = new
        return Position(new)

    def add_right_child(self, pos: Position, element: object) -> Position:
        self._validate_pos(pos)

        new: BinaryTreeLinked._Node = self._Node(pos.handle, element)
        pos.handle.right = new
        return Position(new)

    def remove_subtree(self, pos: Position):

        l_child = self.left_child(pos)
        r_child = self.right_child(pos)

        if l_child is not None:
            self.remove_subtree(l_child)
        if r_child is not None:
            self.remove_subtree(r_child)

        self.remove(pos)

    def remove(self, pos: Position):
        self._validate_pos(pos)
        if not self.is_leaf(pos):
            raise IndexError("remove a non-leaf")

        curr: BinaryTreeLinked._Node = pos.handle

        par = curr.parent
        if par is None:
            return

        if par.left == curr:
            par.left = None
        elif par.right == curr:
            par.right = None

    def replace(self, pos: Position, element: object) -> object:
        curr: BinaryTreeLinked._Node = pos.handle

        r_obj = curr.element

        curr.element = element
        return r_obj

    def is_empty(self) -> bool:
        # To do
        ...

    def root(self) -> Position | None:
        return Position(self._root) if self._root is not None else None

    def parent(self, pos: Position) -> Position | None:
        self._validate_pos(pos)
        curr = pos.handle
        node = curr.parent
        return Position(node) if node is not None else None

    def left_child(self, pos: Position) -> Position | None:
        self._validate_pos(pos)
        curr: BinaryTreeLinked._Node = pos.handle
        node = curr.left
        return Position(node) if node is not None else None

    def right_child(self, pos: Position) -> Position | None:
        self._validate_pos(pos)
        curr: BinaryTreeLinked._Node = pos.handle
        node = curr.right
        return Position(node) if node is not None else None

    def is_root(self, pos: Position) -> bool:
        self._validate_pos(pos)
        curr: BinaryTreeLinked._Node = pos.handle
        return curr.parent is None

    def is_leaf(self, pos: Position) -> bool:
        self._validate_pos(pos)
        curr: BinaryTreeLinked._Node = pos.handle
        return curr.left is None and curr.right is None

    def get_at(self, pos: Position) -> object:
        self._validate_pos(pos)
        curr: BinaryTreeLinked._Node = pos.handle
        return curr.element


def call():

    BTL = BinaryTreeLinked()
    pos = BTL.add_root(5)

    print(BTL)

    if pos is None:
        return

    r_pos = BTL.add_right_child(pos, 4)
    print(BTL)
    rr_pos = BTL.add_right_child(r_pos, 3)
    print(BTL)
    rrr_pos = BTL.add_right_child(rr_pos, 2)
    print(BTL)

    if rrr_pos is None:
        return

    BTL.replace(rr_pos, 99)
    print(BTL)


call()
