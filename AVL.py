
class Node:
    def __init__(self, V):
        self.key=V
        self.leftChild=None
        self.rightChild=None
        self.parent=None
        self.balance=0
        
class AVLTree:
    def __init__(self, zahl):
        self.root=Node(zahl)
        
    def rotateright(self,x):
            y=x.leftChild
            if x.parent==None:
                self.root=y
            elif x.parent.leftChild==x:
                x.parent.leftChild=y
            else:
                x.parent.rightChild=y
            y.parent=x.parent
            x.leftChild=y.rightChild
            if x.leftChild!=None:
                x.leftChild.parent=x
            y.rightChild=x
            x.parent=y
            #x.balance=
    def rotateleft(self,x):
            y=x.rightChild
            #print(y.key)
            if x.parent==None:
                
                self.root=y
            elif x.parent.leftChild==x:
                x.parent.leftChild=y
            else:
                #print("Si")
                x.parent.rightChild=y
            y.parent=x.parent
            x.rightChild=y.leftChild
            if x.rightChild!=None:
                x.rightChild.parent=x
            y.leftChild=x
            x.parent=y
       
    def insert(self, key):
        new=Node(key)
        x=self.root
        #print(x, "root")
        y=None
        critical=False
        while x!=None:
            y=x #copy
            if new.key< x.key:
                x.balance+= -1
                
                if x.balance== -2:
                    
                    critical=x
                    #print(critical.key)
                    
                x=x.leftChild  
            else:
                
                x.balance+= 1
                if x.balance==2:
                    critical=x
                    
                x=x.rightChild
                
                
        new.parent=y
        #print(new.parent)
        if y==None:
            self.root=Node(key)
        elif new.key<y.key:
            y.leftChild=new
        else:
            y.rightChild=new
            
        #self.root=y
        #hasta aqui todo bien
    
        #reparatur
        
        if critical!= False:
            #print(critical.key)
            if critical.parent!=None:
                        critical.parent.balance+= -1
                        
            if critical.balance==-2:
                
                if critical.leftChild.balance==0: #or critical.leftChild.balance==-1:
                    
                    #critical.balance=-1
                    #critical.leftChild.balance=1
                    #rotateright(critical)
                    critical.balance+= 1
                elif critical.leftChild.balance==-1:
                    
                    critical.balance=0
                    critical.leftChild.balance=0
                    rotateright(critical)
                elif critical.leftChild.balance==1:
                    #falta cambio de balance!!!!
                    #rotateLr(critical)
                    if critical.leftChild.rightChild.balance==-1:
                        critical.balance=1
                        critical.leftChild.balance=0
                        critical.leftChild.rightChild.balance=0
                        
                    else:
                        critical.balance=0
                        critical.leftChild.rightChild.balance=0
                        if critical.leftChild.rightChild.balance==0:
                            critical.leftChild.balance=0
                        elif critical.leftChild.rightChild.balance==1:
                            
                            critical.leftChild.balance=-1
                        
                    
                    self.rotateleft(critical.leftChild)
                    self.rotateright(critical)
                    
                    
            elif critical.balance==2:
                
                if critical.rightChild.balance==0:
                    
                    #critical.balance=1
                    #critical.rightChild.balance=-1
                    #self.rotateleft(critical)
                    critical.balance+= -1
                elif critical.rightChild.balance==1:
                    
                    critical.balance=0
                    critical.rightChild.balance=0
                    
                        
                    #print(critical.rightChild.key)
                    self.rotateleft(critical)
                    
                elif critical.rightChild.balance==-1:
                    
                    if critical.rightChild.leftChild.balance==1:
                        critical.balance=-1
                        critical.rightChild.balance=0
                        critical.rightChild.leftChild.balance=0
                    else:
                        critical.balance=0
                        critical.rightChild.leftChild.balance=0
                        if critical.rightChild.leftChild.balance==0:
                            critical.rightChild.balance=0
                        elif critical.rightChild.leftChild.balance==-1:
                            
                            critical.rightChild.balance=1


                    
                    self.rotateright(critical.rightChild)
                    self.rotateleft(critical)
                
        #Rrechtsrotation
      
              

avl=AVLTree(2)
avl.insert(0)
avl.insert(8)
avl.insert(6)
avl.insert(9)
avl.insert(5)
#avl.insert(8)

#avl.insert(1)
#avl.__dict__["root"]
#avl.__dict__["root"].__dict__["rightChild"].__dict__
#avl.__dict__["root"].__dict__["leftChild"].__dict__
#avl.__dict__["root"].__dict__["rightChild"].__dict__["rightChild"].__dict__
