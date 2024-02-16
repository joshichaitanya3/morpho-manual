## The plot module 

<figure id="fig:PlotMesh">
<div class="centering">
<p><span class="sans-serif">A</span><img
src="../Figures/VisChapter/plotmesh/square.png" style="width:2in"
alt="image" /><span class="sans-serif">B</span><img
src="../Figures/VisChapter/plotmesh/square2.png" style="width:2in"
alt="image" /><span class="sans-serif">C</span><img
src="../Figures/VisChapter/plotmesh/square3.png" style="width:2in"
alt="image" /></p>
</div>
<figcaption><strong><span id="fig:PlotMesh"
label="fig:PlotMesh"></span>Using plotmesh.</strong> <strong>A</strong>
By default, the highest grade element is displayed. <strong>B</strong>
Other grades, here points and edges, can be shown by setting the
<code>grade</code> option. <strong>C</strong> The color of the mesh can
be chosen with the color option.</figcaption>
</figure>

The `plot` module offers a convenient way to visualize Meshes, Fields
and Selections. To illustrate its use, we'll create a simple Mesh,

    import meshtools
    var m = AreaMesh(fn (u,v) [u, v, 0], -1..1:0.2, -1..1:0.2)
    m.addgrade(1)

and an associated scalar Field,

    var f = Field(m, fn (x,y) x*y)

#### Meshes

To visualize the Mesh, use the `plotmesh` function

    var g = plotmesh(m)

which outputs a Graphics object, which we'll describe more fully in
the [Graphics Section](graphics_module.md) below. By default, `plotmesh` shows
only the highest grade element presenthere grade 2 or facetsas shown in
Fig. [6.1](#fig:PlotMesh)A. To show other grades, use the `grade`
option:

    var g = plotmesh(m, grade=[0,1])

which shows points and edges as shown in Fig.
[6.1](#fig:PlotMesh)B.

You can control the color of the Mesh with the `color` option as shown
in Fig. [6.1](#fig:PlotMesh)C:

    var g = plotmesh(m, grade=0, color=Red)

To display particular selected elements of a mesh, you can use the
optional `selection` argument and supply a Selection object.

    var sel = Selection(m, fn (x,y,z) x^2+y^2<1)
    sel.addgrade(2)
    var g = plotmesh(m, grade=[0,2], selection=sel)

#### Mesh labels

<figure id="fig:PlotMeshLabels">
<div class="centering">
<p><span class="sans-serif">A</span><img
src="../Figures/VisChapter/plotmeshlabels/meshlabels.png" style="width:2in"
alt="image" /><span class="sans-serif">B</span><img
src="../Figures/VisChapter/plotmeshlabels/meshlabels2.png"
style="width:2in" alt="image" /></p>
</div>
<figcaption><strong><span id="fig:PlotMeshLabels"
label="fig:PlotMeshLabels"></span>Using plotmeshlabels to display
element ids.</strong> <strong>A</strong> Element ids for vertices.
<strong>B</strong> Element ids for the grade 1 elements.</figcaption>
</figure>

It's sometimes helpful to be able to identify the id of a particular
element in a Mesh, especially for debugging purposes. The
`plotmeshlabels` function is designed to facilitate this as shown in
Fig. [6.2](#fig:PlotMeshLabels). You can select which grade to draw ids
for and specify their color, size and draw direction. It's also possible
to give an offset, which can be a list, matrix or even a function, that
adjusts the placement of the labels relative to the center of the
element. Here we offset them a little above and to the right:

    var glabel = plotmeshlabels(m, grade=0, color=Black, offset=[0.025,0.025,0])

The `plotmeshlabels` function only draws labels, not the mesh itself, so
we typically combine it with `plotmesh` and display both:

    var gmesh = plotmesh(m, grade=[0,1])
    var g = gmesh+glabel

To show the grade 1 element ids, for example, we might use:

    var glabel = plotmeshlabels(m, grade=1, color=Red, offset=[-0.05,-0.05,-0.03])

#### Selections

<figure id="fig:PlotSelection">
<div class="centering">
<p><span class="sans-serif">A</span><img
src="../Figures/VisChapter/plotselection/selection.png" style="width:2in"
alt="image" /><span class="sans-serif">B</span><img
src="../Figures/VisChapter/plotselection/selectionbnd.png"
style="width:2in" alt="image" /></p>
</div>
<figcaption><strong><span id="fig:PlotSelection"
label="fig:PlotSelection"></span>Using plotselection.</strong>
<strong>A</strong> Selected elements. <strong>B</strong> Selected
boundary.</figcaption>
</figure>

When setting up a problem in *morpho*, it's very common to use Selection
objects to apply Functionals to limited parts of a Mesh. It's essential
to check that the Selections are correct, and `plotselection` provides
an easy way to do this. To illustrate this, let's select the lower right
hand elements in the Mesh,

    var s = Selection(m, fn (x,y,z) x<=0 && y<=0)
    s.addgrade(1)

and visualize the Selection as shown in Fig.
[6.3](#fig:PlotSelection)A:

    var g = plotselection(m, s, grade=[0,1])

Similarly, we can select the boundary,

    var bnd = Selection(m, boundary=true)

and visualize the selection as shown in Fig.
[6.3](#fig:PlotSelection)B:

    var gbnd = plotselection(m, bnd, grade=[0,1])

#### Fields

Another important use of the `plot` module is to visualize scalar Field
objects. To illustrate this, we'll create an AreaMesh that has more
points,

    var m = AreaMesh(fn (u,v) [u, v, 0], -1..1:0.1, -1..1:0.1)

and a corresponding Field object[^6]:

    var f = Field(m, fn (x,y,z) sin(Pi*x)*sin(Pi*y))

By default, `plotfield` draws points at which the Field is defined, and
colors them by the value as in Fig.
[6.4](#fig:PlotField)A:

    var g = plotfield(f)

Alternatively, `plotfield` can draw higher order elements and
interpolate the coloring if you select the style option appropriately as
shown in Fig. [6.4](#fig:PlotField)B:

    var g = plotfield(f, style="interpolate")

To aid interpretation of these plots, it's common to display a ScaleBar
object alongside the plot. These have quite a few options, including the
position and size, as well as the number of ticks and text layout.

    var sb = ScaleBar(posn=[1.2,0,0], length=1, textcolor=Black)

The scalebar is the then supplied as an optional argument to
`plotfield`. Here, we also use a different colormap object:

    var g = plotfield(f, style="interpolate", scalebar=sb, colormap=PlasmaMap())

The `color` module supplies a number of colormaps that you can try:
ViridisMap is used by default, but PlasmaMap, MagmaMap and InfernoMap
are also recommended and have been specially formulated to be accessible
to users with limited color perception[^7]. GrayMap and HueMap are also
available.

<figure id="fig:PlotField">
<div class="centering">
<p><span class="sans-serif">A</span><img
src="../Figures/VisChapter/plotfield/fieldpts.png" style="width:2in"
alt="image" /><span class="sans-serif">B</span><img
src="../Figures/VisChapter/plotfield/interpolate.png" style="width:2in"
alt="image" /><span class="sans-serif">C</span><img
src="../Figures/VisChapter/plotfield/scalebar.png" style="width:2in"
alt="image" /></p>
</div>
<figcaption><strong><span id="fig:PlotField"
label="fig:PlotField"></span>Visualizing Fields with plotfield.</strong>
<strong>A</strong> By default, the field is displayed by coloring the
respective points. <strong>B</strong> Interpolated view.
<strong>C</strong> The same field with a scalebar added and a different
choice of colormap (here PlasmaMap) used.</figcaption>
</figure>
