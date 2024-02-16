# Working with Meshes{#chap:Working-with-Meshes label="chap:Working-with-Meshes"}

This chapter explains a number of ways the user can create and
manipulate Mesh objects in *morpho*. The simplest way to create a mesh
for a desired domain is to use the `meshgen` module, which provides a
very high level and convenient interface. The `meshtools` module
provides low level mesh creation operations and a number of useful
routines to manipulate meshes. The `implicitmesh` module produces
surfaces from implicit functions. Finally, you can use an external
program to create a mesh that exports the data in vtk format using the
`vtk` module.

Mesh creation follows two patterns. Some methods use a **constructor**
pattern where you call a single function that creates the Mesh, e.g.

```javascript
var mesh = LineMesh(fn (t) [t,0], -1..1:0.1)
```

Other approaches follow a **builder** pattern, where you first create a
special helper object,

```javascript
var mb = MeshBuilder()
```

and manipulate it, e.g. by adding elements or setting options. The Mesh
is then created by calling the build method:

```javascript
var mesh = mb.build() 
```