#coding=utf-8
import os
import wx
import teethchart_functions
import db
import denthist_details
import ins_dentalwork
import config
from economics import SetPatientBalance

img_p=wx.Image("dentworks\DONTIA.png", wx.BITMAP_TYPE_ANY)
img_j=wx.Image("dentworks\NEOGILA.png", wx.BITMAP_TYPE_ANY)
#factor=1.15
#w=img_p.GetWidth()
#h=img_j.GetHeight()
sql="WHERE IDPATIENT='%s'" %db.patients.ids[config.cursor]
dentalhistory = db.Table('dental_hist', sql)
upper_teeth = (11,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,51,52,53,54,55,61,62,63,64,65)
lower_teeth = (31,32,33,34,35,36,37,38,41,42,43,44,45,46,47,48,71,72,73,74,75,81,82,83,84,85)
permanent_teeth = (11,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,31,32,33,34,35,36,37,38,41,42,43,44,45,46,47,48)
juvenile_teeth = (51,52,53,54,55,61,62,63,64,65,71,72,73,74,75,81,82,83,84,85)


#WARNING!!!!! This is slow, img should be replaced by a rescaled image!
#img.Rescale( w*factor, h*factor, wx.IMAGE_QUALITY_HIGH )

class TeethChartPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        dentalworkbuttons=( u"ΟΔΟΝΤΙΚΗ\nΧΕΙΡΟΥΡΓΙΚΗ",u"ΕΝΔΟΔΟΝΤΙΑ",u"ΠΕΡΙΟ",u"ΑΚΙΝΗΤΗ",u"ΚΙΝΗΤΗ",u"ΧΕΙΡΟΥΡΓΙΚΗ",
        u"ΔΙΑΓΝΩΣΤΙΚΗ",u"ΠΑΙΔΟΔΟΝΤΙΑ" )

        font=wx.Font( 9, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        font_big = wx.Font( 13, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.SetFont(font)
        
        mainsizer =wx.BoxSizer( wx.HORIZONTAL )
        add_work_sizer = wx.BoxSizer( wx.VERTICAL ) 
        main_image_sizer = wx.BoxSizer( wx.VERTICAL )
        under_image_sizer = wx.BoxSizer( wx.HORIZONTAL )
        over_image_sizer = wx.BoxSizer( wx.HORIZONTAL )
        details_sizer = wx.BoxSizer( wx.VERTICAL )
        
        for i,btn in enumerate(dentalworkbuttons):
            b = wx.Button( self, label=btn,style=wx.NO_BORDER|wx.BU_EXACTFIT, name=str(i+1) )
            self.Bind(wx.EVT_BUTTON, self.OnClick, b)
            add_work_sizer.Add(b,1,wx.GROW)        
        
        last_name_lbl = wx.StaticText(self, -1, u"Επώνυμο:  ")
        last_name_lbl.SetFont( font_big )
        self.last_name = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY, size=(200,-1))
        self.last_name.SetFont( font_big )
        self.last_name.SetValue('TEST')
        first_name_lbl = wx.StaticText(self, -1, u"Όνομα:  ")
        first_name_lbl.SetFont( font_big )
        self.first_name = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY, size=(200,-1) )
        self.first_name.SetFont( font_big )
        self.first_name.SetValue('TEST')
        over_image_sizer.Add(last_name_lbl, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT|wx.TOP,10)
        over_image_sizer.Add(self.last_name, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.TOP,10)
        over_image_sizer.Add(first_name_lbl, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT|wx.TOP,10)
        over_image_sizer.Add(self.first_name, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.TOP, 10)
        
        nb = ChartNotebook(self)
        
        button = wx.Button( self, label=u"Λεπτομέρειες" )
        box_title = wx.StaticBox( self, -1, u"Φραγμός" )
        box = wx.StaticBoxSizer( box_title, wx.VERTICAL )
        self.radio1 = wx.RadioButton( self, -1, u" Μόνιμος ", style = wx.RB_GROUP, name='1' )
        self.radio2 = wx.RadioButton( self, -1, u" Νεογιλός ", name = '2' )
        box.Add( self.radio1, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
        box.Add( self.radio2, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
        self.current_work_str = wx.StaticText(self, -1, u"Τρέχουσα Εργασία:  ", size=(420,-1) )
        
        det_string1='1'
        det_string2='2'
        det_string3='3'
        
        self.det_addr = wx.StaticText(self, -1, det_string1)
        self.det_tel = wx.StaticText(self, -1, det_string2)
        self.det_bal = wx.StaticText(self, -1, det_string3, name='debt_teeth')
        details_sizer.Add( self.det_addr )
        details_sizer.Add( self.det_tel )
        details_sizer.Add( self.det_bal )
        
        under_image_sizer.Add( box,0, wx.GROW|wx.ALL, 5 )
        under_image_sizer.Add( button,0, wx.GROW|wx.ALL, 5 )
        under_image_sizer.Add( self.current_work_str, 0, wx.GROW|wx.ALL, 5 )
        under_image_sizer.Add( details_sizer, 0, wx.GROW|wx.ALL, 5 )
        
        main_image_sizer.Add( over_image_sizer,0, wx.GROW|wx.ALL, 5 )
        main_image_sizer.Add( wx.StaticLine(self), 0, wx.EXPAND|wx.TOP|wx.BOTTOM )
        main_image_sizer.Add( nb,0, wx.GROW|wx.ALL, 5 )
        main_image_sizer.Add( wx.StaticLine(self), 0, wx.EXPAND|wx.TOP|wx.BOTTOM )
        main_image_sizer.Add( under_image_sizer,0, wx.GROW|wx.ALL, 5 )
        
        mainsizer.Add( add_work_sizer, 1, wx.GROW|wx.ALL, 5 )
        mainsizer.Add( main_image_sizer,9,wx.GROW|wx.ALL,5 )   
        
        self.SetSizer(mainsizer)
        mainsizer.Fit(self)
        self.UpdateControls( db.patients.ids[config.cursor] )
        self.Bind(wx.EVT_BUTTON, self.OnDetailsClick, button)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadio, self.radio1)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadio, self.radio2)
    
    def UpdateControls( self, id_pat ):
        sql="WHERE IDPATIENT='%s'" %id_pat
        global dentalhistory
        dentalhistory = db.Table('dental_hist', sql)
        a = db.patients.data[id_pat]['LASTNAME']
        b = db.patients.data[id_pat]['FIRSTNAME']
        if a:
            self.last_name.ChangeValue(unicode(a))
        else:
            self.last_name.ChangeValue('')
        if b:
            self.first_name.ChangeValue(unicode(b))
        else:
            self.first_name.ChangeValue('') 
        addr=db.patients.data[id_pat]['ADDRESS']+' '+db.patients.data[id_pat]['CITY']
        tel=db.patients.data[id_pat]['TELHOME']
        bal=db.patients.data[id_pat]['BALANCE']
        self.det_addr.SetLabel(unicode(addr))
        self.det_tel.SetLabel(unicode(tel))
        self.det_bal.SetLabel(unicode(bal))
    
    def OnClick(self, evt):
        dialog=ins_dentalwork.InsDentalWork(evt.GetEventObject().GetName())
        result=dialog.ShowModal()
        if result == wx.ID_OK:  
            config.cur_dental_work_id=dialog.dentalwork_id
            config.cur_dental_work_charge=dialog.charge.GetValue()
            config.cur_dental_work_price=dialog.price.GetValue()
            config.cur_dental_work_lab_id=dialog.labdict.get(dialog.lab.GetStringSelection(), 0)
            config.cur_dental_work_lab=dialog.lab.GetStringSelection()
            config.cur_dental_work_material_id=dialog.materialdict.get(dialog.material.GetStringSelection(), 0)
            config.cur_dental_work_material=dialog.material.GetStringSelection()
            config.cur_dental_work_name = dialog.lb.GetStringSelection()
            config.cur_dental_work_date = dialog.datectrl.GetValue().FormatISODate()
            print config.cur_dental_work_lab_id
            print config.cur_dental_work_material_id
        dialog.Destroy()
        self.current_work_str.SetLabel(u'Τρέχουσα Εργασία:  ' + config.cur_dental_work_name) 
    
    def OnRadio( self, evt): 
        self.Refresh()
    
    def OnDetailsClick( self ,evt ):
        dialog=denthist_details.DetailsDlg()
        dialog.ShowModal()          
        dialog.Destroy()
    
