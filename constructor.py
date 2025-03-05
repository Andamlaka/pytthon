class person:
    def __init__(self,name,age):

        self.name=name
        self.age=age
        print(f"person name is {self.name} and age is {self.age}")

    def __del__(self):
        print(f"person {self.name} is being destroyed.")
        

if __name__ == "__main__":
    p1=person("john",25)
    p2=person("jane",30)

    del p1
    del p2