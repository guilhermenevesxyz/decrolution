# Decrolution
Decrolution is a **Python library** that allows one to **create life simulations**,
using [Darwinism](https://en.wikipedia.org/wiki/Darwinism) rules.

This repository includes **the library itself**,
as well as **a minimal font-end implementation**,
for allowing users to see what is going on without having to code their own front-ends.

## License
The project is divided into **two parts**: the **library** and the **front-end**.
The library itself is licensed under the terms of [LGPL v3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html),
while the front-end is under the public domain ([Unlicense](https://unlicense.org/)).

## Functioning
### Creatures
The universe consists of **a grid** containing all the **creatures**.
Each creature has **some data** associated with it.
Some of these data are **genome data**, meaning that they get **passed to the offspring**.
The others--**autonomous data**--are some data **specific** to that individual creature,
and that individual creature only.
Note that this division is not made clear in the library's code.

#### Genome Data
The genome data consist of some traits which get **inherited**.
These **cannot be modified** throughout the creature's life.
Examples of genome data are the colour, the strength or the life expectancy.
When the creature reproduces itself,
the offspring get a mixture of these traits from both of their parents.

#### Autonomous Data
These data **are not inherited** and **may or may not change** throughout the individual creature's life.
The sex, for example, **does not change**.
On the other hand, the energy and age **change over time**.

### Brain
Each creature has a brain,
which itself is a data structure consisting of a hashmap **linking sensors to behaviours**.

A creature's sensors might detect things like the creatures sorrounding it or if there's food nearby.
These data are then passed to the brain,
which has inherent links between them and some possible behaviours in response.
These behaviours can be moving, attacking or eating.
These traits are **inheritable**.

### General Ideas
#### Genetic Variety
The colours in a population are hints of the genetic variety that is present in it.
Many colours mean much variety and vice versa.

They can be used to distinguish the individuals which have certain mutations in them
and help knowing how genetically similar some specimens are.
The colours are also useful to detect mutations,
since they change in mutated individuals.

Some creatures might also be hostile towards different creatures with other colours,
thus protecting their family from predation.

#### Death
Alive creatures usually have bright colours.
Once they perish, their colours become reddish and much darker.
Defunct creatures won't disappear on their own.
The deceased must be eaten by others in order to disappear completely.

#### Breeding
Creatures can start procreation once they hit the age of 18.
After that point, there are no limits as to what they can do till they pass away.

#### Climate influence on metabolism
The left side of the arena is colder, whilst the right side is warmer,
thus creating a temperature gradient.
Creatures on the left side will have a slower metabolism and thence live longer lives,
but they will also be less fertile.
Meanwhile, the creatures on the right, warmer, side of the arena will have faster metabolisms,
allowing them to reproduce more, but dying faster in comparison.

The left-right division **does not** entail any political references.
There had to be a division and a north/south one would have looked worse on the screen,
whilst also not inclusive of those living in the southern hemisphere.

### Tips
The simulation should not produce capable survivors on every single run.
Be patient and try a number of times until you get a good seed.
It should not take too long to do so, in most cases.

