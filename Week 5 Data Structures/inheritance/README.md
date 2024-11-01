# CS50x - Week 5: Inheritance

## Problem Overview

In genetics, a person's blood type is determined by two alleles (different forms of a gene). The possible alleles are A, B, and O, and each individual inherits two alleles, which can be the same or different. 
The combinations of alleles lead to the following possible blood types: OO, OA, OB, AO, AA, AB, BO, BA, and BB.

For example:
- If one parent has the blood type AO and the other has BB, their child could potentially have the blood types AB or OB, depending on which allele is inherited from each parent.
- If one parent has AO and the other has OB, the possible blood types for their child would be AO, OB, AB, and OO.

This project simulates the inheritance of blood types within a family tree, taking into account the genetics of each generation.

### Example Usage
```
$ ./inheritance
Child (Generation 0): blood type OO
    Parent (Generation 1): blood type AO
        Grandparent (Generation 2): blood type OA
        Grandparent (Generation 2): blood type BO
    Parent (Generation 1): blood type OB
        Grandparent (Generation 2): blood type AO
        Grandparent (Generation 2): blood type BO
```

## Credit

This project is part of Harvard's CS50x course. For more details, visit: [CS50 Inheritance Problem Set](https://cs50.harvard.edu/x/2024/psets/5/inheritance/).
