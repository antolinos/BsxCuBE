"""
=============================================
  NAME       : Browse Control Object (Browse.py)
  
  DESCRIPTION:
    
  VERSION    : 1

  REVISION   : 0

  RELEASE    : 2010/MAR/19

  PLATFORM   : Bliss Framework 4

  EMAIL      : ricardo.fernandes@esrf.fr
  
  HISTORY    :
=============================================
"""




# =============================================
#  IMPORT MODULES
# =============================================
try:
    from Framework4.Control.Core.CObject import CObjectBase, Signal, Slot    
except ImportError:
    print "%s.py: error when importing module!" % __name__



# =============================================
#  CLASS DEFINITION
# =============================================
class Browse(CObjectBase):
    

    __CHANNEL_LIST = ["browseTypeChanged",
                     "browseLocationChanged"]
    

    # =============================================
    #  SIGNALS/SLOTS DEFINITION
    # =============================================
    signals = [Signal(channel) for channel in __CHANNEL_LIST]
    
    slots = []
    



    # =============================================
    #  CONSTRUCTOR
    # =============================================    
    def __init__(self, *args, **kwargs):
        CObjectBase.__init__(self, *args, **kwargs)
        
  

    def init(self):
        for channel in self.__CHANNEL_LIST:
            try:
                value = self.channels.get(channel[:-7])
                setattr(self, channel[:-7], value)
                if value is not None:
                    getattr(self, channel[:-7]).connect("update", getattr(self, channel))
            except:
                pass
                                           
    # =============================================
    #  COMMANDS
    # =============================================      


    # =============================================
    #  CHANNELS
    # =============================================
    def browseTypeChanged(self, pValue):
        print "emitting"
        self.emit("browseTypeChanged", pValue)
        print "ok"

    def browseLocationChanged(self, pValue):
        self.emit("browseLocationChanged", pValue)
        




