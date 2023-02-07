import itertools

class LAC:

    def _union(*argv):
        # A ∪ B = {x | x ∈ A ∨ x ∈ B}
        return [x for y in [arg for arg in argv] for x in y]

    def _and(*argv):
        # A ∩ B = {x | x ∈ A ∧ x ∈ B}
        result = set(argv[0])
        for lang in argv[1:]:
            if len(lang) == 0:
                return set([])
            result.intersection_update(lang)
        return result 

    def _concat(*argv):
        # A ∘ B = { xy | x ∈ ∧ y ∈ B }
        # Note: Returns ALL possible combinations. Takes lang1,lang2,lang3...langk
        return list(itertools.product(*[x for x in argv])) if len(argv) > 1 else set([])

    def _star(arr,elems):
        #A* = {x₁,x₂,x₃...xₖ | k ≥ 0 ∧ x ∈ A}
        # Horribly broken. Needs work
        _arr = arr
        elems = elems-1
        if elems == 0:
            return []
        else:
            return LAC._concat(arr,arr)

L1 = [1,2,3,4,6,7]
L2 = ['a','b']

print(LAC._star(L1,2))