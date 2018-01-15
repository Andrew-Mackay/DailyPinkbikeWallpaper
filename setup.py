from cx_Freeze import setup, Executable

build_exe_opts = {"silent":False,
                  "packages":['lxml', 'gzip'],}

setup(name="PinkbikeWallpaper",
      version="0.1",
      description="Program to set desktop wallpaper to the current PoD on pinkbike",
      options={"build_exe": build_exe_opts},
      executables=[Executable("PinkbikeWallpaper.py")])
