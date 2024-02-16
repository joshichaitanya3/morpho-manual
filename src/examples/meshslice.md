## Meshslice

<figure id="fig:Meshslice">
<div class="centering">
<img src="../Figures/ExamplesChapter/meshslice/meshslice2.png"
style="width:4in" />
</div>
<figcaption><strong><span id="fig:Meshslice"
label="fig:Meshslice"></span>Mesh sliced along three planes</strong>
showing a scalar field interpolated onto each slice.</figcaption>
</figure>

This example shows how to use the `meshslice` module to create a slice
through a mesh for visualization purposes. The program uses a spherical
mesh,

    var m = Mesh("sphere.mesh")
    m.addgrade(1)
    m.addgrade(2)

and creates a couple of example Fields, one scalar,

    var phi = Field(m, fn (x,y,z) x+y+z)

and one vector,

    var nn = Field(m, fn (x,y,z) Matrix([x,y,z])/sqrt(x^2+y^2+z^2))

A MeshSlicer is created to do the slicing,

    var slice = MeshSlicer(m)
    var slc = slice.slice([0,0,0], [1,0,0])

and then interpolated Fields along this slice are created too,

    var sphi = slice.slicefield(phi)
    var snn = slice.slicefield(nn)

Grade 1 elements (edges) from the original mesh, together with the field
phi interpolated onto three different slices, are shown in Fig.
[7.10](#fig:Meshslice).
The example program illustrates a few other different possibilities.
