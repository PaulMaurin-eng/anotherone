

class Book_Initiation:
    def __init__(self):
        self.book = []
        self.user = []
        
        
    
    def regi_book(self, title, author, copies):
        self.book.append({"Title" :title, "Author" : author, "Copies" : copies} )
 

    def regi_user(self, name, id_num, email):
        self.user.append({"Name" : name, "id_num" : id_num, "email" : email} ) 
        
        
    def find_user(self, id_num):
        return next((u for u in self.user if u["id_num"] == id_num), None)

    def find_book(self, title):
        return next((b for b in self.book if b["Title"].lower() == title.lower()), None)

        
    
        
        
class Table_print:
    def __init__(self,library:  Book_Initiation):
        self.library = library
    
    def table(self):
        
        print("Available books:")
        print("--------------------------------------------------------------------------------")
        for i in self.library.book:
            print(f'Title: {i["Title"]} | Author: {i["Author"]} | Copies avail: {i["Copies"]}')
            print("--------------------------------------------------------------------------------")
         
       

class Response:
    def __init__(self, library : Book_Initiation):
        self.library = library
        
    def res(self, user_id, title):
        user = self.library.find_user(user_id)
        
        if not user:
            print("User not found")
            return
         
            
         
        book = self.library.find_book(title)    
        if not book:
            print("Can't find book")
            return
            
        
        if book["Copies"] <= 0 :
            print("Not available at the moment")
            
       
            
        book["Copies"] -= 1
        print(f'{user["name"]} borrowed "{book["title"]}". Copies left: {book["copies"]}')
            
            
            
            
            
            
            
        
        
        
k = Book_Initiation()        
    
k.regi_book("petit Prince", "l aviateur", 3)    
k.regi_book("l'ombre", "xavier", 4)
k.regi_book("la relique", "xavier", 2)       
k.regi_user("jean", 345, "jean@email")
k.regi_user("mark", 254, "mark@email")

Table_print(k).table()
        
        
c = Response()

c.res(345,"la relique")


        