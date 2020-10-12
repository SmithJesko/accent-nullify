## Accent Nullify - Seamlessly Blackout Windows
## Made by Smith Jesko and Klay Adams

import winreg

BORDER_PATH = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent"
TITLE_PATH = r"SOFTWARE\Microsoft\Windows\DWM"

accent_color = 'AccentColor' # 0d0d0d
accent_color_inactive = 'AccentColorInactive' # 0d0d0d
border_key = 'AcccentColorMenu' # 0d0d0d
color_prevalence = 'ColorPrevalence' # 1


border_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, BORDER_PATH, 0, winreg.KEY_READ)
title_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, TITLE_PATH, 0, winreg.KEY_READ)