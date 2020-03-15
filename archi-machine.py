import argparse
import json

'''
To do:
--add collaboration
'''
#parser code
parser=argparse.ArgumentParser()
parser.add_argument('-block',dest='name',default='none')
parser.add_argument('-width',dest='width',default=20)
parser.add_argument('-height',dest='height',default=20)
parser.add_argument('-value',dest='value',default='def')
parser.add_argument('-disp',dest='disp',action='store_true',default=False)
parser.add_argument('-exit',dest='exit',action='store_true',default=False)
parser.add_argument('-print',dest='printit',action='store_true',default=False)




#canvas for rendering
class canvas():
    def __init__(self):
        self.width=50
        self.height=30
        self.blocks=dict()
        self.canvas=[[]]
        self.draw_offset_y=2
        self.draw_offset_x=2
        
        self.generate_canvas()
        
    def add_block(self,key,value):
        self.blocks[key]=value
        self.blocks[key].key=key
        self.key_words=key.split()
    
    def generate_canvas(self):
        
        for m in range(0,self.height):
            self.canvas.append([])
            for n in range(0,self.width):
                self.canvas[m].append(' ')
        self.canvas.pop()
            
            
    def draw_block(self,key):
        
        starttext=self.draw_offset_y + (self.blocks[key].height/2)
        n=0
        
        for m in key:
            self.canvas[int(starttext)][n+self.draw_offset_x + int(self.blocks[key].width/2)-len(key)]=m
            n+=1
        
        for m in range(0,self.blocks[key].width):
            self.canvas[self.draw_offset_y][m+self.draw_offset_x]=self.blocks[key].border_top
            self.canvas[self.draw_offset_y+self.blocks[key].height-1][m+self.draw_offset_x]=self.blocks[key].border_top
            
        for m in range(0,self.blocks[key].height):
            self.canvas[m+self.draw_offset_y][self.draw_offset_x]=self.blocks[key].border_side
            self.canvas[m+self.draw_offset_y][self.draw_offset_x+self.blocks[key].width-1]=self.blocks[key].border_side        
        
        
            
            
class printer:
    def __init__(self):
        self.left_padding=20
        self.bottom_padding=20
        
    def printit(self,arg):
        for m in arg:
            print()
            self.print_pad()
            for n in m:
                print(n,end="")
        
        print()
        self.print_pad()
        for m in range(0,50):
            print('=',end="")
    
    def print_pad(self):
        for m in range(0,self.left_padding):
            print(' ',end="")
                       
#-====================================================
            
        


class   block():
    def __init__(self):
        self.offset_x=0
        self.offset_y=0
        self.width=10
        self.height=10
        self.border_top='-'
        self.border_side='|'
        self.value=''
        self.key=''
 
 
        








class Main_worker:
    def __init__(self):
        self.printer=printer()
        self.canvas=canvas()
        self.height=20
        self.width=20
        self.default_offset_x=2
        self.default_offset_y=2
        self.val_height_prev=0
    def add_block(self,key,width,height):
        self.canvas.add_block(key,block())
        self.canvas.blocks[key].width=int(width)
        self.canvas.blocks[key].height=int(height)        
        self.canvas.draw_block(key)
    def display(self):
        self.printer.printit(self.canvas.canvas)
        print()
    def resolve(self,val):
        
        print("resolving")
        if val.name!='none':
            if int(val.width)>(self.canvas.width-self.default_offset_x):
                print("Width is too much")
                return
                
            if (self.canvas.draw_offset_x+int(val.width))>self.canvas.width:
                print("condition found true")
                self.canvas.draw_offset_x=self.default_offset_x
                self.canvas.draw_offset_y=self.val_height_prev+self.default_offset_y    #+self.canvas.draw_offset_y
            
            
            
            self.add_block(val.name,val.width,val.height)
            print("ok here")
            self.canvas.draw_offset_x=self.canvas.draw_offset_x+self.canvas.blocks[val.name].width+self.default_offset_x
            print("ok here")
            
            if int(val.height)>self.val_height_prev:
                self.val_height_prev=val.height
            
            
        print("truth checking")
        if val.disp==True:
            self.display()
            
            
        if val.printit==True:
            f=open('result.txt','w')
            for m in self.canvas.canvas:
                    str1=" "
                    print(m)
                    out=str1.join(m)
                    print(out)
                    f.write(out)
            print(f)
            
            f.close()


worker=Main_worker()

print(''' 
            Architecture designer v1.0.0
      
         Something something all rights blah blah ...
      ===============================================
      
      To start off enter block name in the terminal
      like this :
      -block BLOCK_NAME
            
      If you want to add parameters like block width use :
           -block BLOCK_NAME  -width=20 -height=20 -value="cpu core"
      
      To display the chart type in:
           -disp
           
      To print to a file type in:(this has bugs)
          -print
          
      To exit the console type :
          -exit 
          
          
    
          ''')

exit=False
while   exit==False:
    p=input(">>")
    #try:
    m=parser.parse_args(p.split())
    print("Waiting for task to complete")
    if m.exit==True:
        exit=True        
    worker.resolve(m)
        
    #except:
        #print("Enter the right keywords")
    
    
    
