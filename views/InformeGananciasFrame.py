#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.4 on Fri May 10 10:09:16 2013

import wx

# begin wxGlade: extracode
# end wxGlade


class InformeGananciasFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: InformeListaFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        self.lbl_mes = wx.StaticText(self.panel_1, -1, "Mes:")
        self.combo_box_1 = wx.ComboBox(self.panel_1, -1, choices=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"], style=wx.CB_DROPDOWN)
        self.lbl_mes_copy = wx.StaticText(self.panel_1, -1, u"A�o:")
        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, -1, "", style=wx.TE_PROCESS_ENTER)
        self.panel_2 = wx.Panel(self, -1)
        self.list_titulo = wx.ListCtrl(self.panel_2, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.btn_detalle = wx.Button(self, -1, "Detalle...")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: InformeListaFrame.__set_properties
        self.SetTitle("frame_2")
        self.SetSize((515, 415))
        self.lbl_mes.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.combo_box_1.SetSelection(-1)
        self.lbl_mes_copy.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.text_ctrl_1.SetMinSize((50, 26))
        self.list_titulo.SetMinSize((500, 290))
        self.list_titulo.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: InformeListaFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 1, 0, 0)
        sizer_2_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.lbl_mes, 0, wx.ALL, 10)
        sizer_4.Add(self.combo_box_1, 0, wx.ALL, 15)
        sizer_4.Add(self.lbl_mes_copy, 0, wx.ALL, 10)
        sizer_4.Add(self.text_ctrl_1, 0, wx.TOP, 15)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_1)
        grid_sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        sizer_2_copy.Add(self.list_titulo, 1, wx.ALL | wx.EXPAND, 10)
        self.panel_2.SetSizer(sizer_2_copy)
        grid_sizer_1.Add(self.panel_2, 1, wx.EXPAND, 0)
        sizer_2.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_2.Add(self.btn_detalle, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 10)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade

# end of class InformeListaFrame
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_2 = InformeGananciasFrame(None, -1, "")
    app.SetTopWindow(frame_2)
    frame_2.Show()
    app.MainLoop()