class ChartNotebook(wx.Notebook):
    def __init__( self, parent ):
        wx.Notebook.__init__(self, parent, -1, style=wx.BK_DEFAULT|wx.NB_FIXEDWIDTH )
        self.SetTabSize((220,40))
        font=wx.Font( 13, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.SetFont(font)
        self.parent=parent
        nbpanels = ( u"Οδοντιατρικό Ιστορικό", u"Σχέδιο Θεραπείας", u"Αρχική Κατάσταση" ) 
        for txt in nbpanels:
            self.AddPage(TeethImagePanel(self), txt) 
        
class TeethImagePanel(wx.Panel):   
    def __init__(self,parent):
        self.maxWidth = 720
        self.maxHeight = 420
        wx.Panel.__init__(self, parent, size = (self.maxWidth,self.maxHeight), style=wx.RAISED_BORDER)
        self.Bind( wx.EVT_PAINT, self.OnPaint )
        self.Bind( wx.EVT_LEFT_UP, self.OnMouseClick )
        global img_p
        global img_filling
        #
        self.CreateBitmapList()
        
    def OnMouseClick( self, evt ):
        #Find tooth
        teeth = teethchart_functions.Coordinates.GetToothFromCoordinates(evt.GetPosition())
        x=evt.GetPosition()
        print teeth
        for i in teeth:
            if self.GetParent().GetParent().radio1.GetValue() and (i in permanent_teeth):
                tooth = i
            elif self.GetParent().GetParent().radio2.GetValue() and (i in juvenile_teeth):
                tooth = i         
        #print tooth
        if tooth:
            record = self.CreateDentalWorkRecord( tooth )         # create a new rec
        print record
        if record['IDDENTALWORK']>0:
            charge = str(record['CHARGE'])
            dentalhistory.data[''] = record
            dentalhistory.Insert()
            SetPatientBalance( '0', charge )
            #dentalhistory.Refresh()
            self.Refresh()
 
    def CreateDentalWorkRecord( self, tooth ):
        ther_level_dict = { 0:2, 1:1, 2:0 }
        record = {}
        record['IDPATIENT'] = db.patients.ids[config.cursor]
        record['IDDENTALWORK'] = config.cur_dental_work_id           #int   
        record['IDTECHNICIAN'] = config.cur_dental_work_lab_id         #int
        record['TECHNICIAN'] = config.cur_dental_work_lab
        record['IDMATERIAL'] = config.cur_dental_work_material_id    #int
        record['MATERIAL'] = config.cur_dental_work_material
        record['THERAPYLEVEL'] = str(ther_level_dict[self.GetParent().GetSelection()])
        record['DATE'] = config.cur_dental_work_date
        record['TOOTH'] = tooth                                      #int
        record['NAME'] = config.cur_dental_work_name
        record['PRICE'] = config.cur_dental_work_price               #real
        record['CHARGE'] = config.cur_dental_work_charge             #real
        record['CATEGORY'] = config.cur_dental_work_category         #int
        return record
    
    def CreateBitmapList( self ):
        self.dent_bitmap_dict = {}
        for i in db.dentalworkbmps.data:
           path = "dentworks\\"+db.dentalworkbmps.data[i]['BMP_NAME']
           if os.path.isfile(path):
               self.dent_bitmap_dict[db.dentalworkbmps.data[i]['ID']]=wx.Image(path, wx.BITMAP_TYPE_ANY).ConvertToBitmap()     
    
    def OnPaint( self, evt ):
        ther_level_dict = { 0:2, 1:1, 2:0 }
        mdc = wx.MemoryDC()
        dc = wx.BufferedPaintDC(self)
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        #p: (permanent) index showing if we see juvenille(p=0) or permanent(p=1)  teeth
        if self.GetParent().GetParent().radio1.GetValue():
            self.teeth = img_p.ConvertToBitmap()
            p = 1
        else:
            self.teeth = img_j.ConvertToBitmap()
            p = 0
        dc.DrawBitmap(self.teeth,0,0)
    
        u_1 = []
        u_2 = []
        u_3 = []
        u_4 = []
        d_1 = []
        d_2 = []
        d_3 = []
        d_4 = []
        ud_5 = []
        extr_teeth = []
        id_lists = ( u_1, u_2, u_3, u_4, d_1, d_2, d_3, d_4, ud_5 )
        upper_denture_flag = lower_denture_flag = 0
        for x in dentalhistory.data:
            id_dentalwork = dentalhistory.data[x]['IDDENTALWORK']
            tooth = dentalhistory.data[x]['TOOTH']
            if db.dentalworks.data.get(id_dentalwork):
                priority = db.dentalworks.data.get(id_dentalwork).get('PRIORITY') 
                therapy_level = int(dentalhistory.data[x]['THERAPYLEVEL'])
                active_page = ther_level_dict[self.GetParent().GetSelection()]
                if priority == 1 and therapy_level == active_page:
                    if tooth in upper_teeth:
                        u_1.append(x)
                    else:
                        d_1.append(x)
                if priority == 2 and therapy_level == active_page:
                    extr_teeth.append(tooth)
                    if tooth in upper_teeth:
                        u_2.append(x)
                    else:
                        d_2.append(x)
                if priority == 3 and therapy_level == active_page:
                    if tooth in upper_teeth:
                        u_3.append(x)
                    else:
                        d_3.append(x)
                if priority == 4 and therapy_level == active_page:
                    if tooth in upper_teeth:
                        u_4.append(x)
                    else:
                        d_4.append(x)
                if priority == 5 and therapy_level == active_page:
                    ud_5.append(x)
              
#****UPPER JAW - Draw Priority 1 Dental Works - full dentures 
        if len(u_1)>0 and p:
            upper_denture_flag = 1
            for i in u_1:
                data_line = dentalhistory.data[i]
                id_dentalwork = data_line['IDDENTALWORK']
                if db.dentalworks.data.get(id_dentalwork):
                    tooth = 1020
                    (x_dest, y_dest, d_x, d_y, x_src, y_src)=teethchart_functions.Coordinates.GetToothCoordinates(tooth) 
                    id_bmp = db.dentalworks.data[id_dentalwork]['BITMAP']
                    source = self.dent_bitmap_dict.get(id_bmp)
                    if source:
                        mdc.SelectObjectAsSource(source)
                        dc.Blit(x_dest,y_dest, d_x, d_y, mdc, x_src, y_src, wx.COPY)    
            
#****UPPER JAW - Draw Priority 2 Dental Works  - extractions
        if upper_denture_flag <>1 or not p:
            for i in u_2:
                id_dentalwork = dentalhistory.data[i]['IDDENTALWORK']
                if db.dentalworks.data.get(id_dentalwork):
                    tooth = dentalhistory.data[i]['TOOTH']
                    if ((tooth in permanent_teeth) and p) or ((tooth in juvenile_teeth) and not p):
                        (x_dest, y_dest, d_x, d_y, x_src, y_src)=teethchart_functions.Coordinates.GetToothCoordinates(tooth) 
                        id_bmp = db.dentalworks.data[id_dentalwork]['BITMAP']
                        source = self.dent_bitmap_dict.get(id_bmp)
                        if source:
                            mdc.SelectObjectAsSource(source)
                            dc.Blit(x_dest,y_dest, d_x, d_y, mdc, x_src, y_src, wx.COPY)    
#****UPPER JAW - Draw Priority 3 Dental Works - works on any tooth
        if upper_denture_flag <>1:
            for i in u_3:
                id_dentalwork = dentalhistory.data[i]['IDDENTALWORK']
                if db.dentalworks.data.get(id_dentalwork):
                    tooth = dentalhistory.data[i]['TOOTH']
                    if ((tooth in permanent_teeth) and p) or ((tooth in juvenile_teeth) and not p):
                        (x_dest, y_dest, d_x, d_y, x_src, y_src)=teethchart_functions.Coordinates.GetToothCoordinates(tooth) 
                        id_bmp = db.dentalworks.data[id_dentalwork]['BITMAP']
                        source = self.dent_bitmap_dict.get(id_bmp)
                        if source:
                            mdc.SelectObjectAsSource(source)
                            dc.Blit(x_dest,y_dest, d_x, d_y, mdc, x_src, y_src, wx.COPY)       
#****UPPER JAW - Draw Priority 4 Dental Works - works on non-extracted teeth
        if upper_denture_flag <>1:
            for i in u_4:
                tooth = dentalhistory.data[i]['TOOTH']
                if (tooth not in extr_teeth) and (((tooth in permanent_teeth) and p) or ((tooth in juvenile_teeth) and not p)):
                    id_dentalwork = dentalhistory.data[i]['IDDENTALWORK']
                    if db.dentalworks.data.get(id_dentalwork):
                        (x_dest, y_dest, d_x, d_y, x_src, y_src)=teethchart_functions.Coordinates.GetToothCoordinates(tooth) 
                        id_bmp = db.dentalworks.data[id_dentalwork]['BITMAP']
                        source = self.dent_bitmap_dict.get(id_bmp)
                        if source:
                            mdc.SelectObjectAsSource(source)
                            dc.Blit(x_dest,y_dest, d_x, d_y, mdc, x_src, y_src, wx.COPY)               

#****LOWER JAW - Draw Priority 1 Dental Works - full dentures 
        if len(d_1)>0 and p:
            lower_denture_flag = 1
            for i in d_1:
                id_dentalwork = dentalhistory.data[i]['IDDENTALWORK']
                if db.dentalworks.data.get(id_dentalwork):
                    tooth = 4030
                    (x_dest, y_dest, d_x, d_y, x_src, y_src)=teethchart_functions.Coordinates.GetToothCoordinates(tooth) 
                    id_bmp = db.dentalworks.data[id_dentalwork]['BITMAP']
                    source = self.dent_bitmap_dict.get(id_bmp)
                    if source:
                        mdc.SelectObjectAsSource(source)
                        dc.Blit(x_dest,y_dest, d_x, d_y, mdc, x_src, y_src, wx.COPY)    
        
#****LOWER JAW - Draw Priority 2 Dental Works  - extractions
        if lower_denture_flag <>1 or not p:
            for i in d_2:
                id_dentalwork = dentalhistory.data[i]['IDDENTALWORK']
                if db.dentalworks.data.get(id_dentalwork):
                    tooth = dentalhistory.data[i]['TOOTH']
                    if ((tooth in permanent_teeth) and p) or ((tooth in juvenile_teeth) and not p):
                        (x_dest, y_dest, d_x, d_y, x_src, y_src)=teethchart_functions.Coordinates.GetToothCoordinates(tooth) 
                        id_bmp = db.dentalworks.data[id_dentalwork]['BITMAP']
                        source = self.dent_bitmap_dict.get(id_bmp)
                        if source:
                            mdc.SelectObjectAsSource(source)
                            dc.Blit(x_dest,y_dest, d_x, d_y, mdc, x_src, y_src, wx.COPY)    
#****LOWER JAW - Draw Priority 3 Dental Works - works on any tooth
        if lower_denture_flag <>1:
            for i in d_3:
                id_dentalwork = dentalhistory.data[i]['IDDENTALWORK']
                if db.dentalworks.data.get(id_dentalwork):
                    tooth = dentalhistory.data[i]['TOOTH']
                    if ((tooth in permanent_teeth) and p) or ((tooth in juvenile_teeth) and not p):
                        (x_dest, y_dest, d_x, d_y, x_src, y_src)=teethchart_functions.Coordinates.GetToothCoordinates(tooth) 
                        id_bmp = db.dentalworks.data[id_dentalwork]['BITMAP']
                        source = self.dent_bitmap_dict.get(id_bmp)
                        if source:
                            mdc.SelectObjectAsSource(source)
                            dc.Blit(x_dest,y_dest, d_x, d_y, mdc, x_src, y_src, wx.COPY)       
#****LOWER JAW - Draw Priority 4 Dental Works - works on non-extracted teeth
        if lower_denture_flag <>1:
            for i in d_4:
                tooth = dentalhistory.data[i]['TOOTH']
                if (tooth not in extr_teeth) and (((tooth in permanent_teeth) and p) or ((tooth in juvenile_teeth) and not p)):
                    id_dentalwork = dentalhistory.data[i]['IDDENTALWORK']
                    if db.dentalworks.data.get(id_dentalwork):
                        (x_dest, y_dest, d_x, d_y, x_src, y_src)=teethchart_functions.Coordinates.GetToothCoordinates(tooth) 
                        id_bmp = db.dentalworks.data[id_dentalwork]['BITMAP']
                        source = self.dent_bitmap_dict.get(id_bmp)
                        if source:
                            mdc.SelectObjectAsSource(source)
                            dc.Blit(x_dest,y_dest, d_x, d_y, mdc, x_src, y_src, wx.COPY) 
 
 #****FULL MOUTH - Draw Priority 5 Dental Works - works on the whole mouth
        if lower_denture_flag<>1 or upper_denture_flag<>1:
            for i in ud_5:
                id_dentalwork = dentalhistory.data[i]['IDDENTALWORK']
                if db.dentalworks.data.get(id_dentalwork):
                    tooth = 1234
                    (x_dest, y_dest, d_x, d_y, x_src, y_src)=teethchart_functions.Coordinates.GetToothCoordinates(tooth) 
                    id_bmp = db.dentalworks.data[id_dentalwork]['BITMAP']
                    source = self.dent_bitmap_dict.get(id_bmp)
                    if source:
                        mdc.SelectObjectAsSource(source)
                        dc.Blit(x_dest,y_dest, d_x, d_y, mdc, x_src, y_src, wx.COPY)        
        
if __name__=='__main__':
    app = wx.PySimpleApp(False)
    frame=wx.Frame(None, size=(950,730))
    pnl=TeethChartPanel(frame)
    frame.Show()
    app.MainLoop()
