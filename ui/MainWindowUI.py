import wx
import wx.aui as aui
from AterAuiManager import AterAuiManager
from AterAuiNotebook import AterAuiNotebook
from TermianalTabPanel import TerminalTabPanel
from AterMenuBar import AterMenuBar
from AterToolBar import AterToolBar
from ssh.TermEmulator import TermEmulator
from SessionTree import SessionTreeCtrlPanel


class MainWindowUI(wx.Frame):

    def __init__(self, title):
        title = "Ater"
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          title=title, size=(800, 600))
        self.aui_mgr = AterAuiManager(self)

        # add session tree
        self.sessionTreePanel = SessionTreeCtrlPanel(self, size=(150, 600))
        self.aui_mgr.AddPane(self.sessionTreePanel,
                             aui.AuiPaneInfo().Name("AterSessionTree").Left().CloseButton(False).MaximizeButton(
                                 True).MinimizeButton(True).Floatable(True).PaneBorder(True))

        # add terminal tabbed panel
        self.notebook = AterAuiNotebook(self)
        # self.notebook.addPanel("tab-default", TerminalTabPanel, TermEmulator, True)
        self._notebook_style = self.notebook.default_style
        self.aui_mgr.AddPane(self.notebook,
                             aui.AuiPaneInfo().Name("AterTermainalPanel").
                             Center().CloseButton(False).MaximizeButton(True).MinimizeButton(True).Floatable(
                                 True).PaneBorder(True))

        self.aui_mgr.Update()

        self.setIcon()
        self.initBar()

    def setIcon(self):
        ico = wx.Icon('resource/ater-icon.png', wx.BITMAP_TYPE_PNG)
        self.SetIcon(ico)

    def initBar(self):
        self.aterMenuBar = AterMenuBar(self)
        self.aterToolBar = AterToolBar(self)

    def OnExit(self, event):
        self.Close()
