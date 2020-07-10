# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:27:22 2020

@author: nikita.agarwal
"""


class telescope:
    
    def __init__(self,id,name,lat,long):
        self.id=id
        self.name=n
        self.lat=lat
        self.long=long
        
    def getid(self):
        return self.id
    def getname(self):
        return self.name
    def getlat(self):
        return self.lat
    def getlong(self):
        return self.long
    
class members:
    def __init__(self,memid,name,username,email):
        self.memid=memid
        self.memname=mname
        self.username=uname
        self.email=email
        
    def getmemid(self):
        return self.memid
    def getmemname(self):
        return self.memname
    def getusername(self):
        return self.username
    def getemail(self):
        return self.email
    
class sources:
    def __init__(self,jname,stype,ra,dec):
        self.jname=jname
        self.stype=stype
        self.ra=ra
        self.dec=dec
        
    def getjname(self):
        return self.jname
    def getstype(self):
        return self.stype
    def getra(self):
        return self.ra
    def getdec(self):
        return self.dec    