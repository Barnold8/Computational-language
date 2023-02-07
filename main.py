import itertools


class LAC:

    def _union(*argv):
        # A ∪ B = {x | x ∈ A ∨ x ∈ B}
        return [x for y in [arg for arg in argv] for x in y]

    def _and(*argv):
        # A ∩ B = {x | x ∈ A ∧ x ∈ B}
        result = set(argv[0])
        for lang in argv[1:]:
            result.intersection_update(lang)
        return result

    def _concat(*argv):
        # A ∘ B = { xy | x ∈ ∧ y ∈ B }
        # Note: Returns ALL possible combinations not a set amount
        return list(itertools.product(*[x for x in argv]))

    def _star(arr,elems):
        #A* = {x₁,x₂,x₃...xₖ | k ≥ 0 ∧ x ∈ A}
        return [x for x in arr if len(arr)-1 >= elems][:elems]


L1 = [1,2,3,4,6,7]
L2 = [1,3,7,10]

print(LAC._and(L1,L2))