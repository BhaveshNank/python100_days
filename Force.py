def calculate_force(mass, acceleration):

    force = mass * acceleration
    return force

# Example usage:
mass = int(input("Enter the value of mass ")) # in kilograms
acceleration = int(input("Enter the value of acceleration "))  # in meters per second squared

force = calculate_force(mass, acceleration)
print("The force is:", force, "newtons")
