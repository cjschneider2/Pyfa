import wx
from service.fit import Fit

import gui.mainFrame
from gui import globalEvents as GE
from .calc.fitAddCommand import FitAddCommandCommand


class GuiAddCommandCommand(wx.Command):
    def __init__(self, fitID, commandFitID):
        wx.Command.__init__(self, True, "")
        self.mainFrame = gui.mainFrame.MainFrame.getInstance()
        self.sFit = Fit.getInstance()
        self.internal_history = wx.CommandProcessor()
        self.fitID = fitID
        self.commandFitID = commandFitID

    def Do(self):
        if self.internal_history.Submit(FitAddCommandCommand(self.fitID, self.commandFitID)):
            wx.PostEvent(self.mainFrame, GE.FitChanged(fitID=self.fitID))
            self.sFit.recalc(self.fitID)
            return True
        return False

    def Undo(self):
        for _ in self.internal_history.Commands:
            self.internal_history.Undo()
        self.sFit.recalc(self.fitID)
        wx.PostEvent(self.mainFrame, GE.FitChanged(fitID=self.fitID))
        return True
