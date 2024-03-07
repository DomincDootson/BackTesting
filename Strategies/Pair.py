from dataclasses import dataclass

@dataclass(frozen = True)
class Pair():
    """So this data class will contain all the information we need about each pair"""
    stock_X : str 
    stock_Y : str 
    beta : float
    std : float
        
    def id(self) -> str:
        """Use for hasing and as an ID"""
        return f"{self.stock_X}:{self.stock_Y}"
        
    def should_open_position(self, alpha_E, X, Y) -> bool:
        """Checks to see if a position should be opened"""
        return abs(Y - self.beta * X)/self.std > alpha_E 

    def should_close_position(self, alpha_L, X, Y) -> bool:
        """Checks to see if a position should be closes"""
        return abs(Y - self.beta * X)/self.std < alpha_L