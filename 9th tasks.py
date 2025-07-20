class MobilePhone:
    def __init__(self, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = "Touch Screen"
        self.network_type = "4G/5G"
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def receive_call(self, caller):
        print(f"Receiving call from {caller}...")

    def take_a_picture(self):
        print(f"Taking picture with {self.rear_camera} rear camera and {self.front_camera} front camera.")


class Apple(MobilePhone):
    def __init__(self, model, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(dual_sim, front_camera, rear_camera, ram, storage)
        self.brand = "Apple"
        self.model = model

    def phone_info(self):
        print(f"{self.brand} {self.model}")
        print(f"Dual SIM: {self.dual_sim}")
        print(f"Front Camera: {self.front_camera}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")
        print("-" * 30)


class Samsung(MobilePhone):
    def __init__(self, model, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(dual_sim, front_camera, rear_camera, ram, storage)
        self.brand = "Samsung"
        self.model = model

    def phone_info(self):
        print(f"{self.brand} {self.model}")
        print(f"Dual SIM: {self.dual_sim}")
        print(f"Front Camera: {self.front_camera}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")
        print("-" * 30)


iphone1 = Apple("iPhone 12", False, "12MP", "12MP", "4GB", "64GB")
iphone2 = Apple("iPhone SE", False, "7MP", "12MP", "3GB", "64GB")

samsung1 = Samsung("Galaxy S21", True, "10MP", "48MP", "4GB", "128GB")
samsung2 = Samsung("Galaxy M12", True, "8MP", "16MP", "3GB", "64GB")

iphone1.phone_info()
iphone1.make_call("9876543210")
iphone1.take_a_picture()

samsung1.phone_info()
samsung1.receive_call("Mom")
samsung1.take_a_picture()
