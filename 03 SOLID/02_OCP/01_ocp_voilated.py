class Notifications:
    def send_notification(self, notofication_type):
        if notofication_type == "Email":
            print("Sending Email")
        elif notofication_type == "SMS":
            print("Sending SMS")
        elif notofication_type == "Phone":
            print("Calling")
            
notify = Notifications()
notify.send_notification("Email")
notify.send_notification("SMS")
notify.send_notification("Phone")
            
# OCP says code should be open for extension but closed for modofication
# Here every time a new notofication is introducted we have to modify our existing code
# Also these don't seems to be a way for extension