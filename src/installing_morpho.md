# Installing *Morpho*

*Morpho* is hosted on a publicly available github repository
<https://github.com/Morpho-lang/morpho>. We are continuously working on
improving *morpho* installation. With this release, *morpho* on macOS
now has a streamlined installation process using homebrew. Other
platforms must be installed from source and we hope to provide packages
for future releases. Instructions for different platforms are provided
below.

### Where *morpho* installation puts things

A *morpho* installation includes help files, modules, and other
resources. By default, these are installed in the **/usr/local/** file
structure[^1], including in the following places:

**/usr/local/bin** : The morpho and morphoview executables are placed here.

**/usr/local/share/morpho** : Help files and modules are stored here.

**/usr/local/include/morpho** : Morpho header files for building extensions.

**/usr/local/lib/morpho** : Morpho extensions.

It's possible to build *morpho* to use different locations for resources
and the binary. To do so, set the `MORPHORESOURCESDIR` option when you
run make, e.g.

    sudo make MORPHORESOURCESDIR=X install

where X is the base folder you wish to use, i.e. the replacement for
**/usr/local**. Subfolders will be created by the installer. To control
where the *morpho* binary is placed, also set the `DESTDIR` option,

    sudo make MORPHORESOURCESDIR=X DESTDIR=Y install

### Dependencies

*Morpho* leverages a few libraries to provide certain functionality:

**glfw** : is used to provide gui functionality for an interactive visualization application, `morphoview`.

**blas/lapack** : are used for dense linear algebra.

**suitesparse** : is used for sparse linear algebra[^2].

**freetype** : provides text display.

**povray** : is a ray-tracer that is used for publication-quality graphics.

### macOS

The recommended approach to installing morpho on macOS is to use the
[Homebrew](https://brew.sh) package manager.

1.  If you have a previous installation of morpho, we recommend you
    remove it by following the instructions for uninstalling *morpho*
    below.

2.  Install [Homebrew](https://brew.sh), following instructions on the
    homebrew site.

3.  In the terminal type:

        brew update
        brew tap morpho-lang/morpho
        brew install morpho

    You may be prompted by homebrew to install additional components.
    For some users, it may be necessary to install XCode from the App
    Store.

4.  We also recommend that you obtain the morpho git repository, because
    it contains the manual, examples and other useful materials that
    aren't installed by homebrew.

        git clone https://github.com/Morpho-lang/morpho.git

### macOS (Manual Installation)

If you ever need to do a manual installation, for example if you want to
use the cutting edge `dev` branch of morpho, you should follow these
instructions. If you have an Intel mac, you should omit the
`-f Makefile.m1` flags in the make command below. Note also that some
users may need to preface

    make install

with the sudo command:

    sudo make install

1.  Install the [Homebrew](https://brew.sh) package manager, following
    instructions on the homebrew site.

2.  **If you previously installed morpho using homebrew, you must first
    remove it. This step is vitally important as the two installed
    versions may cause conflicts.**

        brew uninstall morpho

3.  Install dependencies. Open the Terminal application and type:

        brew update
        brew install glfw suite-sparse freetype povray

4.  Obtain the source by cloning the github public repository:

        git clone https://github.com/Morpho-lang/morpho.git

5.  Navigate to the `morpho5` folder within the downloaded repository
    and build the application[^3]

        cd morpho/morpho5
        make -f Makefile.m1 install

6.  Navigate to the `morphoview` folder and build the viewer application

        cd morpho/morphoview
        make -f Makefile.m1 install

7.  Check that the application works by typing

        morpho5

**If you wish to switch back to a homebrew install, follow the
instructions below to uninstall morpho to prevent version conflicts.**

### Linux

Building on Linux is similar to the macOS manual install. Here we give
commands for Ubuntu, which uses the `apt` package manager. On other
distributions you will need to find the equivalent packages.

1.  Make sure your version of apt is up to date.

        sudo apt update
        sudo apt upgrade

2.  Ensure you have basic developer tools installed. Some distributions
    omit these to save space.

        sudo apt install build-essential

3.  Install *morpho*'s dependencies using your distribution's package
    manager (or manually if you prefer):

        sudo apt install libglfw3-dev libsuitesparse-dev liblapacke povraylibfreetype6-dev

4.  Obtain the source by cloning the github public repository:

        git clone https://github.com/Morpho-lang/morpho.git

5.  Navigate to the `morpho5` folder within the downloaded repository
    and build the application:

        cd morpho/morpho5
        sudo make -f Makefile.linux install

6.  Navigate to the `morphoview` folder and build the viewer
    application:

        cd ../morphoview
        sudo make -f Makefile.linux install

7.  Check that the application works by typing

        morpho5

### Windows via Windows Subsystem for Linux (WSL)

#### Install WSL

If you don't have WSL2 installed on your Windows computer, [follow the
instructions to install the Ubuntu
App](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview).
Follow all the steps in this link to ensure that graphics are working.

#### Install Morpho

Once the Ubuntu terminal is working in Windows, you can install *morpho*
the same way as in Linux by running the commands in the instructions in
the Ubuntu terminal.

**If you are using WSL2, then the installation is complete.**

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

5.  **Test the thomson example program.** Navigate to the thomson
    example in the examples directory and run it. If you are in the
    `morphoview` directory.

        cd ../examples/thomson
        morpho5 thomson.morpho

    This example starts with randomly distributed charges on a sphere
    and minimizing electric potential. It should generate an interactive
    figure of points on a sphere.

### Updating *morpho*

As new versions of *morpho* are released, you will likely want to
upgrade to the latest version. From the terminal:

-   If you used homebrew to install morpho, simply type,

        brew upgrade morpho

-   If you installed *morpho* manually, and still have the git
    repository folder on your computer, navigate to this with `cd` and
    type,

        git pull

    which downloads any updates. You can then follow the above
    instructions to recompile *morpho.* It's not necessary to reinstall
    dependencies, but note that some new releases of *morpho* may
    require additional dependencies.

-   If you no longer have the original *morpho* git repository folder
    from which you installed morpho, simply rerun the installation from
    scratch as above. You shouldn't need to reinstall dependencies.

### Uninstalling *morpho*

If you wish to uninstall morpho, you can do so simply from the terminal
application.

-   If you used homebrew to install morpho, simply type

        brew uninstall morpho

-   Alternatively, if you did a manual install, you can remove
    everything with

        rm /usr/local/bin/morpho
        rm /usr/local/bin/morphoview
        rm -r /usr/local/share/morpho
        rm -r /usr/local/lib/morpho

    You may need to prefix these with `sudo`.

[^1]: On the macOS, these files are contained within the homebrew system