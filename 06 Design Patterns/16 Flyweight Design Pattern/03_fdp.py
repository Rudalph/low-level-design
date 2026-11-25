# Flyweight class: All Intrinsic Properties
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x, y):
        print(
            f"Drawing {self.name} tree "
            f"at ({x}, {y})"
        )


# Flyweight Factory: Creating objects of Intrinsic Properties and saving in MAP
class TreeFactory:
    def __init__(self):
        self.tree_types = {}

    def get_tree_type(self, name, color, texture):

        key = (name, color, texture)

        if key not in self.tree_types:
            self.tree_types[key] = TreeType(
                name, color, texture
            )

        return self.tree_types[key]


# Context class: All Extrinsic Properties
class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        self.tree_type.draw(self.x, self.y)


# Client code
factory = TreeFactory()

oak1 = Tree(
    10, 20,
    factory.get_tree_type("Oak", "Green", "OakTexture")
)

oak2 = Tree(
    30, 40,
    factory.get_tree_type("Oak", "Green", "OakTexture")
)

oak3 = Tree(
    50, 60,
    factory.get_tree_type("Oak", "Green", "OakTexture")
)

oak1.draw()
oak2.draw()
oak3.draw()

print(oak1.tree_type is oak2.tree_type)