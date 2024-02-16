# Overview 

*Morpho* aims to solve the following class of problems. Consider a
functional,
$$F=\int_{C}f(q,\nabla q,\nabla^{2}q,...)d^{n}x+\int_{\partial C}g(q,\nabla q,\nabla^{2}q,...)d^{n-1}x,$$
where \\(q\\) represents a set of fields defined on a manifold \\(C\\) that
could include scalar, vector, tensor or other quantities and their
derivatives \\(\nabla^{n}q\\). The functional includes terms in the bulk and
on the boundary \\(\partial C\\) and might also include geometric properties
of the manifold such as local curvatures. This functional is to be
minimized from an initial guess \\( \\{ C_{0},q_{0} \\}\\) with
respect to the fields \\(q\\) and the shape of the manifold \\(C\\). Global and
local constraints may be imposed both on \\(C\\) and \\(q\\).

*Morpho* is an object-oriented environment: all components of the
problem, including the computational domain, fields, functionals etc.
are all represented as objects that interact with one another. Much of
the effort in writing a *morpho* program involves creating and
manipulating these objects. The environment is flexible, modular, and
users can easily create new kinds of object, or entirely change how
*morpho* works.

This manual aims to help users to learn to use *morpho*. It provides
installation instructions in [Chapter 2](installing_morpho.md), information about how to run the
program in [Chapter 3](using_morpho.md). A detailed tutorial is provided in
[Chapter 4](tutorial.md), showing how to set up and solve an example
problem. [Chapter 5](working_with_meshes.md) provides information about working
with meshes and [Chapter 6](visualization.md) describes how to visualize the results
of your calculation with *morpho*. The examples provided with morpho are
described in [Chapter 7](examples.md). The remaining chapters, comprising the
second part of the manual, provide a reference guide for all areas of
*morpho* functionality.
