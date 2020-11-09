import requests, time

class Comms:
  def __init__(self, ip):
    self.url = "http://" + ip + "/out.txt"
    self.lastMessage = ""
    self.get()
    
  def get(self):  
    current = requests.get(self.url).text
    if(current != self.lastMessage):
      self.lastMessage = current
      return current
    return ""

  def send(self, message):
    with open("/var/www/html/out.txt", "w") as f:
      f.write(message)
      f.close()

  def waitForMessage(self, handler):
    newMessage = False
    past = self.get()
    while not newMessage:
      current = self.get()
      if(current != past):
        newMessage = True
    handler(current)