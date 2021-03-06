import unittest
from penmon.eto import Station

class Test(unittest.TestCase):

    def test_daylight_hours(self):
        station = Station(41.42, 109)
        day = station.day(135)
        day.temp_min = 19.5
        day.temp_max = 28

        self.assertEqual(day.daylight_hours(), 14.3, "daylighth_hours")

if __name__ == "__main__":
    unittest.main()
    