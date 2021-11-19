class Students:
    waiver = 0.8 # to pay after applying waiver

    def __init__(self,name: str, cgpa: float, semester: int, tutuin_fee: float):
        # Run validations
        assert cgpa >= 0, f"cgpa {cgpa} should be grater on equal to zero"
        assert semester >= 0, f"semester {semester} should be grater on equal to zero"

        # Assigned to self object
        self.name = name
        self.cgpa = cgpa
        self.sem = semester
        self.tution_fee = tutuin_fee

    # def apply_waiver(self):
    #     self.tution_fee = self.tution_fee * self.waiver

    def show_details(self):
        self.tution_fee = self.tution_fee * self.waiver
        print(f"{self.name} got {self.cgpa} cgpa in {self.sem} semester pays about {self.tution_fee} tk")


shahin = Students("meherullah shahin", 3.73, 11, 50000)
if shahin.cgpa == 4 :
    shahin.waiver = .5
# shahin.apply_waiver()
shahin.show_details()
