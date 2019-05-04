import wx
import wx.grid as gridlib


class UsersPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super(UsersPanel, self).__init__(*args, **kw)

        grid = gridlib.Grid(self)
        grid.CreateGrid(5, 1)

        sizer = wx.BoxSizer()
        sizer.Add(grid, 0, wx.EXPAND)
        self.SetSizer(sizer)


class MessagesPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super(MessagesPanel, self).__init__(*args, **kw)

        grid = gridlib.Grid(self)
        grid.CreateGrid(25, 12)

        # sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(grid, 0, wx.EXPAND)
        # self.SetSizer(sizer)


class TextBoxPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super(TextBoxPanel, self).__init__(*args, **kw)
        wx.TextCtrl(self)


class Interface(wx.Frame):
    def __init__(self, *args, **kw):
        super(Interface, self).__init__(*args, **kw)
        self.create_interface()

    def create_interface(self):
        splitter = wx.SplitterWindow(self)
        left_p = UsersPanel(splitter)
        right_p = TextBoxPanel(splitter)

        # split the window
        splitter.SplitVertically(left_p, right_p)
        splitter.SetMinimumPaneSize(180)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)


