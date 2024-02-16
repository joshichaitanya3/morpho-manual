## Delaunay

<figure id="fig:Delaunay">
<div class="centering">
<p><img src="../Figures/ExamplesChapter/delaunay/delaunay-2d.png"
style="width:3in" alt="image" /><img
src="../Figures/ExamplesChapter/delaunay/delaunay-3d.png" style="width:3in"
alt="image" /></p>
</div>
<figcaption><strong><span id="fig:Delaunay"
label="fig:Delaunay"></span>Delaunay triangulation.</strong> (left)
Triangulation of random 2D point cloud (right) Tetrahedralization of
random 3D point cloud.</figcaption>
</figure>

This example demonstrates use of the `delaunay` module to create a
Delaunay triangulation from a point cloud. The triangulation generated
is explicitly checked for the property that no point other than the
vertices lies within the circumsphere of each triangle.
