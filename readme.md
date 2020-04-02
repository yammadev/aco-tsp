## Solving Travelling Salesman Problem using Ant Colony Optimization
Taking as data a [Symmetric traveling salesman problem (TSP)](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/): `kroA100.tsp` - **The 100-city problem A** by *Krolak/Felts/Nelson*

### Ant Colony Optimization (ACO)
It is an **optimization algorithm** used to find the shortest path between points or nodes. It is developed by observing the behaviour of ants when they follow a path to their food source. Ants are essentially blind so they follow pheromone trails left behind by other ants on the path. This algorithm follows the same approach by using the probability of going to the next node as the distance to the node and the amount of pheromones.

### Symmetric traveling salesman problem (TSP)
Given a set of **n** nodes and distances for each pair of **nodes**, find a roundtrip of minimal total length visiting each node exactly once. The distance from node *i* to node *j* is the same as from node *j* to node *i*.

### Author
Yefferson Marí­n - ([@yammadev](https://github.com/yammadev))

## Implementation
TO DO

## Changelog
All notable changes to this project are documented in this part of the file. The format is based on [Keep a Changelog](http://keepachangelog.com/).

#### [x.y.z] - AAAA-MM-DD / YYYY-MM-DD
- **x** for major release related to major additions or changes.
- **y** for minor release related to minor additions or changes in current major release.
- **z** for minor release related to minor additions or changes in current minor release.

#### Extras / Extras
- **Added** for new features.
- **Modified** for changes in existing functionality.
- **Deprecated** for soon-to-be removed features.
- **Removed** for removed features.
- **Fixed for** any bug fixes.
- **Security** in case of vulnerabilities.

### [1.2.1] - 2020-04-02
#### Modified
- Restructured for better code reading and implementation.

### [1.2.0] - 2020-04-01
#### Added
- Plotting features.

#### Modified
- Better code structure.
- Readme edited.

### [1.1.0] - 2020-04-01
#### Added
- `.tsp` data is readen and displayed.
- Calls from `Jupiter Notebook` file.

### [1.0.0] - 2020-03-31
#### Added
- Initial commit with minimal `Jupiter Notebook` config.
- `kroA100.tsp` file added - the `100-city problem A` (Krolak/Felts/Nelson)
