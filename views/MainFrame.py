#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade HG on Thu Mar 14 17:01:31 2013

import wx

# begin wxGlade: extracode
# end wxGlade



class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.MAXIMIZE | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.RESIZE_BORDER | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.frame_menubar.Append(wxglade_tmp_menu, "Archivo")
        wxglade_tmp_menu = wx.Menu()
        self.frame_menubar.Append(wxglade_tmp_menu, "Editar")
        wxglade_tmp_menu = wx.Menu()
        self.frame_menubar.Append(wxglade_tmp_menu, "Ver")
        wxglade_tmp_menu = wx.Menu()
        self.frame_menubar.Append(wxglade_tmp_menu, "Ayuda")
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        self.panel_1 = wx.Panel(self, -1)
        self.boton_solapas_prendas_clientes = wx.Notebook(self.panel_1, -1, style=0)
        self.notebook_1_pane_1 = wx.Panel(self.boton_solapas_prendas_clientes, -1)
        self.texto_buscar_prendas = wx.TextCtrl(self.notebook_1_pane_1, -1, "Buscar...")
        self.radio_btn_codigo_prendas = wx.RadioButton(self.notebook_1_pane_1, -1, "Codigo", style=wx.RB_GROUP)
        self.radio_btn_nombre_prendas = wx.RadioButton(self.notebook_1_pane_1, -1, "Nombre", style=wx.RB_GROUP)
        self.lista_prendas = wx.ListCtrl(self.notebook_1_pane_1, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.boton_detalle_prendas = wx.Button(self.notebook_1_pane_1, -1, "&Detalle")
        self.boton_eliminar_prendas = wx.Button(self.notebook_1_pane_1, -1, "&Eliminar")
        self.boton_nuevo_prendas = wx.Button(self.notebook_1_pane_1, -1, "&Nuevo")
        self.boton_agregar_quitar = wx.Button(self.notebook_1_pane_1, -1, "Agregar")
        self.button_realizar_venta = wx.Button(self.notebook_1_pane_1, -1, "Realizar &Venta")
        self.notebook_1_pane_2 = wx.Panel(self.boton_solapas_prendas_clientes, -1)
        self.texto_buscar_clientes = wx.TextCtrl(self.notebook_1_pane_2, -1, "Buscar...")
        self.radio_btn_dni_cliente = wx.RadioButton(self.notebook_1_pane_2, -1, "DNI", style=wx.RB_GROUP)
        self.radio_btn_nombre_cliente = wx.RadioButton(self.notebook_1_pane_2, -1, "Nombre", style=wx.RB_GROUP)
        self.lista_clientes = wx.ListCtrl(self.notebook_1_pane_2, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.boton_detalle_clientes = wx.Button(self.notebook_1_pane_2, -1, "&Detalle")
        self.boton_eliminar_clientes = wx.Button(self.notebook_1_pane_2, -1, "&Eliminar")
        self.boton_nuevo_clientes = wx.Button(self.notebook_1_pane_2, -1, "&Nuevo")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("Dress")
        self.SetSize((803, 500))
        self.SetFocus()
        self.texto_buscar_prendas.SetMinSize((250, 22))
        self.texto_buscar_prendas.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.radio_btn_codigo_prendas.SetMinSize((62, 42))
        self.radio_btn_codigo_prendas.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.radio_btn_nombre_prendas.SetMinSize((62, 42))
        self.radio_btn_nombre_prendas.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.lista_prendas.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.boton_detalle_prendas.SetDefault()
        self.button_realizar_venta.SetMinSize((130, 30))
        self.button_realizar_venta.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.notebook_1_pane_1.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.texto_buscar_clientes.SetMinSize((250, 22))
        self.texto_buscar_clientes.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.radio_btn_dni_cliente.SetMinSize((37, 42))
        self.radio_btn_dni_cliente.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.radio_btn_nombre_cliente.SetMinSize((69, 42))
        self.radio_btn_nombre_cliente.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.lista_clientes.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.boton_detalle_clientes.SetDefault()
        self.boton_solapas_prendas_clientes.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_6_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_4_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.texto_buscar_prendas, 0, wx.ALL, 10)
        sizer_5.Add(self.radio_btn_codigo_prendas, 0, wx.RIGHT | wx.EXPAND, 16)
        sizer_5.Add(self.radio_btn_nombre_prendas, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(sizer_5, 1, wx.LEFT | wx.EXPAND, 20)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_6.Add(self.lista_prendas, 1, wx.LEFT | wx.RIGHT | wx.EXPAND | wx.ALIGN_RIGHT, 10)
        sizer_7.Add(self.boton_detalle_prendas, 0, wx.TOP | wx.BOTTOM, 3)
        sizer_7.Add(self.boton_eliminar_prendas, 0, wx.TOP | wx.BOTTOM, 3)
        sizer_7.Add(self.boton_nuevo_prendas, 0, wx.TOP | wx.BOTTOM, 3)
        sizer_7.Add(self.boton_agregar_quitar, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 120)
        sizer_6.Add(sizer_7, 0, wx.RIGHT, 10)
        sizer_3.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_8.Add(self.button_realizar_venta, 0, wx.ALL | wx.ALIGN_RIGHT, 10)
        sizer_3.Add(sizer_8, 0, wx.ALIGN_RIGHT, 0)
        self.notebook_1_pane_1.SetSizer(sizer_3)
        sizer_4_copy.Add(self.texto_buscar_clientes, 0, wx.ALL, 10)
        sizer_5_copy.Add(self.radio_btn_dni_cliente, 0, wx.RIGHT | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 20)
        sizer_5_copy.Add(self.radio_btn_nombre_cliente, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4_copy.Add(sizer_5_copy, 1, wx.LEFT | wx.EXPAND, 20)
        sizer_3_copy.Add(sizer_4_copy, 0, wx.EXPAND, 0)
        sizer_6_copy.Add(self.lista_clientes, 1, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND | wx.ALIGN_RIGHT, 10)
        sizer_7_copy.Add(self.boton_detalle_clientes, 0, wx.ALL, 3)
        sizer_7_copy.Add(self.boton_eliminar_clientes, 0, wx.ALL, 3)
        sizer_7_copy.Add(self.boton_nuevo_clientes, 0, wx.ALL, 3)
        sizer_6_copy.Add(sizer_7_copy, 0, wx.RIGHT, 10)
        sizer_3_copy.Add(sizer_6_copy, 1, wx.EXPAND, 0)
        self.notebook_1_pane_2.SetSizer(sizer_3_copy)
        self.boton_solapas_prendas_clientes.AddPage(self.notebook_1_pane_1, "Prendas")
        self.boton_solapas_prendas_clientes.AddPage(self.notebook_1_pane_2, "Clientes")
        sizer_2.Add(self.boton_solapas_prendas_clientes, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class MainFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MainFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
