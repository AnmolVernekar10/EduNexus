import PyPDF2
from django.db import models
import os
from home.keywords import extract_text
#from keywords import extract
# Create your models here.
class Files(models.Model):
    file=models.FileField(default="")

    def filename(self):

        return os.path.basename(self.file.name)
    
    def tes(self):
        return os.path.getsize()
    
    def extract_keyword(self):
        z = extract_text(f"media/{self.file.name}")
        l1=[]
        try:
            if(len(z)<5):
                for j in z:
                    for i in j:
                        if(len(l1)<=20):
                            l1.append(i[1])
                        else:
                            break   
            else:
                for j in z:
                    for i in j:
                        if(len(l1)<=10):
                            l1.append(i[1])
                        else:
                            break            
            s=str(l1)
        except:
            s="['No Keywords Found']"
        return s
    
    def __str__(self) -> str:
        return self.file.name
class file_name_against_keyword(models.Model):
    filename=models.CharField(max_length=1024)
    keyword=models.CharField(max_length=1024)
    
    def __str__(self) -> str:
        return self.filename

class keyword_against_file_name(models.Model):
    filename=models.CharField(max_length=1024)
    keyword=models.CharField(max_length=2024)

    def __str__(self) -> str:
        return self.keyword
# class (models.Model):    
