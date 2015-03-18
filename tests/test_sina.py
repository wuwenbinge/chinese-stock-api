# coding=utf-8
# system library
import unittest
import datetime

# project library
from cstock.sina_engine import SinaEngine


class TestEngine(unittest.TestCase):

    def setUp(self):
        self.engine = SinaEngine()

    def test_get_url(self):
        url = self.engine.get_url('600010') 
        self.assertEqual(url, "http://hq.sinajs.cn/list=sh600010")

    def test_parse(self):
        data = 'var hq_str_sh600010="包钢股份,5.98,5.99,6.15,6.34,5.95,6.15,6.16,542628944,3341837325,239800,6.15,1033800,6.14,2408711,6.13,1719525,6.12,1001900,6.11,2873590,6.16,1481300,6.17,2113716,6.18,1177600,6.19,2587603,6.20,2015-03-18,15:03:05,00";'

        stock = self.engine.parse(data, 'foo_id')

        self.assertEqual(
            stock.as_dict(),
            {'close': '5.99',
             'code': 'foo_id',
             'high': '6.34',
             'low': '5.95',
             'name': '\xe5\x8c\x85\xe9\x92\xa2\xe8\x82\xa1\xe4\xbb\xbd',
             'open': '5.98',
             'price': '6.15',
             'turnover': '3341837325',
             'volume': '542628944',
             'date': '2015-03-18',
             'time': '15:03:05'}
        )
