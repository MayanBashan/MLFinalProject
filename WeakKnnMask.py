

class WeakKnnMask:
    def __init__(self, name, mask_vec, mask_fields):
        self.mask_vec = mask_vec
        self.name = name
        self.mask_fields = mask_fields

    def mask(self, vec):
        return [vec[i] for i in self.mask_vec]

    def mask_base(self, base_set):
        masked_base = []
        for vec in base_set:
            masked_base.append(self.mask(vec))
        return masked_base
