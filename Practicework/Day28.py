'''
#Encapsulation
#Public Attributes
class user:
    def __init__(self,username):
        self.username=username
user1=user("Eswar")
print(user1.username)
user1.username="RAM"
print(user1.username)

#Protected Attribute
class user:
    def __init__(self,username,otp):
        self.username=username
        self.otp=otp
user1=user("Eswar","143143")
print(user1.otp)
user1.otp="141141"
print(user1.otp)

#Using Protected Attributes in a Subclass
class user:
    def __init__(self,username,otp):
        self.username=username
        self.otp=otp
class Admin(user):
    def show_otp(self):
        return f"Adimin can see OTP: {self.otp}"
adimin1=Admin("Eswar","777777")
print(adimin1.show_otp())
user1=user("Eswar","143143")
print(user1.otp)
user1.otp="141141"
print(user1.otp)

#Private Attributes in Python
class user:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        
user1=user("Eswar","Eswar@143")
print(user1.username)
print(user1.password)

#example:
class user:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        
    def get_password(self):
        return "******"
    def set_password(self,new_password):
        if len(new_password)<6:
            print("Error: Password must be at least 6 characters long.")
        else:
            self.password = new_password
            print("Password updated successfully.")
user1=user("Eswar","Eswar@143")
print(user1.get_password)
user1.set_password("123")
print(user1.set_password)
user1.set_password("Eswar@143")
print(user1.set_password)

#7. Complete Encapsulation Example (Public, Protected,and Private Attributes)
class user:
    def __init__(self,username,password,otp):
        self.username=username
        self.password=password
        self.otp=otp
        
    def get_password(self):
        return "******"
    def set_password(self,new_password):
        if len(new_password)<6:
            print("Error: password must be at least 6 charcharacters long.")
        else:
            self.password=new_password
            print("password update successfully.")
    def get_otp(self):
        return self.otp
    
    def set_otp(self, new_otp):
        self.otp = new_otp
        print("OTP updated successfully.")

user1=user("Eswar","Eswar@143","143143")
print(user1.username)
user1.username="Ram"
print(user1.username)
print(user1.get_otp())
user1.set_otp("141141")
print(user1.get_otp())
print(user1.get_password())
user1.set_password("Ram@4004")
print(user1.get_password())

#Inheritance
#Instagram-Based Analogy
#step1.Define a General Class

class user:
    def __init__(self,username,email):
        self.username=username
        self.email=email
        
    def post_photo(self):
        print(f"{self.username} posted a photo")
        
    def follow(self,other_user):
        print(f"{self.username} followed {other_user.username}")
#Types of Inheritance (with Instagram Examples)
#1.Single Inheritance
class verifieduser(user):
    def __init__(self,username,email,badge_color):
        super().__init__(username,email)
        self.badge_color=badge_color
    def go_live(self):
        print(f"{self.username} is going live")
        
v = verifieduser("Eswar", "eswar@email.com", "Blue")
v.post_photo()
v.go_live()

#2. Multilevel Inheritance
class influencer(verifieduser):
    def __init__(self,username,email,badge_color,niche):
        super().__init__(username,email,badge_color)
        self.niche=niche
    def promote_brand(self,brand):
        print(f"{self.username} is promoting {brand}")
        
i = influencer("Anu", "anu@email.com", "Gold", "Travel")
i.promote_brand("Adidas")

#3. Hierarchical Inheritance
class businessuser(user):
    def __init__(self,username,email,business_name):
        super().__init__(username, email)
        self.business_name = business_name
    def view_insights(self):
        print(f"{self.username} is viewing business insights.")
class Creator(user):
    def __init__(self, username, email, content_type):
        super().__init__(username, email)
        self.content_type = content_type
    def monetize_content(self):
        print(f"{self.username} is monetizing {self.content_type} content.")
        
b = businessuser("ShopKing", "shop@email.com", "KingStore")
b.view_insights()

c = Creator("Ravi", "ravi@email.com", "Videos")
c.monetize_content()

#4. Multiple Inheritance
class Analytics:
    def track_engagement(self):
        print("Tracking engagement...")
class HybridUser(user, Analytics):
    def __init__(self, username, email):
        super().__init__(username, email)
    def hybrid_action(self):
        print(f"{self.username} uses hybrid features.")

h = HybridUser("Kiran", "kiran@email.com")
h.hybrid_action()
h.track_engagement()

#super() Keyword
#How super() Works in Different Inheritance Types
#1. Single Inheritance
class user:
    def __init__(self,username):
        self.username=username
        print(f"user instalized: {username}")
        
class verifieduser(user):
    def __init__(self,username,badge):
        super().__init__(username)
        self.badge=badge
        print(f"verified user instalized badge:{badge}")
a=verifieduser("Eswar","Blue") 

#2. Multilevel Inheritance
class user:
    def __init__(self,username,):
        self.username=username
class verifieduser(user):
    def __init__(self, username, badge):
        super().__init__(username)
        self.badge=badge
        print(f"VerifiedUser initialized:{badge}")
class influencer(verifieduser):
    def __init__(self,username,badge,niche):
        super().__init__(username,badge)
        self.niche=niche
        print(f"Influencer initialized:{niche}")
a=influencer("Eswar","Gold","Fashion")

#3. Multiple Inheritance with super() and MRO
class analytics:
    def __init__(self):
        super().__init__()
        print("Analytics initilized")
class moderator:
    def __init__(self):
        super().__init__()
        print("Moderator initilized")
class adminuser(analytics,moderator):
    def __init__(self):
        super().__init__()
        print("Adminuser initilized")
a=adminuser()        

#When to Use ClassName.method(self, ...)
class Moderator:
    def show_permissions(self):
        print("Moderator permissions")

class Admin:
    def show_permissions(self):
        print("Admin permissions")
class HybridUser(Moderator, Admin):
    def show_permissions(self):
        Moderator.show_permissions(self)
        Admin.show_permissions(self)
user1 = HybridUser()
user1.show_permissions()
'''


                
    




