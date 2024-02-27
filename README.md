# Mandelbrot and Julia Sets in Python

# The Julia Set

![Julia Sets](https://github.com/ArmandtErasmus/mandelbrot_and_julia/blob/main/julia02.png)

A Julia set arises from complex polynomials. Consider the map

$$f:\mathbb{C}\rightarrow\mathbb{C} \text{ where } f(z)=z^{2}-p$$


If $$(p_{1},p_{2},...)$$ is an orbit under f, then the orbit is bounded if there exists some constant $R>0$ such that $-R < p_{n} <R$ for all natural numbers n. The filled Julia set for f is the set 

$$(p\in\mathbb{C} | \text{ the orbit of p is bounded })$$

An example of a filled Julia Set:

![Filled Julia Set](https://github.com/ArmandtErasmus/mandelbrot_and_julia/blob/main/julia01.png)

# The Mandelbrot Set

The Mandelbrot set M is a subset of the complex plane defined as

$$M=(c\in\mathbb{C} | \text{ the filled Julia set for } z^{2}+c \text{ is path-connected })$$

Recall that a set is path-connected if every pair of points in the set are connected by a path in the set.

A zoomed in part of the Mandelbrot set looks like the following

![Filled Julia Set](https://github.com/ArmandtErasmus/mandelbrot_and_julia/blob/main/mandel02.png)

![Filled Julia Set](https://github.com/ArmandtErasmus/mandelbrot_and_julia/blob/main/mandel01.png)
