Th# Test cases for COSI 107a Lab 6 - TinySSl

import unittest

from tinyssl_client import TinySSLClient

class RecordFormatTestCase(unittest.TestCase):
    def setUp(self):
        self.tsclient = TinySSLClient()

    def test_make_record_basic(self):
        testdata = 'This is a test'.encode()
        result = self.tsclient.make_record(testdata)
        self.assertEqual(result[0] & 0x80, 0x80,
                         "High bit in first byte not set")
        datalen = ((result[0] & 0x7f) << 8) | result[1];
        self.assertEqual(datalen, len(testdata),
                         "Unexpected length value")
        self.assertEqual(len(result), len(testdata) + 2,
                         "Length of data does not match header")

    def test_receive_record_basic(self):
        test_data = b'\x80\x18This is yet another test'
        expected = 'This is yet another test'.encode()
        result = self.tsclient.decode_record(test_data)
        self.assertEqual(result, expected,
                         "Unexpected data")

if __name__ == '__main__':
    unittest.main()
