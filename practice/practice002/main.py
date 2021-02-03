#! env python
# -*- coding: utf-8 -*-

import os
import sys
import wx
from MyProject1MyFrame1 import MyProject1MyFrame1

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyProject1MyFrame1(None)
    frame.Show(True)
    app.MainLoop()
