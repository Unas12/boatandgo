from ._anvil_designer import HomeScreenTemplate
from anvil import *

class HomeScreen(HomeScreenTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def btn_customer_click(self, **event_args):
        open_form('CustomerMenu')

    def btn_staff_click(self, **event_args):
        open_form('StaffDashboard')

    def btn_owner_click(self, **event_args):
        open_form('OwnerLogin')
