# Graph adjacency matrix generator

This project was created for the _Graph Theory_ discipline in the college.  

This project reads a input file(example in *input.txt*) to build a graph and returns whether or not the graph can be divided in two cliques

## Getting started

To run this project you must have PIP installed in your PC.

Run the following command in your terminal to install the project dependencies:
```bash
pip install -r requirements.txt
```

After that you can run this project by use the following command:
```bash
python main.py
```

**If you are in a linux distribution you must change _python_ and _pip_ commands to _python3_ and _pip3_ respectively to use version 3 of Python**

## Useful information

The input file follows the pattern below:  
**first line:** The node names separated by "|"(pipe)  
**other lines:** pairs of edge nodes

After each execution of the project, will be generated two image files: *graph.png* and *complement.png*, respectively,
the graph generated from *input.txt* and the complement graph used to determine if the graph can be divided in two cliques.
