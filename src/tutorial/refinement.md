# Refinement

We have now solved our first shape optimization problem, and the
complete problem script is provided in the `examples/tutorial` folder
inside the git repository as `tutorial.morpho`. The result we have
obtained in Fig. [4.5](#fig:FinalResult) is, however, a very coarse, low resolution
solution comprising only a relatively small number of elements. To gain
an improved solution, we need to _refine_ our mesh. Because modifying
the mesh also requires us to update other data structures like fields
and selections, a special `MeshRefiner` object is used to perform the
refinement.

To perform refinement we:

1.  Create a `MeshRefiner` object, providing it a list of all the
    `Mesh`, `Field` and `Selection` objects (i.e. the mesh and objects
    that directly depend on it) that need to be updated:
    ```javascript
    var mr = MeshRefiner([m, nn, bnd]); // Set the refiner up
    ```
2.  Call the `refine` method on the `MeshRefiner` object to actually
    perform the refinement. This method returns a `Dictionary` object
    that maps the old objects to potentially newly created ones.
    ```javascript
    var refmap = mr.refine(); // Perform the refinement
    ```
3.  Tell any other objects that refer to the mesh, fields or selections
    to update their references using `refmap`. For example,
    `OptimizationProblem` and `Optimizer` objects are typically updated
    at this step.
    ```javascript
    for (el in [problem, sopt, fopt]) el.update(refmap); // Update the problem
    ```
4.  Update our own references
    ```javascript
    m = refmap[m];
    nn = refmap[nn];
    bnd = refmap[bnd]; // Update variables
    ```

<figure id="fig:Refinement">
<p><img src="../Figures/Tutorial/3Refine/out1.png" style="width:2in"
alt="image" /><img src="../Figures/Tutorial/3Refine/out2.png" style="width:2in"
alt="image" /><img src="../Figures/Tutorial/3Refine/out3.png" style="width:2in"
alt="image" /></p>
<figcaption><span id="fig:Refinement"
label="fig:Refinement"></span>Optimized mesh and director field at three
successive levels of refinement.</figcaption>
</figure>

We insert this code after our optimization section, which causes
_morpho_ to successively optimize and refine.

> The complete code including refinement is in `examples/tutorial` folder inside the git repository as `tutorial2.morpho`

The resulting
optimized shapes are displayed in Fig. [4.6](#fig:Refinement).

    // Optimization loop
    var refmax = 3
    for (refiter in 1..refmax) {
      print "===Refinement level ${refiter}==="
      for (i in 1..100) {
        fopt.linesearch(20)
        sopt.linesearch(20)
      }

      if (refiter==refmax) break

      // Refinement
      var mr=MeshRefiner([m, nn, bnd]) // Set the refiner up
      var refmap=mr.refine() // Perform the refinement
      for (el in [problem, sopt, fopt]) el.update(refmap) // Update the problem
      m=refmap[m]; nn=refmap[nn]; bnd=refmap[bnd] // Update variables
    }
