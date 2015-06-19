###set font of display of password and website link

###create buttons for direct copy and paste of credentials

import wx
class main(wx.Frame):

    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title = title,size= (350,100))
        panel = wx.Panel(self,-1)

        sizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.b1 = wx.Button(panel,1,"Save password")
        self.b2 = wx.Button(panel,1,"Retrieve password")
        self.b3 = wx.Button(panel,1,"Exit")

        sizer1.Add(self.b1,1,wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND,wx.ALL)
        sizer1.Add(self.b2,1,wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND,wx.ALL)
        sizer1.Add(self.b3,1,wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND,wx.ALL)

        
        self.b1.Bind(wx.EVT_BUTTON,self.savenewpassword)        
        self.b2.Bind(wx.EVT_BUTTON,self.reviewpassword)
        self.b3.Bind(wx.EVT_BUTTON,self.quit)

        panel.SetSizer(sizer1)
        self.Centre()
        self.Show()

    def savenewpassword(self,e):
        a = npass(None,"Save your password")
        
    def reviewpassword(self,e):
        a = rpass(None,"Review your saved passwords")
        
    def quit(self,e):
        self.Close()

class authentication(wx.Frame):
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

        st2 = wx.StaticText(panel,-1,"Enter the phone number \n(with which u registered the account) :")
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
        
        vsizer.Add(hsizer1,2,wx.ALIGN_CENTER_HORIZONTAL,0)
        vsizer.Add(hsizer2,2,wx.ALIGN_CENTER_HORIZONTAL,0)
        vsizer.Add(hsizer_b,2,wx.ALIGN_CENTER_HORIZONTAL|wx.UP,10)

        self.current_user = 0
        panel.SetSizer(vsizer)
        self.Centre()
        self.Show()
        
    def login(self,e):
        self.userinfo()
        i = self.user_match()
        if i == 1:
            t = main(None,"Welcome " + self.username_list[self.current_user])
            self.quit(e)
        else:
            self.st1 = wx.StaticText(self,-1,"Either of your credentials are wrong\n Kindly make changes and retry with login",(80,115),style = wx.ALIGN_CENTRE)
            
    def userinfo(self):
        f = open('C:\Users\DJ\Documents\pss.txt','r')
        self.username_list,self.usernumber_list = [],[]
        for l in f:
            temp = str.split(str(l),'\t')
            if temp[0] == 'Username':
                self.username_list.append(str(temp[1]))
                self.usernumber_list.append(str(temp[2]))
                
    
    def user_match(self):
        temp1 = str(self.sb1.GetValue())
        temp2 = str(self.sb2.GetValue())
        i = 0
        while i<len(self.username_list):
            if temp1 == str(self.username_list[i]) and temp2 == str(self.usernumber_list[i]):
                self.current_user = i
                return 1;
            i+=1
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
        f = open('C:\Users\DJ\Documents\pss.txt','a')
        f.write("Username")
        f.write('\t')
        f.write(str(self.sb1.GetValue()))
        f.write('\t')
        f.write(str(self.sb2.GetValue()))
        f.write('\t')
        f.write('\n')
        f.close()
        self.Close()
             
    def quit(self,e):
        self.Close()

##########################################################################################################################################################################

class npass(wx.Frame):
    def __init__(self,parent,title):
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
        
        panel.SetSizer(vsizer1)
        self.Centre()
        self.Show()

    def save(self,e):
        f = open('C:\Users\DJ\Documents\pss.txt','a')
        f.write(str(self.sb1.GetValue()))
        f.write('\t')
        f.write(str(self.sb2.GetValue()))
        f.write('\t')
        f.write(str(self.sb3.GetValue()))
        f.write('\n')
        f.close()
        self.Close()
                
        
    def quit(self,e):
            self.Close()

##########################################################################################################################################################################

class rpass(wx.Frame):

    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title = title)
        panel = wx.Panel(self,-1)
        f = open('C:\Users\DJ\Documents\pss.txt','r')
        string = []
        for l in f:
            temp = str.split(str(l),'\t')
            if str(temp[0]) != 'Username':
                string.append(temp[0])
        f.close()

        vsizer = wx.BoxSizer(wx.VERTICAL)
        
        self.cb = wx.ComboBox(panel,-1,'Select the alias with which you saved your data',size = (290,-1),choices = string, style = wx.CB_DROPDOWN)  

        self.st1 = wx.StaticText(panel,-1,"Here is your website",style = wx.ALIGN_CENTRE)
        self.st2 = wx.StaticText(panel,-1,"Here is your Password",style = wx.ALIGN_CENTRE)

        self.b1 = wx.Button(panel,-1,"Show")
        self.b1.Bind(wx.EVT_BUTTON,self.select)
        self.b2 = wx.Button(panel,-1,"Previous Window")
        self.b2.Bind(wx.EVT_BUTTON,self.close)

        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(self.b1,1,wx.LEFT|wx.RIGHT,10)
        hsizer.Add(self.b2,1,wx.LEFT|wx.RIGHT,10)
                              
        vsizer.Add(self.cb,0,wx.DOWN,15)
        vsizer.Add(self.st1,0,wx.UP|wx.ALIGN_CENTER_HORIZONTAL,25)
        vsizer.Add(self.st2,0,wx.UP|wx.ALIGN_CENTER_HORIZONTAL,25)
        vsizer.Add(hsizer,0,wx.ALIGN_CENTER_HORIZONTAL|wx.UP,40)

        panel.SetSizer(vsizer)
        self.Centre()
        self.Show()

    def select(self,e):
        s = (self.cb.GetValue())
        f = open('C:\Users\DJ\Documents\pss.txt','r')
        font = wx.Font(15,wx.ROMAN,wx.NORMAL,weight = wx.BOLD)
        for l in f:
            temp = str.split(str(l),'\t')
            if temp[0] == s:
                self.st1.SetLabel(str(temp[1]))
                self.st1.SetFont(font)
                self.st2.SetLabel(str(temp[2]))
                self.st2.SetFont(font)
                f.close()
                return;
        f.close()
    def close(self,e):
            self.Close()

##########################################################################################################################################################################
app = wx.App()
aa = authentication(None,"Remeber your passwords with ease")
app.MainLoop()
