# Lem-in

This program finds the shortest path from `start` vertice to `end` vertice in a graph.

## Getting Started

### Compiling

Clone the repository

```bash
git clone --recurse-submodules -j8 https://github.com/zshanabek/lem-in.git
```

Enter project

```bash
cd lem-in
```

Compile using Makefile

```bash
make
```

### Usage

Lem-in reads on STDIN so you can just launch it and write your map:

```bash
./lem-in
```

or you can redirect an existing map:

```bash
./lem-in < maps/simple
```

## Example

A map looks like this:

```bash
3
##start
a 0 0
b 1 1
c 2 0
##end
d 3 1
a-b
b-c
d-e
```

It is composed of three parts:

* **Number of ants**. In this case 3 is number of ants
* **Rooms**. `a` and `b` are rooms
* **Links**. `a-b` is the edge between rooms `a` and `b`

`##start` The beginning of path. In this case `a` is a start room

`##end` The exit from path. In this case `d` is a start room

Comments can be anywhere but you have to specify the start and end rooms by putting the commands `##start` and `##end` before declaring the room.
