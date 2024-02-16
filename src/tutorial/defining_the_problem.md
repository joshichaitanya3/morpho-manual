## Defining the problem

We now turn to setting up the problem. Each term in the energy
functional [(1)](../tutorial.md#free-energy) is represented by a corresponding *functional*
object, which acts on a `Mesh` (and possibly a `Field`) to calculate an
integral quantity such as an energy; Functional objects are also
responsible for calculating gradients of the energy with respect to
vertex positions and components of Fields.

Let's take the terms in [(1)](../tutorial.md#free-energy) one by one: To represent the nematic elasticity we
create a `Nematic` object:

    var lf=Nematic(nn)

The surface tension term involves the length of the boundary, so we need
a `Length` object:

    var lt=Length()

The anchoring term doesn't have a simple built in object type, but we
can use a general `LineIntegral` object to achieve the correct result.

    var la=LineIntegral(fn (x, n) n.inner(tangent())^2, nn)

Notice that we have to supply a functionthe integrandwhich will be
called by `LineIntegral` when it evaluates the integral. Integrand
functions are called with the local coordinates first (as a `Matrix`
object representing a column vector) and then the local interpolated
value of any number of `Fields`. We also make use of the special
function `tangent()` that locally returns a local tangent to the line.

We also need to impose constraints. Any *functional* object can be used
equally well as an energy or a constraint, and hence we create a
`NormSq` (norm-squared) object that will be used to implement the local
unit vector constraint on the director field:

    var ln=NormSq(nn)

and an `Area` object for the global constraint. This is really a
constraint fixing the volume of fluid in the droplet, but since we're in
2D that becomes a constraint on the area of the mesh:

    var laa=Area()

Now we have a collection of functional objects that we can use to define
the problem. So far, we haven't specified which functionals are energies
and which are constraints; nor have we specified which parts of the mesh
the functionals are to be evaluated over. All that information is
collected in an `OptimizationProblem` object, which we will now create:

    // Set up the optimization problem
    var W = 1
    var sigma = 1

    var problem = OptimizationProblem(m)
    problem.addenergy(lf)
    problem.addenergy(la, selection=bnd, prefactor=-W/2)
    problem.addenergy(lt, selection=bnd, prefactor=sigma)
    problem.addconstraint(laa)
    problem.addlocalconstraint(ln, field=nn, target=1)

Notice that some of these functionals only act on a selection such as
the boundary and hence we use the optional `selection` parameter to
specify this. We can also specify the prefactor of the functional.
