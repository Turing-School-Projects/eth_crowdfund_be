import unittest
from ..services.ConversionService import ConversionService

class PriceConverterTest(unittest.TestCase): 

    def setUp(self): 
        self.conversion_service = ConversionService()

    def test_wei_to_eth(self):
        wei = 1e18
        eth = self.conversion_service.wei_to_eth(wei)
        self.assertEqual(eth, 1)