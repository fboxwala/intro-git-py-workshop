# intro-git-py-workshop
A workshop introducing concepts of open source Python development with Git and Github

To get started with the workshop, head over to the [wiki](https://github.com/fboxwala/intro-git-py-workshop/wiki).

# Caduceus

Caduceus is a python package containing tools to work with data about snakes. Caduceus understands csv files 
about snakes.

To use caducues:

`cd intro-git-py-workshop`

`pip install .`

Now you can import caduceus into your python projects! An example of usage:

```
import caduceus.core as c

snakes = c.build_snakes('data/snakes_by_name.csv', 'data/snake_stats.csv')

c.print_snakes_by_weight(snakes)
```

Running the above snippet with python will return:

```
Blood Python: 500g
Children's Python: 600g
Spotted Python: 700g
Ball Python: 1500g
Indian Python: 2700g
Rock Python: 3000g
Olive Python: 4500g
```
