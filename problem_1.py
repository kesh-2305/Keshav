class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"2D Vector: {self.x}i + {self.y}j")


class Vector3D(Vector2D):   # ✅ Class bahar nikali + naam correct kiya
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"3D Vector: {self.x}i + {self.y}j + {self.z}k")


v2 = Vector2D(3, 4)
v2.show()

v3 = Vector3D(1, 2, 3)   # ✅ Name match ho gaya
v3.show()