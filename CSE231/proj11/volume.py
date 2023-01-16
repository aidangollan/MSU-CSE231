"Initializes Volume object with attibutes to enable printing, checking for validity, getting specific data values, checking for equality, and addition/subtraction"

UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

class Volume(object):
    def __init__(self, magnitude=0, unit="ml"):
        "Initializes object, checks for correct format for both data types, if there is inconsistency returns invalid object"
        if (type(magnitude) == float or type(magnitude) == int) and (unit in UNITS) and (magnitude >= 0):
            self.magnitude = magnitude
            self.unit = unit
        elif type(magnitude) != float or type(magnitude) != int:
            if unit in UNITS:
                self.magnitude = 0
                self.unit = None
            else:
                self.magnitude = None
                self.unit = None
            
    def __str__(self):
        "Returns formatted version of object as a string, or error message if invalid format"
        if self.unit != None:
            return("{:.3f} {}".format(self.magnitude,self.unit))
        else:
            return("Not a Volume")
        
    def __repr__(self):
        "Returns alternatively formatted version of object as a string, or error message if invalid format"
        if self.unit != None:
            return("{:.6f} {}".format(self.magnitude,self.unit))
        else:
            return("Not a Volume")
        
    def is_valid(self):
        "Checks if object is in valid format, if so returns True, if not returns False"
        if self.unit != None:
            return(True)
        else:
            return(False)
    
    def get_units(self):
        "If object is in valid format returns units of object, otherwise returns None"
        if self.unit != None:
            return(self.unit)
        else:
            return(None)
    
    def get_magnitude(self):
        "If magnitude of object is in valid format returns magnitude of object, otherwise returns None"
        if self.magnitude != None:
            return(self.magnitude)
        else:
            return(None)
    
    def metric(self):
        "If object is in valid format converts to metric, otherwise returns invalid object"
        if self.unit == None or self.unit == "ml":
            return(Volume(self.magnitude, self.unit))
        else:
            return(Volume(self.magnitude * MLperOZ, "ml"))

    def customary(self):
        "If object is in valid format converts to US customary, otherwise returns invalid object"
        if self.unit == None or self.unit == "oz":
            return(Volume(self.magnitude, self.unit))
        else:
            return(Volume(self.magnitude / MLperOZ, "oz"))
        
    def __eq__(self,other):
        "If objects are valid checks if magnitudes are equal to a certain degree, if so returns True, else returns False. If object is invalid returns False"
        if self.unit == None or other.unit == None:
            return(False)
        elif self.unit == other.unit:
            if abs(self.magnitude - other.magnitude) < DELTA:
                return(True)
            else:
                return(False)
        else:
            if self.unit == "ml" and (abs((self.magnitude / MLperOZ) - other.magnitude)) < DELTA:
                return(True)
            elif abs((self.magnitude / MLperOZ) - other.magnitude) < DELTA:
                return(True)
            else:
                return(False)
       
    def add(self,other):
        "If objects are valid adds magnitude of objects and returns new object with the units of the first object. If invalid returns invalid object"
        try:
            if self.unit == None or other.unit == None:
                return(Volume(None,None))
            elif self.unit == "ml":
                if other.unit == "ml":
                    return(Volume((self.magnitude + other.magnitude,"ml")))
                else:
                    return(Volume(self.magnitude + (other.magnitude * MLperOZ),"ml"))
            else:
                if other.unit == "oz":
                    return(Volume(self.magnitude + other.magnitude,"oz"))
                else:
                    return(Volume(self.magnitude + (other.magnitude / MLperOZ),"oz"))
        except:
            if self.unit == None:
                return(Volume(None, None))
            elif self.unit == "ml":
                return(Volume(self.magnitude + other,"ml"))
            else:
                return(Volume(self.magnitude + other,"oz"))

    def sub(self,other):
        "If objects are valid subtracts magnitude of objects and returns new object with the units of the first object. If invalid returns invalid object"
        try:
            if self.unit == None or other.unit == None:
                return(Volume(None, None))
            elif self.unit == "ml":
                if other.unit == "ml":
                    return(Volume(self.magnitude - other.magnitude,"ml"))
                else:
                    return(Volume(self.magnitude - (other.magnitude * MLperOZ),"ml"))
            else:
                if other.unit == "oz":
                    return(Volume(self.magnitude - other.magnitude,"oz"))
                else:
                    return(Volume(self.magnitude - (other.magnitude / MLperOZ),"oz"))
        except:
            if self.unit == None:
                return(Volume(None, None))
            elif self.unit == "ml":
                return(Volume(self.magnitude - other,"ml"))
            else:
                return(Volume(self.magnitude - other,"oz"))
