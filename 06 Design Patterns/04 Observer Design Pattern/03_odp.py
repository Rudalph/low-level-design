from abc import ABC, abstractmethod

class YTChannel(ABC):
    def __init__(self):
        self.all_subscribers = []
        self.latest_video = None
    
    @abstractmethod
    def add_subscribers(self, subscriber):
        pass
    
    @abstractmethod
    def remove_subscriber(self, subscriber):
        pass
    
    @abstractmethod
    def upload_video(self, video):
        pass
    
    @abstractmethod
    def get_content(self):
        pass
    
    @abstractmethod
    def notify(self):
        pass
    
class CodingChannels(YTChannel):
    def add_subscribers(self, subscriber):
        self.all_subscribers.append(subscriber)
    
    def remove_subscriber(self, subscriber):
        if subscriber in self.all_subscribers:
            self.all_subscribers.remove(subscriber)
    
    def upload_video(self, video):
        self.latest_video = video
        self.notify()
        
    def get_content(self):
        return self.latest_video
    
    def notify(self):
        for subscriber in self.all_subscribers:
            subscriber.update()


class Subscriber(ABC):
    def __init__(self, name, channel):
        self.subscriber_name = name
        self.channel = channel
    
    @abstractmethod
    def get_details(self):
        pass
    
    @abstractmethod
    def update(self):
        pass

class CodingChannelSubscribers(Subscriber):
    def get_details(self):
        return self.subscriber_name
    
    def update(self):
        print(self.channel.get_content())
        

coding_channel = CodingChannels()

sub1 = CodingChannelSubscribers('Sub1', coding_channel)
sub2 = CodingChannelSubscribers('Sub2', coding_channel)

coding_channel.add_subscribers(sub1)
coding_channel.add_subscribers(sub2)

coding_channel.upload_video('Programming')
# coding_channel.notify() # Notify can work automatically as well as by calling in this way as well

'''
subscriber's update() could receive the video directly.

Currently:
def update(self):
    print(self.channel.get_content())
    
another approach
def update(self, video):
    print(video)
    
And notify:
def notify(self):
    for subscriber in self.all_subscribers:
        subscriber.update(self.latest_video)
        
Both approaches are valid. The second approach is called push notification because the Subject pushes the new video to its observers.
Your existing approach is pull notification because the observers fetch the latest video from the Subject.
'''
