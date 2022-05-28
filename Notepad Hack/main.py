import pyautogui
import time

pyautogui.press('win')
pyautogui.typewrite('notepad')
time.sleep(.3)
pyautogui.press('enter')
time.sleep(1)

pyautogui.hotkey('win', 'up')

pyautogui.press('alt')
pyautogui.press('right', presses=2)
pyautogui.press('enter')
time.sleep(.3)

pyautogui.press('down')
pyautogui.press('enter')

pyautogui.typewrite('Comic Sans MS')

pyautogui.press('tab')

pyautogui.typewrite('Bold')

pyautogui.press('tab')

pyautogui.typewrite('55')

pyautogui.press('enter')

pyautogui.typewrite('You are hacked and\nall your files are encrypted!\n')

pyautogui.typewrite('\nIf you want your files back\nyou have to pay 2 lakh rupees!')

pyautogui.press('enter')

pyautogui.hotkey('win', '.')
time.sleep(.5)
pyautogui.press('down')
pyautogui.press('enter')
