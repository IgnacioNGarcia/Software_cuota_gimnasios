from abc import ABC, abstractmethod
class Es_pago(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def get_precio(self):
        pass
    