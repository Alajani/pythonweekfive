# Base Class
class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_capacity = battery_capacity
    
    def display_specs(self):
        return f"{self.brand} {self.model}: {self.storage}GB Storage, {self.battery_capacity}mAh Battery"

# Derived Class for Advanced Features
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, battery_capacity, camera_quality, has_5g):
        super().__init__(brand, model, storage, battery_capacity)
        self.camera_quality = camera_quality
        self.has_5g = has_5g

    # Overriding the method to include more details
    def display_specs(self):
        base_specs = super().display_specs()
        additional_features = f"Camera: {self.camera_quality}MP, 5G Support: {'Yes' if self.has_5g else 'No'}"
        return f"{base_specs}, {additional_features}"

# Creating objects
basic_phone = Smartphone("Samsung", "Galaxy A13", 64, 5000)
pro_phone = SmartphonePro("Apple", "iPhone 15 Pro", 256, 4500, 48, True)

# Using methods
print(basic_phone.display_specs())  # Samsung Galaxy A13: 64GB Storage, 5000mAh Battery
print(pro_phone.display_specs())    # Apple iPhone 15 Pro: 256GB Storage, 4500mAh Battery, Camera: 48MP, 5G Support: Yes
# Base Class
class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_capacity = battery_capacity
    
    def display_specs(self):
        return f"{self.brand} {self.model}: {self.storage}GB Storage, {self.battery_capacity}mAh Battery"

# Derived Class for Advanced Features
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, battery_capacity, camera_quality, has_5g):
        super().__init__(brand, model, storage, battery_capacity)
        self.camera_quality = camera_quality
        self.has_5g = has_5g

    # Overriding the method to include more details
    def display_specs(self):
        base_specs = super().display_specs()
        additional_features = f"Camera: {self.camera_quality}MP, 5G Support: {'Yes' if self.has_5g else 'No'}"
        return f"{base_specs}, {additional_features}"

# Creating objects
basic_phone = Smartphone("Samsung", "Galaxy A13", 64, 5000)
pro_phone = SmartphonePro("Apple", "iPhone 15 Pro", 256, 4500, 48, True)

# Using methods
print(basic_phone.display_specs())  # Samsung Galaxy A13: 64GB Storage, 5000mAh Battery
print(pro_phone.display_specs())    # Apple iPhone 15 Pro: 256GB Storage, 4500mAh Battery, Camera: 48MP, 5G Support: Yes
