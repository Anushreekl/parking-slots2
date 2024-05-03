class ParkingSlot:
    def __init__(self, slot_number, is_available=True):
        self.slot_number = slot_number
        self.is_available = is_available
        self.vehicle = None

class ParkingLot:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.slots = [ParkingSlot(slot_number) for slot_number in range(1, total_slots + 1)]

    def park_vehicle(self, vehicle_number):
        for slot in self.slots:
            if slot.is_available:
                slot.is_available = False
                slot.vehicle = vehicle_number
                return slot.slot_number
        return -1  # If parking lot is full

    def remove_vehicle(self, slot_number):
        if 1 <= slot_number <= self.total_slots:
            slot = self.slots[slot_number - 1]
            if not slot.is_available:
                slot.is_available = True
                slot.vehicle = None
                return True
        return False  # If slot number is invalid or already empty

    def available_slots(self):
        return [slot.slot_number for slot in self.slots if slot.is_available]

    def occupied_slots(self):
        return [(slot.slot_number, slot.vehicle) for slot in self.slots if not slot.is_available]


# Example Usage
if __name__ == "__main__":
    total_slots = 20  # Total number of parking slots
    parking_lot = ParkingLot(total_slots)

    # Park vehicles
    print("Parking vehicle with number ABC123:", parking_lot.park_vehicle("ABC123"))
    print("Parking vehicle with number XYZ789:", parking_lot.park_vehicle("XYZ789"))
    print("Parking vehicle with number DEF456:", parking_lot.park_vehicle("DEF456"))

    # Display available and occupied slots
    print("Available slots:", parking_lot.available_slots())
    print("Occupied slots:", parking_lot.occupied_slots())

    # Remove vehicle from slot 2
    print("Removing vehicle from slot 2:", parking_lot.remove_vehicle(2))

    # Display available and occupied slots after removal
    print("Available slots:", parking_lot.available_slots())
    print("Occupied slots:", parking_lot.occupied_slots())
