## Merging meshes

A potential strategy to create meshes for complicated domains is to
begin by creating several simpler meshes and then merging them together
into one larger mesh. The MeshMerge class in the `meshtools` package
allows us to do this. To use it, we create a MeshMerge object with a
list of meshes we wish to merge

    var mrg = MeshMerge([m1, m2, m3, ... ])

and then call the merge method to perform the merge and return the
resulting Mesh:

    var newmesh = mrg.merge()

As an example of this, we will build a mesh that might be an initial
guess for a membrane held between two square fixed boundaries. We'll do
this by creating one octant and then reflecting it along different axes.
The basic unit is constructed with PolyhedronMesh, as shown in Fig.
[5.11](#fig:MeshMerge):

    var a = 0.5 // Vertical separation
    var r = 0.5 // Size of hole
    var L = 1  // Size of box 

    // One octant of the mesh 
    var vertices = [ [r,0,a], [L,0,a], [L,r,a], [L,L,a],
                     [r,L,a], [0,L,a], [0,r,a], [r,r,a],
                     [r,0,0], [r,r,0], [0,r,0] ]
    var faces = [ [0,1,2,7], [2,3,4,7], [7,4,5,6], [0,8,9,7], [6,7,9,10] ]

    var m1 = PolyhedronMesh(vertices, faces)
    m1.addgrade(1)

We now need to create code that reflects a Mesh about one or more axes.
There's more than one way this could be done, but we will here create a
MeshReflector class that follows the builder pattern:

    class MeshReflector {
      init(mesh) {
        self.mesh = mesh
        self.dim = mesh.vertexmatrix().dimensions()[0] // Get Mesh dimension
      }

      // Construct a matrix that reflects about one or more axes    
      _reflectionmatrix(axis) { 
        var rmat = Matrix(self.dim,self.dim)
        for (i in 0...self.dim) rmat[i,i]=1
        if (isint(axis)) rmat[axis,axis]*=-1
        else if (isobject(axis)) for (i in axis) rmat[i,i]*=-1
        return rmat
      }

      reflect(axis) { // Reflect the mesh about the given axis or axes
        var rmat = self._reflectionmatrix(axis)
        // Clone and transform the mesh
        var m = self.mesh.clone()
        for (vid in 0...m.count()) {
          m.setvertexposition(vid, rmat * m.vertexposition(vid))
        }
        return m
      }
    } 

Having defined this class, we create a MeshReflector and use it to build
seven reflected copies:

    var mr = MeshReflector(m1)

    // Merge reflected meshed together
    var merge = MeshMerge([ m1,
                            mr.reflect(0),
                            mr.reflect(1),
                            mr.reflect(2),
                            mr.reflect([0,1]),
                            mr.reflect([1,2]),
                            mr.reflect([2,0]),
                            mr.reflect([0,1,2])
                          ])
    var m = merge.merge()

The resulting mesh is shown in Fig.
[5.11](#fig:MeshMerge),
right panel. Note that MeshMerge automatically removes duplicate
elements as the merge is performed, so that

    print m1.count(1)

reports that there were 35 line elements in the original mesh, while

    print m.count(1)

yields \\(256=8\times(35-6/2)\\) line elements, because there are 6 shared
edges for each copy.

<figure id="fig:MeshMerge">
<p><img src="../Figures/MeshChapter/MeshMerge/unit.png" style="width:3in"
alt="image" /><img src="../Figures/MeshChapter/MeshMerge/final.png"
style="width:3in" alt="image" /></p>
<figcaption><span id="fig:MeshMerge" label="fig:MeshMerge"></span>By
reflecting a small mesh segment (left) about various axes, we can
assemble a larger mesh (right).</figcaption>
</figure>
