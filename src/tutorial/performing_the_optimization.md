## Performing the optimization

We're now ready to perform the optimization, for which we need an
`Optimizer` object. These come in two flavors: a `ShapeOptimizer` and a
`FieldOptimizer` that respectively act on the shape and a field. We
create them with the problem and quantity they're supposed to act on:
```javascript
// Create shape and field optimizers
var sopt = ShapeOptimizer(problem, m)
var fopt = FieldOptimizer(problem, nn)
```
Having created these, we can perform the optimizion by calling the
`linesearch` method with a specified number of iterations for each:

```javascript
// Optimization loop
for (i in 1..100) {  
    fopt.linesearch(20)
    sopt.linesearch(20)
}
```
Each iteration of a `linesearch` evolves the field (or shape) down the
gradient of the target functional, subject to constraints, and finds an
optimal stepsize to reduce the value of the functional. Here, we
alternate between optimizing the field and optimizing the shape,
performing twenty iterations of each, and overall do this one hundred
times. These numbers have been chosen rather arbitrarily, and if you
look at the output you will notice that *morpho* doesn't always execute
twenty iterations of each. Rather, at each iteration it checks to see if
the change in energy satisfies, $$|E|<\epsilon,$$ or,
$$\left|\frac{\Delta E}{E}\right|<\epsilon$$ where the value of
\\(\epsilon\\), the convergence tolerance can be changed by setting the
`etol` property of the Optimizer object:

```javascript
sopt.etol = 1e-7 // default value is 1e-8
```
Some other properties of an `Optimizer` that may be useful for the user to
adjust are as follows:


|       Property       |   Default value        |Purpose
|----------------------|------------------------|--------------------------------------------------------------------------
|        `etol`        | \\(1\times10^{-8}\\)   | Energy tolerance (relative error)
|        `ctol`        | \\(1\times10^{-10}\\)  | Constraint tolerance (how well are constraints satisfied)
|      `stepsize`      |        `0.1`           |Stepsize for `relax` (changed by linesearch)
|     `steplimit`      |        `0.5`           |Largest stepsize a `linesearch` can take
| `maxconstraintsteps` |        `20`            |Number of steps the optimizer may take to ensure constraints are satisfied
|       `quiet`        |       `false`          |Whether to print output as the optimization happens
