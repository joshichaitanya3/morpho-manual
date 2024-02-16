## Implicitmesh

These examples illustrate how to use the `implicitmesh` module to
generate surfaces described as the zero set of a scalar function. The
`sphere.morpho` and `torus.morpho` examples are described more fully in
Chapter X, Section Y. The remaining `threesurface.morpho` creates a
triangulation of a surface with three handles,
$$r_{z}^{4}z^{2}-\left(1-\left(\frac{x}{r_{x}}\right)^{2}-\left(\frac{y}{r_{y}}\right)^{2}\right)\left((x-x_{1})^{2}+y^{2}-r_{1}^{2}\right)\left((x+x_{1})^{2}+y^{2}-r_{1}^{2}\right)\left(x^{2}+y^{2}-r_{1}^{2}\right)=0,$$
where \\(r_{x}\\), \\(r_{y}\\), \\(r_{z}\\), \\(r_{1}\\) and \\(x_{1}\\) are parameters. The
resulting surface is shown in Fig.
[7.7](#fig:Threesurface).

<figure id="fig:Threesurface">
<div class="centering">
<img src="../Figures/ExamplesChapter/implicitmesh/threesurface.png"
style="width:4in" />
</div>
<figcaption><span id="fig:Threesurface"
label="fig:Threesurface"></span><strong>Surface with three
handles</strong> generated with the <code>implicitmesh</code>
module.</figcaption>
</figure>
