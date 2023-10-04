import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    s1, b1, a1, p1 = getDataPoint(quotes[0])
    s2, a2, b2, p2 = getDataPoint(quotes[1])
    self.assertEqual(p1, 120.84)
    self.assertEqual(p2, 119.775)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    s1, b1, a1, p1 = getDataPoint(quotes[0])
    s2, a2, b2, p2 = getDataPoint(quotes[1])
    self.assertEqual(p1, 119.84)
    self.assertEqual(p2, 119.775)

  def test_getRatio_0dot5(self):
     ratio = getRatio(100, 200)
     self.assertEqual(ratio, 0.5)

  def test_getRatio_1(self):
     ratio = getRatio(150, 150)
     self.assertEqual(ratio, 1)

  def test_getRatio_exception(self):
     ratio = getRatio(150, 0)
     self.assertEqual(ratio, None)


if __name__ == '__main__':
    unittest.main()
