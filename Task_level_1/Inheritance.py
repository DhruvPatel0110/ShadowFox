# Creating base class MobilePhone
class MobilePhone:

    def __init__(self, screen_type, network_type, dual_sim,
                 front_camera, rear_camera, ram, storage):

        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self):
        print("Making a phone call")

    def receive_call(self):
        print("Receiving a phone call")

    def take_picture(self):
        print("Taking a picture")

# Creating Apple class using inheritance
class Apple(MobilePhone):

    def __init__(self, screen_type, network_type, dual_sim,
                 front_camera, rear_camera, ram, storage,
                 model, ios_version):

        super().__init__(screen_type, network_type, dual_sim,
                         front_camera, rear_camera, ram, storage)

        self.model = model
        self.ios_version = ios_version

    def display_info(self):
        print(f"Apple Model : {self.model}")
        print(f"iOS Version : {self.ios_version}") #unique property
        print(f"Screen Type : {self.screen_type}")
        print(f"Network Type : {self.network_type}")
        print(f"Dual Sim : {self.dual_sim}")
        print(f"Front Camera : {self.front_camera}")
        print(f"Rear Camera : {self.rear_camera}")
        print(f"RAM : {self.ram}")
        print(f"Storage : {self.storage}")

# Creating Samsung class using inheritance
class Samsung(MobilePhone):

    def __init__(self, screen_type, network_type, dual_sim,
                 front_camera, rear_camera, ram, storage,
                 model, android_version):

        super().__init__(screen_type, network_type, dual_sim,
                         front_camera, rear_camera, ram, storage)

        self.model = model
        self.android_version = android_version

    def display_info(self):
        print(f"Samsung Model : {self.model}")
        print(f"Android Version : {self.android_version}") #unique property
        print(f"Screen Type : {self.screen_type}")
        print(f"Network Type : {self.network_type}")
        print(f"Dual Sim : {self.dual_sim}")
        print(f"Front Camera : {self.front_camera}")
        print(f"Rear Camera : {self.rear_camera}")
        print(f"RAM : {self.ram}")
        print(f"Storage : {self.storage}")

# Creating Apple objects with different properties
iphone1 = Apple(
    "Touch Screen", "5G", True,
    "12MP", "48MP", "8GB", "256GB",
    "iPhone 15 Pro", "iOS 18"
)

iphone2 = Apple(
    "Touch Screen", "4G", False,
    "8MP", "16MP", "4GB", "64GB",
    "iPhone 11", "iOS 16"
)

# Creating Samsung objects with different properties
samsung1 = Samsung(
    "Touch Screen", "5G", True,
    "16MP", "108MP", "12GB", "512GB",
    "Samsung S24 Ultra", "Android 15"
)

samsung2 = Samsung(
    "Touch Screen", "4G", True,
    "8MP", "32MP", "6GB", "128GB",
    "Samsung A54", "Android 13"
)


# Displaying Apple object details
iphone1.display_info()
iphone1.make_call()
iphone1.take_picture()

# Output :
# Apple Model : iPhone 15 Pro
# iOS Version : iOS 18
# Screen Type : Touch Screen
# Network Type : 5G
# Dual Sim : True
# Front Camera : 12MP
# Rear Camera : 48MP
# RAM : 8GB
# Storage : 256GB
# Making a phone call
# Taking a picture

print()

iphone2.display_info()
iphone2.receive_call()

# Output :
# Apple Model : iPhone 11
# iOS Version : iOS 16
# Screen Type : Touch Screen
# Network Type : 4G
# Dual Sim : False
# Front Camera : 8MP
# Rear Camera : 16MP
# RAM : 4GB
# Storage : 64GB
# Receiving a phone call

print()

# Displaying Samsung object details
samsung1.display_info()
samsung1.take_picture()

# Output :
# Samsung Model : Samsung S24 Ultra
# Android Version : Android 15
# Screen Type : Touch Screen
# Network Type : 5G
# Dual Sim : True
# Front Camera : 16MP
# Rear Camera : 108MP
# RAM : 12GB
# Storage : 512GB
# Taking a picture

print()

samsung2.display_info()
samsung2.make_call()

# Output :
# Samsung Model : Samsung A54
# Android Version : Android 13
# Screen Type : Touch Screen
# Network Type : 4G
# Dual Sim : True
# Front Camera : 8MP
# Rear Camera : 32MP
# RAM : 6GB
# Storage : 128GB
# Making a phone call