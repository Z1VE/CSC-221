from classes import Vehicle,ElectricCar

def main():
    print("\nCreating three cars...")

    car1 = Vehicle("Ford","Mustang",155)
    car2 = ElectricCar("Tesla","Model 3", 140, 75)
    car3 = ElectricCar("Rimac", "Nevera", 258, 120)

# testing data types

    print(f"is car 1 a vehicle? {isinstance(car1, Vehicle)}")
    print(f"is car 1 a vehicle? {isinstance(car1, ElectricCar)}")

    print(f"is car 2 a vehicle? {isinstance(car2, Vehicle)}")
    print(f"is car 2 a vehicle? {isinstance(car2, ElectricCar)}")

# testing __lt__

    print(f"Checking to see if car2 is slower than car1: {car2 < car1}")

    print(car3)
    # using __lt__ to sort a list of cars

    fleet = [car1,car2,car3]
    sorted_fleet = sorted(fleet)


    print("\nVehicles sorted by top speed")
    for car in sorted_fleet:
        print(f"- {car}: Top speed is {car.top_speed}")


if __name__ == '__main__':
    main()