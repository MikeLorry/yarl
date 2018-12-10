import names

class Hero:
    """Common class for Heroes"""
    empCount = 0

    def __init__(self):
        self.name = names.get_first_name()
        self.avatar = "robot.png"
        self.max_life = 10
        self.life = self.max_life
        print(self.name + " just entered")
        print("All systems operational")

    def defend(self,force,type="hit"):
        print("Attacked by " + str(force) + " " + type)
        return

    def heal(self,points):
        if self.life + points >= self.max_max_life:
            self.life = self.max_life
            print("Back to full health")
        else:
            self.life += points
            print("Healed " + str(points) + " life points")
        return