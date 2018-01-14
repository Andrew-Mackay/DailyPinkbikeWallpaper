from cx_Freeze import setup, Executable

setup(name="Pinkbike Wallpaper",
      version="0.1",
      description="Program to set desktop wallpaper to the current PoD on pinkbike",
      executables=[Executable("dailyPinkbikeWallpaperWindows10.py")])
