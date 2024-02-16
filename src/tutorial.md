# Tutorial

To illustrate how to use *morpho*, we will solve a problem involving
nematic liquid crystals (NLCs), fluids composed of long, rigid molecules
that possess a local average molecular orientation described by a unit
vector field \\(\mathbf{n}\\). Droplets of NLC immersed in a host
isotropic fluid such as water are called *tactoids* and, unlike droplets
of, say, oil in water that form spheres, tactoids can adopt elongated
shapes.

The functional to be minimized, the free energy of the system, is quite
complex,
#### Free energy
$$ F = \underbrace{\frac{1}{2}\int_{C}K_{11}\left(\nabla\cdot\mathbf{n}\right)^{2}+K_{22}(\mathbf{n}\cdot\nabla\times\mathbf{n})^{2}+K_{33}\left|\mathbf{n}\times\nabla\times\mathbf{n}\right|^{2}dA} $$
$$ \text{Liquid crystal elastic energy}$$

$$ + \underbrace{\sigma\int dl}$$ 

$$ \text{Surface tension} $$

$$ - \underbrace{\frac{W}{2}\int\left(\mathbf{n}\cdot\mathbf{t}\right)^{2}dl}$$ 

$$ \text{Anchoring} $$

where the three terms include **liquid crystal elasticity** that drives elongation of the droplet, **surface
tension** *(s.t.)* that opposes lengthening of the boundary and an
**anchoring term** that imposes a preferred orientation at the boundary.
We need a local constraint, \\(\mathbf{n}\cdot\mathbf{n}=1\\), and will also
impose a constraint on the volume of the droplet. For simplicity, we'll
solve this problem in 2D. The complete code for this tutorial example is
contained in the `examples/tactoid` folder in the repository.
