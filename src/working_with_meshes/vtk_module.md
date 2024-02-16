## The vtk module

The vtk module provides importing and exporting facilities for the
popular VTK file format, which is used by many other programs such as
`paraview`. Unlike morpho *.mesh* files, VTK files can include both Mesh
and Field data. To load a mesh from a VTK file, use a VTKImporter
object:

    import vtk 
    var mv = VTKImporter("file.vtk")
    var m = mv.mesh()

Fields can be loaded in a similar way. Each field in the VTK file has an
identifier, which is passed to the `field` method as a string.

    var f = mv.field("F")
    var g = mv.field("G")

Exporting requires a VTKExporter class,

    import meshtools 
    import vtk 
    var m1 = LineMesh(fn (t) [t,0,0], -1..1:2)
    var g1 = Field(m1, fn(x,y,z) Matrix([x,2*x,3*x]))

    var vtkE = VTKExporter(g1, fieldname="g")
    vtkE.export("data.vtk")