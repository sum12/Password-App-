#
#edit password not working
#filter to prevent a earlier existing alias or empty alias
import wx,filehandlingmod
from pyDes import *
       
#########################################################################################################################################################################
class filters():
    def newuser_filter(self,s,sb1,sb2,x):
        if sb1 == '' :
            dlg = wx.MessageDialog(s, 'Username cannot be kept blank', 'Error', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        elif sb2 == '':
            dlg = wx.MessageDialog(s, 'Phone number cannot be kept blank', 'Error', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        elif x.username_search(str(sb1),0)==1:
            dlg = wx.MessageDialog(s, 'Username already exists in our database \nKindly select a new username', 'Error', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        elif x.username_search(str(sb2),1)==1:
            dlg = wx.MessageDialog(s, 'Phone number already registered in our database \nKindly enter another number', 'Error', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        else : 
            return 1

    def save_new_password_filter(self,s,b):
        #NON BLANK ALIAS CHECKER
        if b == '' :
            dlg = wx.MessageDialog(s, 'Alias cannot be kept blank\nIt wil help your retrieve your password\nSelect one such that you can remember', 'Error', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        return 1

#########################################################################################################################################################################

class authentication(wx.Frame):
    def __init__(self,parent,title,b):
        wx.Frame.__init__(self,parent,title = title,size = (400,275))
        panel = wx.Panel(self,-1)
        
        vsizer = wx.BoxSizer(wx.VERTICAL)

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_b = wx.BoxSizer(wx.HORIZONTAL)
        
        st1 = wx.StaticText(panel,-1,"Enter your Name :\n(First + Last name) ")
        self.sb1 = wx.TextCtrl(panel,-1)
        hsizer1.Add(st1,1,wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL,10)
        hsizer1.Add(self.sb1,2,0,0)
        
        st2 = wx.StaticText(panel,-1,"Enter the phone number : \n(with which u registered the account) ")
        self.sb2 = wx.TextCtrl(panel,-1)
        hsizer2.Add(st2,1,wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL,0)
        hsizer2.Add(self.sb2,2,0,0)

        self.b1 = wx.Button(panel,1,"Login")
        self.b1.Bind(wx.EVT_BUTTON,self.login)
        self.b2 = wx.Button(panel,1,"Exit")
        self.b2.Bind(wx.EVT_BUTTON,self.quit)
        self.b3 = wx.Button(panel,1,"New User")
        self.b3.Bind(wx.EVT_BUTTON,self.user_reg)

        hsizer_b.Add(self.b1,0,wx.ALIGN_CENTER_HORIZONTAL,0)
        hsizer_b.Add(self.b2,0,wx.ALIGN_CENTER_HORIZONTAL,0)
        hsizer_b.Add(self.b3,0,wx.ALIGN_CENTER_HORIZONTAL,0)
        
        vsizer.Add(hsizer1,2,wx.ALIGN_CENTER_HORIZONTAL|wx.UP,10)
        vsizer.Add(hsizer2,2,wx.ALIGN_CENTER_HORIZONTAL,0)
        vsizer.Add(hsizer_b,2,wx.ALIGN_CENTER_HORIZONTAL|wx.UP,10)

        self.current_user_name = ''
        self.current_user = 0
        self.alluserinfo = []
        
        panel.SetSizer(vsizer)
        self.Centre()
        self.Show(b)
        
    def login(self,e):
        self.userinfo()
        i = self.user_match()
        if i == 1:
            t = main(None,"Welcome " + self.alluserinfo[self.current_user][0],self.current_user_name,self.current_user)
            self.quit(e)
        else:
            self.st1 = wx.StaticText(self,-1,"Either of your credentials are wrong\n Kindly make changes and retry with login",(80,125),style = wx.ALIGN_CENTRE)
            
    def userinfo(self):
        x = filehandlingmod.filehandling()
        t = x.userinfo()
        self.alluserinfo = t
    def user_match(self):
        t1,t2 = str(self.sb1.GetValue()),str(self.sb2.GetValue())
        for i in range(len(self.alluserinfo)):
            if t1 == str(self.alluserinfo[i][0]) and t2 == str(self.alluserinfo[i][1]):
                self.current_user = i
                self.current_user_name = str(self.alluserinfo[i][0])
                return 1;
        return 0
                
    def user_reg(self,e):
        a = user_regestration(None,"Register yourself user")
        
    
    def quit(self,e):
        self.Close()
    
"""        st3 = wx.StaticText(panel,-1,"Securtiy question")
        self.sb3 = wx.TextCtrl(panel,-1)
        vsizer.Add(st3,1,wx.RIGHT,70)
        vsizer.Add(self.sb3,2,0,0)
"""
##########################################################################################################################################################################
class main(wx.Frame):

    def __init__(self,parent,title,user,identity):
        wx.Frame.__init__(self,parent,title = title,size= (466,100))
        panel = wx.Panel(self,-1)

        sizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.b1 = wx.Button(panel,1,"Save password")
        self.b2 = wx.Button(panel,1,"Retrieve password")
        self.b3 = wx.Button(panel,1,"Edit password")
        self.b4 = wx.Button(panel,1,"Exit")

        sizer1.Add(self.b1,1,wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND,wx.ALL)
        sizer1.Add(self.b2,1,wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND,wx.ALL)
        sizer1.Add(self.b3,1,wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND,wx.ALL)
        sizer1.Add(self.b4,1,wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND,wx.ALL)
        
        self.b1.Bind(wx.EVT_BUTTON,self.savenewpassword)        
        self.b2.Bind(wx.EVT_BUTTON,self.reviewpassword)
        self.b3.Bind(wx.EVT_BUTTON,self.editpassword)
        self.b4.Bind(wx.EVT_BUTTON,self.quit)

        self.current_user_name = user
        self.current_user = identity 
        panel.SetSizer(sizer1)
        self.Centre()
        self.Show()
        
    def savenewpassword(self,e):
        a = npass(None,"Save your password",self.current_user_name ,self.current_user + 1)
        
    def reviewpassword(self,e):
        a = rpass(None,"Review your saved passwords",self.current_user_name ,self.current_user + 1)

    def editpassword(self,e):
        a = editpass(None,"Edit your credentials",self.current_user_name ,self.current_user + 1)
        
    def quit(self,e):
        self.Close()

##########################################################################################################################################################################
class cryptography():
    def __init__(self,t):
        self.k = des("RATNANEO", CBC, "\1\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        f = open('C:\Users\DJ\Documents\pss.txt','r+')
        self.data = f.read()
        f.close()

        if t == 'e':
            self.encryptdata()
        elif t == 'd':
            self.decryptdata()
    def encryptdata(self):
        x = self.k.encrypt(self.data)
        f = open('C:\Users\DJ\Documents\pss.txt','r+')
        f.write(x)
        f.close()
    def decryptdata(self):
        x = self.k.decrypt(self.data)
        f = open('C:\Users\DJ\Documents\pss.txt','r+')
        f.write(x)
        f.close()
##########################################################################################################################################################################

class user_regestration(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title = title)
        panel = wx.Panel(self,-1)
        vsizer = wx.BoxSizer(wx.VERTICAL)

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_b = wx.BoxSizer(wx.HORIZONTAL)

        st1 = wx.StaticText(panel,-1,"Enter your Name \n(First + Last name) :")
        self.sb1 = wx.TextCtrl(panel,-1)
        hsizer1.Add(st1,1,wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL,10)
        hsizer1.Add(self.sb1,2,0,0)

        st2 = wx.StaticText(panel,-1,"Enter the phone number \n(with which you want to register your account) :")
        self.sb2 = wx.TextCtrl(panel,-1)
        hsizer2.Add(st2,1,wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL,0)
        hsizer2.Add(self.sb2,2,0,0)

        self.b1 = wx.Button(panel,1,"Save")
        self.b1.Bind(wx.EVT_BUTTON,self.save)
        self.b2 = wx.Button(panel,1,"Exit")
        self.b2.Bind(wx.EVT_BUTTON,self.quit)

        hsizer_b.Add(self.b1,0,wx.ALIGN_CENTER_HORIZONTAL,0)
        hsizer_b.Add(self.b2,0,wx.ALIGN_CENTER_HORIZONTAL,0)
        
        vsizer.Add(hsizer1,2,wx.ALIGN_CENTER_HORIZONTAL,0)
        vsizer.Add(hsizer2,2,wx.ALIGN_CENTER_HORIZONTAL,0)
        vsizer.Add(hsizer_b,2,wx.ALIGN_CENTER_HORIZONTAL,0)
        #vsizer.Add(hsizer1,2,0,0)

        panel.SetSizer(vsizer)
        self.Centre()
        self.Show()

    def save(self,e):
        #temp = crytography('')
        x = filehandlingmod.filehandling()
        y = filters()
        if (y.newuser_filter(self,self.sb1.GetValue(),self.sb2.GetValue(),x)) :
            x.save_new_user(self.sb1.GetValue(),self.sb2.GetValue())
            self.Close()     
    def quit(self,e):
        self.Close()

##########################################################################################################################################################################

class editpass(wx.Frame):
    def __init__(self,parent,title,user,identity):
        wx.Frame.__init__(self,parent,title = title)
        panel = wx.Panel(self,-1)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer4 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.user = user
        self.identity = identity

        x=filehandlingmod.filehandling()
        string = x.dropdown_options_in_rpass(self.user)

        self.cb = wx.ComboBox(panel,-1,'Select the alias with which you saved your data',size = (290,-1),choices = string, style = wx.CB_DROPDOWN)  
        self.cb.Bind(wx.EVT_COMBOBOX,self.show)
        self.stt2 = wx.StaticText(panel,-1,"Your username will appear here")
        
        st1 = wx.StaticText(panel,-1,"Enter the previous password : :")
        self.sb1 = wx.TextCtrl(panel,-1)
        hsizer1.Add(st1,1,wx.RIGHT,10)
        hsizer1.Add(self.sb1,2,0,0)

        st2 = wx.StaticText(panel,-1,"Enter the new password :")
        self.sb2 = wx.TextCtrl(panel,-1)
        hsizer2.Add(st2,1,wx.RIGHT,15)
        hsizer2.Add(self.sb2,2,0,0)

        st3 = wx.StaticText(panel,-1,"Re-enter the new password :")
        self.sb3 = wx.TextCtrl(panel,-1)
        hsizer3.Add(st3,1,wx.RIGHT,70)
        hsizer3.Add(self.sb3,2,0,0)
        
        self.b2= wx.Button(panel,1,"Update password")
        self.b3 = wx.Button(panel,1,"Exit")
        hsizer4.Add(self.b2,1,wx.ALIGN_CENTER_HORIZONTAL,0)
        hsizer4.Add(self.b3,1,wx.ALIGN_CENTER_HORIZONTAL,0)
        
        self.b2.Bind(wx.EVT_BUTTON,self.update)
        self.b3.Bind(wx.EVT_BUTTON,self.quit)
        
        vsizer1.Add(self.cb,0,wx.DOWN|wx.ALIGN_CENTER_HORIZONTAL,5)
        vsizer1.Add(self.stt2,0,wx.DOWN|wx.ALIGN_CENTER_HORIZONTAL,15)
        vsizer1.Add(hsizer1,0,wx.DOWN,15)
        vsizer1.Add(hsizer2,0,wx.DOWN,15)
        vsizer1.Add(hsizer3,0,wx.DOWN,15)
        vsizer1.Add(hsizer4,0,wx.ALIGN_CENTER_HORIZONTAL,0)
        
        self.user = user
        self.identity = identity
        
        panel.SetSizer(vsizer1)
        self.Centre()
        self.Show()
        
    def show(self,e):
        s = (self.cb.GetValue())
        x = filehandlingmod.filehandling()
        t = x.show_saved_password(s,self.user)
        font = wx.Font(15,wx.ROMAN,wx.NORMAL,weight = wx.BOLD)
        self.stt2.SetLabel(str(t[0][0]))
        self.stt2.SetFont(font)
        
    def update(self,e):
        s = (self.cb.GetValue())
        if self.sb3.GetValue()==self.sb2.GetValue():
            x = filehandlingmod.filehandling()
            temp = x.show_saved_password(s,self.user)
            if len(temp)>=1:
                x.save_editted_password(self.user,s,str(temp[0][1]),str(self.sb3.GetValue()))
                self.Close()
        else:
            dlg = wx.MessageDialog(self, "The new password you want to update is not same in above two places\nPlease rectify", 'Error', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()        
    def quit(self,e):
            self.Close()

##########################################################################################################################################################################

class npass(wx.Frame):
    def __init__(self,parent,title,user,identity):
        wx.Frame.__init__(self,parent,title = title)
        panel = wx.Panel(self,-1)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer4 = wx.BoxSizer(wx.HORIZONTAL)
        
        st = wx.StaticText(panel,-1,"Enter the details properly to save into our database")

        st1 = wx.StaticText(panel,-1,"Enter the Alias you want to save as :")
        self.sb1 = wx.TextCtrl(panel,-1)
        hsizer1.Add(st1,1,wx.RIGHT,10)
        hsizer1.Add(self.sb1,2,0,0)

        st2 = wx.StaticText(panel,-1,"Enter the Username :")
        self.sb2 = wx.TextCtrl(panel,-1)
        hsizer2.Add(st2,1,wx.RIGHT,15)
        hsizer2.Add(self.sb2,2,0,0)

        st3 = wx.StaticText(panel,-1,"Enter the password :")
        self.sb3 = wx.TextCtrl(panel,-1)
        hsizer3.Add(st3,1,wx.RIGHT,70)
        hsizer3.Add(self.sb3,2,0,0)
        
        self.b1 = wx.Button(panel,1,"Save Data")        
        self.b2 = wx.Button(panel,1,"Exit without saving")
        hsizer4.Add(self.b1,1,wx.RIGHT,10)
        hsizer4.Add(self.b2,1,wx.LEFT,10)
        
        self.b1.Bind(wx.EVT_BUTTON,self.save)
        self.b2.Bind(wx.EVT_BUTTON,self.quit)
        
        vsizer1.Add(st,0,wx.DOWN,50)
        vsizer1.Add(hsizer1,0,wx.DOWN,15)
        vsizer1.Add(hsizer2,0,wx.DOWN,15)
        vsizer1.Add(hsizer3,0,wx.DOWN,15)
        vsizer1.Add(hsizer4,0,wx.LEFT|wx.RIGHT,50)
        
        self.user = user
        self.identity = identity
        
        panel.SetSizer(vsizer1)
        self.Centre()
        self.Show()

    def save(self,e):
        x = filehandlingmod.filehandling()
        y = filters()
        if (y.save_new_password_filter(self,self.sb1.GetValue())):
            x.save_new_password(self.user,self.sb1.GetValue(),self.sb2.GetValue(),self.sb3.GetValue())
            self.Close()
                
    def quit(self,e):
            self.Close()

##########################################################################################################################################################################

class rpass(wx.Frame):

    def __init__(self,parent,title,user,identity):
        wx.Frame.__init__(self,parent,title = title)
        panel = wx.Panel(self,-1)

        self.user = user
        self.identity = identity

        x=filehandlingmod.filehandling()
        string = x.dropdown_options_in_rpass(self.user)

        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        
        self.cb = wx.ComboBox(panel,-1,'Select the alias with which you saved your data',size = (290,-1),choices = string, style = wx.CB_DROPDOWN)  

        self.st1 = wx.StaticText(panel,-1,"Here is your username",style = wx.ALIGN_CENTER)
        self.st2 = wx.StaticText(panel,-1,"Here is your password",style = wx.ALIGN_CENTRE)

        self.b1 = wx.Button(panel,-1,"Show")
        self.b1.Bind(wx.EVT_BUTTON,self.select)
        self.b2 = wx.Button(panel,-1,"Previous Window")
        self.b2.Bind(wx.EVT_BUTTON,self.close)

        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(self.b1,1,wx.LEFT|wx.RIGHT,10)
        hsizer.Add(self.b2,1,wx.LEFT|wx.RIGHT,10)
                              
        self.vsizer.Add(self.cb,0,wx.DOWN|wx.UP|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL,15,25)
        self.vsizer.Add(self.st1,0,wx.UP|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL,25)
        self.vsizer.Add(self.st2,0,wx.UP|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL,25)
        self.vsizer.Add(hsizer,0,wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.UP,40)
        self.vsizer.Fit(panel)
        panel.SetSizer(self.vsizer)
        self.Centre()
        self.Show()

    def select(self,e):
        s = (self.cb.GetValue())
        font = wx.Font(15,wx.ROMAN,wx.NORMAL,weight = wx.BOLD)
        x = filehandlingmod.filehandling()
        temp = x.show_saved_password(s,self.user)
        self.st1.SetLabel(str(temp[0][0]))
        self.st1.SetFont(font)
        self.st2.SetLabel(str(temp[0][1]))
        self.st2.SetFont(font)
        self.vsizer.Layout()
        self.vsizer.Fit()        
        
    def close(self,e):
            self.Close()

##########################################################################################################################################################################
##########################################################################################################################################################################

app = wx.App()
aa = authentication(None,"Remeber your passwords with ease",True)
app.MainLoop()

