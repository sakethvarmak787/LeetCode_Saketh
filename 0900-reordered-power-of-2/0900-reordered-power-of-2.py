class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
   
       
        sorted_n = sorted(str(n))
        
       
        for i in range(30):
            power_of_two = 1 << i  
            
           
            sorted_power_of_two = sorted(str(power_of_two))
        
            if sorted_n == sorted_power_of_two:
                return True
                
    
        return False