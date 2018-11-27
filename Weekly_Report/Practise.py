# # Strategy Pattern
# class FlyingBehaviour(object):
#     def take_off(self):
#         print("I'm running fast, flapping with my wings.")
#
#     def fly_to(self, destination):
#         print("Now flying to [%s]" %destination)
#
#     def land(self):
#         print("Slowing down, extending legs, touch down.")
#
#
# class NonFlyingBehaviour(FlyingBehaviour):
#     def take_off(self):
#         print("It's not working. :-(")
#
#     def fly_to(self, destination):
#         raise Exception("I am not flying anywhere.")
#
#     def land(self):
#         print("That won't necessary.")
#
#
# class Duck(object):
#     def __init__(self):
#         print("Initialization.....")
#         self.flying_behaviour = FlyingBehaviour()
#
#     def quack(self):
#         print("Quack!")
#
#     def display(self):
#         print("Boaring looking duck.")
#
#     def take_off(self):
#         self.flying_behaviour.take_off()
#
#     def fly_to(self, destination):
#         self.flying_behaviour.fly_to(destination)
#
#     def land(self):
#         self.flying_behaviour.land()
#
#
# class RedHeadDuck(Duck):
#     def display(self):
#         print("Duck with Red Head.")
#
#
# class RubberDuck(Duck):
#     def __init__(self):
#         self.flying_behaviour = NonFlyingBehaviour()  # this is overrind super class "Duck" init
#
#     def quack(self):
#         print("Squeak!!")
#
#     def display(self):
#         print("small yellow rubber duck")
#
# class DecoyDuck(Duck):
#     def __init__(self):
#         self.flying_behaviour = NonFlyingBehaviour()
# if __name__ =="__main__":
#
#     a = RedHeadDuck()
#     a.display()
#     a.take_off()
#
#     b = RubberDuck()
#     b.quack()
#     b.display()
#     b.take_off()
#     b.land()
#
#     c = DecoyDuck()
#     c.quack()
#     c.take_off()

#========================== Decorator Pattern


class Beverages(object):
    def __init__(self, withMilk, withSugar):
        self.withMilk = withMilk
        self.withSugar  = withSugar

    def get_description(self):
        description = str(self._get_default_description())
        if self.withMilk:
            description += ", with Milk."
        if self.withSugar:
            description += ", with Sugar."
        return description

    def _get_default_description(self):
        return 'Beverages'

    def get_cost(self):
        return 0.00


class Coffee(Beverages):
    def _get_default_description(self):
        return "Normal Coffee"

    def get_cost(self):
        return 3.00


class Tea(Beverages):
    def get_description(self):
        return "tee"

    def get_cost(self):
        return 2.50


class Coffeewithmilk(Coffee):
    def get_description(self):
        return super(Coffeewithmilk, self).get_description() + ", with milk"

    def get_cost(self):
        return super(Coffeewithmilk, self).get_cost() + 0.30


if __name__ == "__main__":

    C = Coffeewithmilk(withMilk=True, withSugar=False)
    print(C.get_description())
    print(C.get_cost())
