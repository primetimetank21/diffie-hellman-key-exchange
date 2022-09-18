from dataclasses import dataclass, field


@dataclass
class Client:
    name: str = field(default=None, repr=True)
    prime_p: int = field(default=None, repr=True)
    base_g: int = field(default=None, repr=True)
    secret_num: int = field(default=None, repr=False)

    def generate_partial_key(self):
        return pow(base=self.base_g, exp=self.secret_num, mod=self.prime_p)

    def generate_full_key(self, partial_key):
        return pow(base=partial_key, exp=self.secret_num, mod=self.prime_p)
