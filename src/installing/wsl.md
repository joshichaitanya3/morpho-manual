## Windows via Windows Subsystem for Linux (WSL)

Windows support is provided through Windows Subsystem for Linux (WSL),
which is an environment that enables windows to run linux applications.
We highly recommend using WSL2, which is the most recent version and
provides better support for GUI applications; some instructions for WSL1
are provided below.

1.  Begin by installing the [Ubuntu App](https://ubuntu.com/desktop/wsl)
    from the Microsoft store. Follow all the steps in this link to
    ensure that graphics are working.

2.  Once the Ubuntu terminal is working in Windows, you can install
    *morpho* either through homebrew or by building from source.

#### Graphics On WSL1

If you instead are working on WSL1, then you need to follow these
instructions to get graphics running. Unless mentioned otherwise, all
the commands below are run in the Ubuntu terminal.

1.  A window manager must be installed so that the WSL can create
    windows. On Windows, install
    [VcXsrv](https://sourceforge.net/projects/vcxsrv/). It shows up as
    XLaunch in the Windows start menu.

2.  Open Xlaunch. Then,

    1.  choose 'Multiple windows', set display number to 0, and hit
        'Next'

    2.  choose 'start no client' and hit 'Next'

    3.  **Unselect** 'native opengl' and hit 'Next'

    4.  Hit 'Finish'

3.  In Ubuntu download a package containing a full suite of desktop
    utilities that allows for the use of windows.

        sudo apt install ubuntu-desktop mesa-utils

    Tell ubuntu which display to use

        export DISPLAY=localhost:0

    To set the DISPLAY variable on login type

        echo export DISPLAY=localhost:0 >> ~/.bashrc 

    *\[Note that this assumes you are using bash as your terminal; you
    will may to adjust this line for other terminals\].*

4.  Test that the window system is working by running

        glxgears

    which should open a window with some gears.
