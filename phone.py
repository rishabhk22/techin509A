
# TODO

#1. Create 2 instances of the iPhone.

#2. Change iPhone names through set_name()

#3. Send a iMessage from phone1 to phone2

#4. phone2 should be able to check messages. Print the messages on screen.

class iphone:
    def __init__(self, name, colour, version, model, number ): #constructor
        self.name = name
        self.colour = colour
        self.model = model
        self.number = number
        self.version = version
        self.files = []
        self.message = []
    
    def check_message(self):
        pass
          
    def drop(self,filename, recipient):
        print("Dropping %s" % filename)
        #self.recipient = recieve.name
        pass

    def recieve(self, name):
        self.name = name
        pass

    def call(self,number):
        pass

    def set_name(self, new_name): # function to change the name
        if len(new_name)< 3:
            print("Name must be longer than 3 characters")
        self.name = new_name
    
    def send_msg(self, recipent, message):  #send message and give confirmation on screen
        recipent.receive_msg(f"New message from {self.name}: {message}")
        print(f"**Message sent to {recipent.name}**")
    
    def receive_msg(self, message): #message receiving function
        self.message.append(message)
        #print(message)
    
    def check_msg(self): # notification to check message
        print(f"--{self.name}, you have a new message!--")
    
    def display_msg(self): # display the message
        for message in self.message:
            print(message)

ians_iphone = iphone(name= "Ian's iPhone", colour = "red", version = "18", model = "16 Pro", number = "298719")
print(ians_iphone.name)
#print(ians_iphone.colour)
#print(ians_iphone.version)
#print(ians_iphone.model)
#print(ians_iphone.number) 
#ians_iphone.drop("notes.pdf", "")

rishis_iphone = iphone(name = "Rishi's iPhone" , colour = "black", version = "18.1", model = "16 Pro Max", number = "80901097")
print(rishis_iphone.name)

rishis_iphone.set_name("Rishi's New iPhone") # chaning the name of the device by calling set_name function
ians_iphone.set_name("Ian's New iPhone")

print("New names")
print(ians_iphone.name)
print(rishis_iphone.name)

ians_iphone.send_msg(rishis_iphone, "Hi there!") # message sending
rishis_iphone.check_msg() # checking the message received
rishis_iphone.display_msg()


  
      




