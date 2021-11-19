class Students:
    def __init__(self,name: str, cgpa: float, semester: int):
        # Run validations
        assert cgpa >= 0, f"cgpa {cgpa} should be grater on equal to zero"
        assert semester >= 0, f"semester {semester} should be grater on equal to zero"

        #Assigned to self object
        self.name = name
        self.cgpa = cgpa
        self.sem = semester


    def show_details(self):
        print(f"{self.name} got {self.cgpa} cgpa in {self.sem} semester")


shahin = Students("meherullah shahin", 3.71, 10)
shahin.show_details()
