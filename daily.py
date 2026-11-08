import sys
sys.path.insert(1, r'C:\Users\dinis\OneDrive\Ambiente de Trabalho\Daily')
from daily_bot import daily_bot
import asyncio

if __name__ == "__main__":
  
    #---------------#
    #   VARIABLES   #
    #---------------#
    
    chromedriver_folder_path = r"C:\Users\dinis\OneDrive\Ambiente de Trabalho\chromedriver\chromedriver"
    headless = False
    
    #---------------#
    #   START BOT   #
    #---------------#                   
    
    daily_bot.daily_rewards(chromedriver_folder_path, headless)