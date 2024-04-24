## Install from source

The second way to install morpho is by compiling the source code
directly. Morpho now leverages the [CMake](https://cmake.org) build
system, which enables platform independent builds.

#### Where a *morpho* source installation puts things

A *morpho* installation includes help files, modules, and other
resources. By default, these are installed in the **/usr/local/** file
structure as follows:

**/usr/local/bin** : The morpho and morphoview executables are placed here.

**/usr/local/share/morpho** : Help files and modules are stored here.

**/usr/local/include/morpho** : Morpho header files for building extensions.

**/usr/local/lib/morpho** : Morpho extensions.

### Collect Dependencies

_Morpho_ requires a few libraries to provide certain functionality:

**blas/lapack** : are used for dense linear algebra.

**suitesparse** : is used for sparse linear algebra.

> See <https://people.engr.tamu.edu/davis/suitesparse.html> and publications for details

**povray** : is a ray-tracer that is used for publication-quality graphics (only
    required by the `povray` module).

The terminal application uses

**libgrapheme** _or_,

**libunistring**: for unicode grapheme support.

*Morphoview* additionally requires

**glfw** : to provide gui functionality.

**freetype** : provides text display.

Each of these dependencies can be installed using any appropriate
package manager.

-   Homebrew (preferred on macOS):

        brew update
        brew install glfw suite-sparse freetype povray libgrapheme

-   Apt (preferred on Ubuntu):

        sudo apt update
        sudo apt upgrade
        sudo apt install build-essential
        sudo apt install libglfw3-dev libsuitesparse-dev liblapacke povray libfreetype6-dev libunistring-dev

#### Build the morpho shared library

The core piece of *morpho* is a shared library, that can then be used by
multiple applications. To build it,

1.  Obtain the source by cloning the github public repository:

        git clone https://github.com/Morpho-lang/morpho.git

2.  Navigate to the `morpho` folder and build the library:

        cd morpho
        mkdir build
        cd build
        cmake -DCMAKE_BUILD_TYPE=Release ..
        sudo make install

3.  Navigate back out of the morpho folder:

        cd ../../

#### Build the morpho terminal app

The terminal app provides an interactive interface to *morpho*, and can
also run morpho files.

1.  Obtain the source by cloning the github public repository:

        git clone https://github.com/Morpho-lang/morpho-cli.git

2.  Navigate to the `morpho-cli` folder and build the library:

        cd morpho-cli
        mkdir build
        cd build
        cmake -DCMAKE_BUILD_TYPE=Release ..
        sudo make install

3.  Check it works by typing:

        morpho6

4.  Assuming that the morpho terminal app starts correctly, type `quit`
    to return to the shell and then

        cd ../../

    to navigate back out of the morpho-cli folder.

#### Build the morphoview viewer application

*Morphoview* is a simple viewer application to visualize *morpho*
results.

1.  Obtain the source by cloning the github public repository:

        git clone https://github.com/Morpho-lang/morpho-morphoview.git

2.  Navigate to the `morpho-cli` folder and build the library:

        cd morpho-morphoview
        mkdir build
        cd build
        cmake -DCMAKE_BUILD_TYPE=Release ..
        sudo make install

3.  Check it works by typing:

        morphoview

    which should simply run and quit normally. You can then type

        cd ../../

    to navigate back out of the morpho-morphoview folder.

