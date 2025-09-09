# Handheld Game Console
This project is a custom-built handheld game console powered by a Raspberry Pi 5. Inspired by Leandro Linares’ DIY design, my version features a 3D-printed enclosure, Python-based GPIO input mapping, and RetroPie integration for multi-console emulation. The build supports custom button hardware, Xbox controller configuration, and RetroAchievements, creating a fully portable retro gaming experience.

## Credits
This project was inspired by Leandro Linares' DIY Handheld Game Console : https://leandrolinares.com/blog/diy-handheld-game-console/
Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).  

## Features 
- 3D-printed enclosure with integrated 5" display and PiSugar 2 Pro battery  
- Python-based GPIO mapping using the GPIO Zero library  
- RetroPie setup supporting a wide range of consoles, including Nintendo DS  
- RetroAchievements integration for in-game achievement tracking

## Project Rundown
- Started with **Recalbox**, but switched to **RetroPie** since it supports more consoles (including Nintendo DS, used for *Pokémon Black & White 2*)  
- Implemented RetroAchievements (not part of original games) for achievement tracking  
- Resolved ROM transfer issue:  
  - On Recalbox → transferred files through network  
  - On RetroPie → network transfer failed → switched to **FileZilla (FTP)** to transfer successfully  
- Improved input handling using **GPIO Zero** since Adafruit Retrogame wasn’t compatible on 64-bit systems  

## Tech Stack
- Raspberry Pi 5  
- RetroPie  
- Python (GPIO Zero library)  
- PiSugar 2 Pro battery  
- 3D-printed enclosure
