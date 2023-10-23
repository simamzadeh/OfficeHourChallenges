# Challenge: Packages into Lockers!
# Difficulty: Intermediate
#
# Amazon is developing a new locker system for Amazon deliveries to ensure customer packages are delivered
# in a secure location.
# In order to assist delivery drivers, Amazon will develop software to be installed that will instruct which locker
# the driver should place the package in depending on its size.
#
# For the purposes of this question, design and implement the component of this system that will
# take a package's size and return the locker number the package should be stored in so that the customer
# can be notified where their package is located.
# This solution should be able to simulate adding a package to the locker and removing a package given a locker number.

import random


class Locker:
    sizes = {'small': 1, 'medium': 2, 'large': 3}

    def __init__(self, locker_id, size):
        self.locker_id = locker_id
        self.size = size
        self.package_inside = False

    def fits_package(self, package_size):
        return self.sizes[package_size] <= self.sizes[self.size]

    def __str__(self):
        return f"Locker {self.locker_id} - Size: {self.size}, Has Package: {self.package_inside}"


class LockerManager:
    locker_sizes = ['small', 'medium', 'large']
    lockers = []

    @staticmethod
    def allocate_locker_for_package(lockers):
        package_size = input("Enter package size (small, medium, or large): ").lower()
        if package_size not in LockerManager.locker_sizes:
            print("Invalid package size.")
            return None

        for locker in lockers:
            if locker.fits_package(package_size) and not locker.package_inside:
                locker.package_inside = True
                print(f"Package placed in locker {locker.locker_id, locker.size}.")
                return locker.locker_id

        print("No available locker for the package size.")
        return None

    @staticmethod
    def remove_package_from_locker(locker_id):
        for locker in LockerManager.lockers:
            if locker.locker_id == locker_id:
                if locker.package_inside:
                    locker.package_inside = False
                    print(f"Package removed from locker {locker.locker_id}.")
                else:
                    print(f"No package found in locker {locker.locker_id}.")
                return

        print(f"Locker {locker_id} not found.")


def generate_random_lockers(max_lockers=100000):
    num_lockers = random.randint(1, max_lockers)

    lockers = []

    for i in range(num_lockers):
        random_size = random.randint(0, len(LockerManager.locker_sizes) - 1)
        size = LockerManager.locker_sizes[random_size]
        locker = Locker(i + 1, size)
        lockers.append(locker)

    return lockers


locker_manager = LockerManager()
random_lockers = generate_random_lockers()
LockerManager.lockers = random_lockers

for locker in random_lockers:
    print(locker)

# Delivery Driver: "Which locker should I place the package in?"
allocated_locker_id = LockerManager.allocate_locker_for_package(random_lockers)

# Customer: "I want to remove a package from locker number x"
locker_to_remove_package = int(input("Enter the locker number to remove the package from: "))
LockerManager.remove_package_from_locker(locker_to_remove_package)
