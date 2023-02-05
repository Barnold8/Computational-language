import itertools


class LAC:

    def _union(*argv):
        # A ∪ B = {x | x ∈ A ∨ x ∈ B}
        sets = [x for y in [arg for arg in argv] for x in y]
        return sets

    def _concat(*argv):
        # A ∘ B = { xy | x ∈ ∧ y ∈ B }
        # Note: Returns ALL possible combinations not a set amount
        return list(itertools.product(*[x for x in argv]))

f = [1,2,3,4,5,6,7,8]
a = [10,20,30,40,50,60,70,80]

print(LAC._concat(f,a,a,a,f))