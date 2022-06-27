# Pretty Colours
> NOTE: Warning - potential seizure warning!
Simply program which generates random pretty colours on your screen.

Entertains your baby as they randomly mash your keyboard.

## Installation Instructions
More likely than not, your currently installed Python version does not have `tkinter`.

### Ubuntu
  * `apt install python3-tk`
### Arch/Manjaro
  * `pacman -S tk`
### RHEL/CentOS
  * `????`
### Windows
  * `????`
### MacOS
First install `Tkinter` via [homebrew](brew.sh/):
* `brew install tcl-tk`

Next, `python` must be reinstalled with the following environment variables set:
```bash
export PATH="/usr/local/opt/tcl-tk/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/tcl-tk/lib"
export CPPFLAGS="-I/usr/local/opt/tcl-tk/include"
export PKG_CONFIG_PATH="/usr/local/opt/tcl-tk/lib/pkgconfig"
export PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I$(brew --prefix tcl-tk)/include' \
                              --with-tcltk-libs='-L$(brew --prefix tcl-tk)/lib -ltcl8.6 -ltk8.6'"
```

Now, reinstall Python:
```
brew reinstall python
```

## How to use
Run the following:
* `python3 src/prettycolours.py`

Press any key to generate a new colours. To exit, press `CTRL + x`