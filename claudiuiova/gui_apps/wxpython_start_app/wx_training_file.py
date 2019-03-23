import wx


class ApplicationObject(wx.App):
    def __init__(self):
        super(ApplicationObject, self).__init__(self)
        self.create_frame()
        self.MainLoop()

    @staticmethod
    def create_frame():
        """
        Constructor arguments:
        wx.Frame(wx.Window parent, int id=-1, string title='', wx.Point pos=wx.DefaultPosition,
                wx.Size size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, string name="frame")
        :return:
        """
        wx.Frame(None, title="First WX GUI!").Show()


ApplicationObject()
