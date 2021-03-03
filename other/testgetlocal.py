import unittest
from getdirinfo import CountFiles

testdir = r'D:\11-壁纸\电脑桌面壁纸'

class TestGlinfo(unittest.TestCase):
    def setUp(self):
        self.obj = CountFiles(path=testdir)
    
    def tearDown(self):
        self.obj = None

    def test_cjpeg(self):
        self.assertEqual(self.obj.cjpeg(), 18)
    
    def test_cpng(self):
        self.assertEqual(self.obj.cpng(), 2)

    def test_cfile(self):
        self.assertEqual(self.obj.cfile(), 0)

    def test_cdir(self):
        self.assertEqual(self.obj.cdir(), 0)
    
if __name__ == '__main__':
    unittest.main()