## Cube

<figure id="fig:Cube">
<div class="centering">
<p><img src="../Figures/ExamplesChapter/cube/cube-init.png"
style="width:3in" alt="image" /><img
src="../Figures/ExamplesChapter/cube/cube.png" style="width:3in"
alt="image" /></p>
</div>
<figcaption><strong><span id="fig:Cube" label="fig:Cube"></span>Minimal
surface at constant enclosed volume.</strong> (left) Initial cube
(right) Final optimized structure after 4 levels of
refinement.</figcaption>
</figure>

This example finds a minimal surface with fixed enclosed volume, i.e. a
sphere. It closely parallels a similar example from *Surface Evolver*,
and hence may aid those familiar with that program in learning to use
*morpho*. Starting from an initial cube, shown in Fig.
([7.3](#fig:Cube)), and
created as follows:

     // Create an initial cube
    var m = PolyhedronMesh([ [-0.5, -0.5, -0.5],
                             [ 0.5, -0.5, -0.5],
                             [-0.5,  0.5, -0.5],
                             [ 0.5,  0.5, -0.5],
                             [-0.5, -0.5,  0.5],
                             [ 0.5, -0.5,  0.5],
                             [-0.5,  0.5,  0.5],
                             [ 0.5,  0.5,  0.5]],
                           [ [0,1,3,2], [4,5,7,6],
                             [0,1,5,4], [3,2,6,7],
                             [0,2,6,4], [1,3,7,5] ])

The problem and optimizer are set up:

    var problem = OptimizationProblem(m)
    var la = Area()
    problem.addenergy(la)

    var lv = VolumeEnclosed()
    problem.addconstraint(lv)

    var opt = ShapeOptimizer(problem, m)

The mesh is optimized, then refined, then reoptimized:

    var Nlevels = 4 // Levels of refinement
    var Nsteps = 1000 // Maximum number of steps per refinement level

    for (i in 1..Nlevels) {
      opt.conjugategradient(Nsteps)
      if (i==Nlevels) break
      // Refine
      var mr=MeshRefiner([m])
      var refmap = mr.refine()
      for (el in [problem, opt]) el.update(refmap)
      m = refmap[m]
    }

And finally the resulting area is compared with the true area of a
sphere at the same volume:

    var V0=lv.total(m)
    var Af=la.total(m)
    var R=(V0/(4/3*Pi))^(1/3)
    var area = 4*Pi*R^2
    print "Final area: ${Af} True area: ${area} diff: ${abs(Af-area)}"

