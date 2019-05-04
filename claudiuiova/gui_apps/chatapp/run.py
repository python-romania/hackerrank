import wx
from chat_gui import Interface


if __name__ == "__main__":
    app = wx.App()
    frame = Interface(None, title="Chattwin", size=(960, 640))
    frame.Show()
    app.MainLoop()
