# simpleComms
python/apache2 comms system


## Useage:

To use simply:
```python
from comms import Comms

toJames = Comms("James' IP")

toJames.send("Hello")

toJames.get() # gets last message from James
```
