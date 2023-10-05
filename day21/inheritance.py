class Animal:
    def __init__(self) -> int:
        self.num_of_eye = 2

    def breathing(self) -> str:
        print( "inhile and exhale")
    



class Fish(Animal):
    def __init__(self) -> int:
        super().__init__()

    def swim(self) -> str:
        print("moving in water")
    


bayaad = Fish()

bayaad.swim()
bayaad.breathing()
