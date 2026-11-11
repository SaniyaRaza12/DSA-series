class node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next 
class DLL:
    def __init__(self,start):
        self.start=start
    def is_empty(self):
        return self.start==None  
    def search(self,data):
        if self.start.item==data:
            return self.start
        else:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    return temp
                    break
                temp=temp.next
    def insert_at_first(self,data):
        new=node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=new
        self.start=new
    def insert_at_last(self,data):
         new=node(None,data,None)
         if self.is_empty():
              self.start=new
         if self.start.next==None: 
              new.prev=self.start
              self.start.next=new                
         else:
              temp=self.start
              while temp.next is not None:
                   temp=temp.next    
              new.prev=temp
              temp.next=new  
    def insert_at_after(self,data,temp):
          new=node(temp,data,temp.next)
          if temp.next is not None:
              temp.next.prev=new
          temp.next=new
    def delete_at_first(self):
              if not self.is_empty():
                   self.start.next.prev=None
                   self.start=self.start.next
    def delete_at_last(self):
         if self.is_empty():
              pass
         if self.start.next==None:
              self.start=None
         else:
              temp=self.start
              while temp.next is not None:
                   temp=temp.next
              temp.prev.next=temp.next
    def delete_item(self,data):
         if self.is_empty():
              pass
         if self.start.next is None:
              if self.start.item==data:
                   self.start=self.start.next
         else:
              temp=self.start
              while temp.next is not None:
                   if temp.item==data:
                        if temp.next is not None:
                           temp.next.prev=temp.prev          
                        temp.prev.next=temp.next
                   temp=temp.next
    def print(self):
     temp=self.start
     while temp is not None:
          print(temp.item,end=" ")         
          temp=temp.next
          
    def __iter__(self):
          return DLLIterator(self.start)
class DLLIterator:
          def  __init__(self,start):
              self.current=start
          def __iter__(self):
             return self
          def __next__(self):
             if not self.current:
               raise StopIteration
             data=self.current.item
             self.current=self.current.next
             return data

n=DLL(None)
n.insert_at_first(200)
n.insert_at_last(100)
n.insert_at_after(400,n.search(100))
n.insert_at_after(300,n.search(200))
n.insert_at_first(800)
n.insert_at_last(50)
n.delete_at_first()
n.delete_at_last()
n.delete_item(100)
n.search(200)
for x in n:
     print(x,end=" ")
print()     
n.print()