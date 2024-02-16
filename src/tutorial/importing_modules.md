## Importing modules

*Morpho* is a modular system and hence we typically begin our program by
telling *morpho* the modules we need so that they're available for us to
use. To do so, we use the `import` keyword followed by the name of the
module:
```javascript
    import meshtools
    import optimize
    import plot
```
We can also use the `import` keyword to import additional program files
to assist in modularizing large programs. These are the modules we'll
use for this example:


|Module       |Purpose
|-------------|------------------------------------------
|`meshtools`  |Utility code to create and refine meshes
|`optimize`   |Perform optimization
|`plot`       |Visualize results
