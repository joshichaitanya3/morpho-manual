## Creating the initial mesh

<figure id="fig:Mesh">
<div class="centering">
<p><img src="../Figures/Tutorial/0ExampleMesh/meshgrade0.png" style="width:2in"
alt="image" /><img src="../Figures/Tutorial/0ExampleMesh/meshgrade1.png"
style="width:2in" alt="image" /><img
src="../Figures/Tutorial/0ExampleMesh/meshgrade2.png" style="width:2in"
alt="image" /></p>
</div>
<figcaption><span id="fig:Mesh" label="fig:Mesh"></span>A <em>Mesh</em>
object contains different kinds of element. In this example, the mesh
contains points, lines and area elements referred to by their
<em>grade</em>.</figcaption>
</figure>

Meshes are discretized regions of space. The very simplest region we can
imagine is a *point* or *vertex* described by a set of coordinates
\\((x_{1},x_{2},....,x_{D})\\) where the number of coordinates \\(D\\) defines
the dimensionality of the space that the manifold is said to be
*embedded* in. From more than one point, we can start constructing more
complex regions. First, between two points we can imagine fixing an
imaginary ruler and drawing a straight line or *edge* between them.
Three points define a plane, and also a triangle; we can therefore
identify the two dimensional area of the plane bounded by the triangle
as a *face*, as in the face of a polyhedron. Using four points, we can
define the volume bounded by a tetrahedron. Each of these **elements**
has a different dimensionalitycalled a *grade*and a complete `Mesh` may
contain elements of many different grades as shown in Fig.
[4.2](#fig:Mesh).

*Morpho* provides a number of ways of creating a mesh. One can load a
mesh from a file, build one manually from a set of points, create one
from a polyhedron, or from the level set (contours) of a function.

For this example, we'll use a predefined mesh file `disk.mesh`. To
create a Mesh object from this file, we call the *Mesh* function with
the file name:

```javascript
var m = Mesh("disk.mesh")
```

Here, the **var** keyword tells morpho to create a new variable *m*,
which now refers to the newly created *Mesh* object. 

<figure id="fig:InitialMesh">
<div class="centering">
<img src="../Figures/Tutorial/1Mesh/mesh.png" style="width:3.5in" />
</div>
<figcaption><span id="fig:InitialMesh"
label="fig:InitialMesh"></span>The initial mesh, loaded from
<code>disk.mesh</code>.</figcaption>
</figure>

The initial mesh is
depicted in Fig. [4.3](#fig:InitialMesh); we'll provide the code to perform the
visualization in section
[Visualizing the results](./visualizing_the_results.md).


If you open the file `disk.mesh`, which you can find in the same folder
as `tactoid.morpho`, you'll find it has a simple human readable format:

    vertices

    1 -1. 0. 0 
    2 -0.951057 -0.309017 0
    ...

    edges
    1 8 2 
    2 2 4
    ...

    faces
    1 8 2 4 
    2 8 4 6
    ...

The file is broken into sections, each describing elements of a
different grade. Each line begins either with a section delimiter such
as *vertices*, *edges* or *faces*, or with an id. Vertices are then
defined by a set of coordinates; edges and faces are defined by
providing the respective vertex ids.