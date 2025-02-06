# ---------------------------------------------
# Smart Home Management System
# ---------------------------------------------
# This system manages:
# 1. Devices with power status and consumption tracking.
# 2. Rooms with assigned devices.
# 3. Users with Admin and Guest roles.
# 4. Energy-efficient devices with ratings and statuses.
# ---------------------------------------------

# ---------------------------------------------
# Device Class
# ---------------------------------------------

class Device:    
    """
    Represents a basic device with power status and consumption tracking.
    """

    def __init__(self, device_name, status, power_consumption):
        self.device_name = device_name
        self.status = status
        self.power_consumption = power_consumption

    def turn_on(self): 
        self.status = "on"
        return f"{self.device_name} has been powered on!"
    
    def turn_off(self): 
        self.status = "off"
        return f"{self.device_name} has been turned off!"
    
    @staticmethod 
    def is_power_safe(power_consumption):
        """
        Checks if the device is consuming too much power.
        """
        return "Your device is consuming too much power!" if power_consumption > 2000 else "Your device's power consumption is safe."

# ---------------------------------------------
# User Class
# ---------------------------------------------

class User:
    """
    Represents a user in the system with an assigned role.
    """

    user_count = 0  # Track the number of users

    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.users = []
        User.user_count += 1

    def display_info(self): 
        """
        Displays user details.
        """
        return f"Name: {self.name} | Role: {self.role}"
    
    def add_user(self, user): 
        """
        Adds a new user to the system.
        """
        self.users.append(user)

# ---------------------------------------------
# Room Class
# ---------------------------------------------

class Room:
    """
    Represents a room with assigned devices.
    """

    total_rooms = 0
    total_devices = 0

    def __init__(self, room_name):
        self.room_name = room_name
        self.devices = []
        Room.total_rooms += 1

    def add_device(self, device): 
        """
        Adds a device to the room.
        """
        self.devices.append(device)
        Room.total_devices += 1

    def remove_device(self, device): 
        """
        Removes a device from the room.
        """
        if device in self.devices:
            self.devices.remove(device)
            Room.total_devices -= 1
    
    @classmethod
    def get_total_rooms(cls): 
        """
        Retrieves the total number of rooms.
        """
        return f"You have {cls.total_rooms} rooms added!"
    
    @classmethod
    def accommodate_rooms(cls): 
        """
        Checks if more rooms can be added.
        """
        return "There is no more space for rooms!" if cls.total_rooms >= 10 else "You can add more rooms!"

# ---------------------------------------------
# Energy Efficient Device Class
# ---------------------------------------------

class EnergyEfficientDevice(Device):
    """
    Represents an energy-efficient device with a rating.
    """

    def __init__(self, device_name, status, power_consumption, energy_efficiency_rating):
        super().__init__(device_name, status, power_consumption)
        self.energy_efficiency_rating = energy_efficiency_rating

    def get_status(self): 
        """
        Retrieves device status and energy efficiency rating.
        """
        return f"Device: {self.device_name} | Status: {self.status} | Energy Efficiency: {self.energy_efficiency_rating}"

    def display_efficiency(self): 
        """
        Displays energy efficiency rating and recommendations.
        """
        if self.energy_efficiency_rating == 100:
            return f"{self.device_name} is running perfectly!"
        elif 80 <= self.energy_efficiency_rating < 90:
            return f"{self.device_name} is running optimally!"
        elif 70 <= self.energy_efficiency_rating < 80:
            return f"{self.device_name} is running well!"
        elif 60 <= self.energy_efficiency_rating < 70:
            return f"{self.device_name} needs servicing soon!"
        else:
            return f"{self.device_name} needs immediate servicing!"

# ---------------------------------------------
# Smart Light Class
# ---------------------------------------------

class SmartLight(EnergyEfficientDevice):
    """
    Represents a Smart Light with brightness adjustment.
    """

    def __init__(self, device_name, status, power_consumption, energy_efficiency_rating, brightness_level):
        super().__init__(device_name, status, power_consumption, energy_efficiency_rating)
        self.brightness_level = brightness_level

    def adjust_brightness(self, level): 
        """
        Adjusts the brightness of the smart light.
        """
        self.brightness_level = level
        return f"Brightness level set to {self.brightness_level}."

# ---------------------------------------------
# Smart Thermostat Class
# ---------------------------------------------

class SmartThermo(EnergyEfficientDevice):
    """
    Represents a Smart Thermostat with temperature control.
    """

    def __init__(self, device_name, status, power_consumption, energy_efficiency_rating, current_temperature, target_temperature):
        super().__init__(device_name, status, power_consumption, energy_efficiency_rating)
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature

    def set_temperature(self, new_temp):  
        """
        Adjusts the thermostat's temperature.
        """
        self.target_temperature = new_temp
        return f"Temperature set from {self.current_temperature}°F to {self.target_temperature}°F."

# ---------------------------------------------
# Admin Class
# ---------------------------------------------

class Admin(User, Room):
    """
    Represents an Admin user with room control capabilities.
    """

    def __init__(self, name, role, room_name):
        User.__init__(self, name, role)
        Room.__init__(self, room_name)

    def display_devices(self): 
        """
        Displays the list of devices in the room.
        """
        return f"Devices in {self.room_name}: {', '.join([device.device_name for device in self.devices])}"

# ---------------------------------------------
# Guest Class
# ---------------------------------------------

class Guest(User):
    """
    Represents a Guest user.
    """

    def __init__(self, name, role):
        super().__init__(name, role)

# ---------------------------------------------
# Example Usage
# ---------------------------------------------

# Create a room
room = Room("Living Room")

# Create users
admin1 = Admin("Nazir", "Admin", "Living Room")
guest1 = Guest("Arden", "Guest")

# Add users
user_system = User("System", "Manager")
user_system.add_user(admin1)
user_system.add_user(guest1)

print(f"There are {User.user_count} users currently assigned.")

# Create devices
kitchen_light = SmartLight("Kitchen Lights", "on", 90, 90, 100)
house_thermo = SmartThermo("Thermostat", "on", 3000, 100, 75, 61)

device1 = EnergyEfficientDevice("Desktop", "on", 1500, 100)
device2 = EnergyEfficientDevice("TV", "off", 3000, 69)

# Add devices to room
room.add_device(device1)
room.add_device(device2)

# Display device information
print(kitchen_light.turn_off())
print(kitchen_light.get_status())
print(kitchen_light.turn_on())
print(kitchen_light.adjust_brightness(80))

print(house_thermo.get_status())
print(house_thermo.display_efficiency())
print(house_thermo.set_temperature(68))

print(Room.accommodate_rooms())
print(Admin.get_total_rooms())
print(room.device_amount())

print(admin1.display_info())
print(device1.turn_on())
print(device2.turn_off())
print(Device.is_power_safe(device1.power_consumption))
print(device1.display_efficiency())

print(guest1.display_info())
