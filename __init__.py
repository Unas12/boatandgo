from ._anvil_designer import StaffDashboardTemplate
from anvil import *

# Sample orders — simpler view for staff (no revenue)
STAFF_ORDERS = [
    {"order_id": "#B-041", "name": "Somchai",  "item": "Classic Boat Noodle", "spice": "Extra Spicy 🌶🌶🌶", "pickup": "11:30 AM", "status": "✅ Ready"},
    {"order_id": "#B-042", "name": "Nattaya",  "item": "Beef Boat Noodle",    "spice": "Medium 🌶🌶",       "pickup": "12:00 PM", "status": "👨‍🍳 Preparing"},
    {"order_id": "#B-043", "name": "Piyawat",  "item": "Chicken Tom Yum",     "spice": "Mild 🌶",           "pickup": "12:00 PM", "status": "👨‍🍳 Preparing"},
    {"order_id": "#B-044", "name": "Sirima",   "item": "Vegetarian Broth",    "spice": "No Spice 🙂",       "pickup": "12:30 PM", "status": "📋 Received"},
    {"order_id": "#B-045", "name": "Tanakorn", "item": "Classic Boat Noodle", "spice": "Extra Spicy 🌶🌶🌶", "pickup": "12:30 PM", "status": "📋 Received"},
]

class StaffDashboard(StaffDashboardTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.data_grid_orders.items = STAFF_ORDERS

    def btn_back_click(self, **event_args):
        open_form('HomeScreen')
