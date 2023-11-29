class Solution:
    def convertTemperature(self, num: float) -> List[float]:

        
        res= []
        kelvin = str(num + 273.15)
        f = str(num * 1.80 + 32)
        res.append(float(kelvin))
        res.append(float(f))
        return res
