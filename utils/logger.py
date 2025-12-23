import logging
from datetime import datetime
from pathlib import Path

class Logger:
    def __init__(self):
        LogDir = Path(__file__).parent.parent / "output"
        LogDir.mkdir(exist_ok=True)
        LogFile = LogDir / f"log_{datetime.now():%Y%m%d_%H%M%S}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(LogFile),
                logging.StreamHandler()
            ]
        )
        self.Logger = logging.getLogger(__name__)
    
    def Info(self, Message):
        self.Logger.info(Message)
    
    def Error(self, Message):
        self.Logger.error(Message)
    
    def Warning(self, Message):
        self.Logger.warning(Message)

LoggerInstance = Logger()
