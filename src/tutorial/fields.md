## Fields

Having created our initial computational domain, we will now create a
`Field` object representing the director field \\(\mathbf{n}\\):

    var nn = Field(m, Matrix([1,0,0]))

As with the `Mesh` object earlier, we declare a variable, *nn*, to refer
to the `Field` object. We have to provide two arguments to `Field`: the
`Mesh` object on which the `Field` is defined, and something to
initialize it. Here, we want the initial director to have a spatially
uniform value, so we can just provide `Field` a constant `Matrix`
object. By default, *morpho* stores a copy of this matrix on each vertex
in the mesh; Fields can however store information on elements of any
grade (and store both more than one quantity per grade and information
on multiple grades at the same time).

It's possible to initialize a `Field` with spatially varying values by
providing an *anonymous function* to `Field` like this:

    var phi = Field(m, fn (x,y,z) x^2+y^2)

Here, *phi* is a scalar field that takes on the value \\(x^{2}+y^{2}\\). The
**fn** keyword is used to define functions.