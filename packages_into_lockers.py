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

# CLASS FOR INDIVIDUAL LOCKERS!
class Locker:
    def __init__(self, size, locker_id):
        self.size = size
        self.locker_id = locker_id
        self.package = None

    def fits_package(self, package_size):
        return package_size <= self.size


# CLASS FOR ALL THE LOCKERS TOGETHER!
class LockerManager:
    def __init__(self):
        self.lockers = []

    # Function that adds locker by creating locker ID and size
    def add_locker(self, size):
        locker_id = len(self.lockers) + 1
        locker = Locker(size, locker_id)
        self.lockers.append(locker)

    # Locker is allocated (i.e. locker ID is given) for a package according to a locker that fits it
    def allocate_locker(self, package_size):
        for locker in self.lockers:
            if locker.fits_package(package_size) and locker.package is None:
                locker.package = package_size
                return locker.locker_id
        return None

    # Add package of size x to specified locker (ID)
    def add_package_to_locker(self, locker_id, package_size):
        for locker in self.lockers:
            if locker.locker_id == locker_id and locker.package is None:
                locker.package = package_size
                return True
        return False

    def remove_package_from_locker(self, locker_id):
        for locker in self.lockers:
            if locker.locker_id == locker_id and locker.package:
                removed_package = locker.package
                locker.package = None
                return removed_package
        return None

    # Show the size of the specified locker and any packages within it.
    def display_lockers(self):
        for locker in self.lockers:
            package_info = f"Package: {locker.package}" if locker.package else "No package"
            print(f"Locker {locker.locker_id} (Size: {locker.size}): {package_info}")


# Example usage
locker_manager = LockerManager()
locker_manager.add_locker('large')
locker_manager.add_locker('medium')
locker_manager.add_locker('small')
locker_manager.add_locker('large')
locker_manager.add_locker('medium')
locker_manager.add_locker('small')
locker_manager.add_locker('large')
locker_manager.add_locker('medium')
locker_manager.add_locker('medium')

# Allocate lockers for packages
package_sizes = ['small', 'medium', 'large', 'small', 'medium', 'large', 'small', 'small']
for package in package_sizes:
    locker_id = locker_manager.allocate_locker(package)
    if locker_id:
        locker_manager.add_package_to_locker(locker_id, package)

# Display the state of lockers
locker_manager.display_lockers()

# Remove a package from a specific locker
# removed_package = locker_manager.remove_package_from_locker(1)
# if removed_package:
#     print(f"Removed package from Locker 1: {removed_package}")
# else:
#     print("Locker 1 is empty or does not exist.")

# Display the updated state of lockers
# locker_manager.display_lockers()


# todo: problem is that packages of smaller sizes are not being allocated even to available larger lockers
# todo: create a way to check package size according to size depending on number rather than word (eg. 'large = 3')