import unittest
from paint_calculator import api
from paint_calculator.run import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_calculate(self):
        """
        Tests calculate function
        """
        room1 = {'length':20,'width':20,'height':20}
        room2 = {'length':10,'width':10,'height':10}
        response = self.app.post(
            '/api/v1/calculate',
            json={
                'room-1':room1,
                'room-2':room2
                }
            )
        ft_room1 = {}
        ft_room1['ft'] = api.calculate_feet(room1)
        gallons_room1 = api.calculate_gallons_required(ft_room1)
        self.assertEqual(response.json['room-1']['ft'], ft_room1['ft'], "total ft for room-1 should be calculated from calculate_feet function")
        self.assertEqual(response.json['room-1']['gallons'], gallons_room1, "total gallons for room-1 should be calculated from calculate_gallons_required function")
        self.assertEqual(response.json['room-1']['room'], '1', "room number should be 1")

        ft_room2 = {}
        ft_room2['ft'] = api.calculate_feet(room2)
        gallons_room2 = api.calculate_gallons_required(ft_room2)
        self.assertEqual(response.json['room-2']['ft'], ft_room2['ft'], "total ft for room-2 should be calculated from calculate_feet function")
        self.assertEqual(response.json['room-2']['gallons'], gallons_room2, "total gallons for room-2 should be calculated from calculate_gallons_required function")
        self.assertEqual(response.json['room-2']['room'], '2', "room number should be 2")

        total_gallons = gallons_room1 + gallons_room2
        self.assertEqual(response.json['total_gallons'], total_gallons, "total gallons for all rooms should be calculated by calculate function")

    def test_calculate_feet(self):
        """
        Tests calculate_feet function
        """
        room1 = {'length':20,'width':20,'height':20}
        room2 = {'length':10,'width':10,'height':10}
        self.assertEqual(api.calculate_feet(room1), 1600, "total ft for room-1 (20-20-20) should be 1600")
        self.assertEqual(api.calculate_feet(room2), 400, "total ft for room-2 (10-10-10) should be 400")

    def test_calculate_gallons_required(self):
        """
        Tests calculate_gallons_required function
        """
        room1 = {'length':20,'width':35,'height':20}
        room2 = {'length':10,'width':10,'height':10}

        ft_room1 = {}
        ft_room1['ft'] = api.calculate_feet(room1)

        ft_room2 = {}
        ft_room2['ft'] = api.calculate_feet(room2)

        self.assertEqual(api.calculate_gallons_required(ft_room1), 6, "total gallons for room-1 (20,35,20) should be 6")
        self.assertEqual(api.calculate_gallons_required(ft_room2), 1, "total gallons for room-2 (20,20,20) should be 1")