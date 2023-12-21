from beautifultable import BeautifulTable
import logging
import traceback
import keyboard
import time
import os
from inventory import personal, vendor, belt, common
from config import Config
from logger import Logger
from version import __version__
from screen import start_detecting_window, stop_detecting_window


def main():
    if Config().advanced_options["logg_lvl"] == "info":
        Logger.init(logging.INFO)
    elif Config().advanced_options["logg_lvl"] == "debug":
        Logger.init(logging.DEBUG)
    else:
        print(f"ERROR: Unkown logg_lvl {Config().advanced_options['logg_lvl']}. Must be one of [info, debug]")

    keyboard.add_hotkey(Config().advanced_options["exit_key"], lambda: Logger.info(f'Force Exit') or os._exit(1))

    print(f"============ Gamble {__version__} [name: {Config().general['name']}] ============")
    table = BeautifulTable()
    table.rows.append(["f11", "Start Gamble"])
    table.rows.append([Config().advanced_options['exit_key'], "Stop Gamble"])
    table.columns.header = ["hotkey", "action"]
    print(table)
    print("\n")
	
	
    while 1:
	    if keyboard.is_pressed("f11"):
	        vendor.gamble()
	        break
        time.sleep(0.02)

if __name__ == "__main__":
    # To avoid cmd just closing down, except any errors and add a input() to the end
    try:
        start_detecting_window()
        time.sleep(2)
        main()
    except:
        traceback.print_exc()
    print("Press Enter to exit ...")
    input()
    stop_detecting_window()
