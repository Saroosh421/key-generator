"""key_generator.py"""
import random
class generate:
    def __init__(self,
                num_of_atom = 5,
                separator = '-',
                min_atom_len = 3,
                max_atom_len = 10,
                type_of_value = 'hex',
                capital = 'none',
                extras = [],
                seed = None,):
        self.num_of_atom = num_of_atom
        self.separator = separator
        self.min_atom_len = min_atom_len
        self.max_atom_len = max_atom_len
        self.type_of_value = type_of_value
        self.capital = capital
        self.extras = extras
        self.seed = seed
        self.key = self.__gen_key()
    def __gen_rand_sub_atom_val(self):
        if(self.type_of_value == 'hex'):
            sub_atom_val_code = random.randint(0-len(self.extras), 15)
        elif(self.type_of_value == 'char'):
            sub_atom_val_code = random.randint(10, 35+len(self.extras))
        elif(self.type_of_value == 'int'):
            sub_atom_val_code = random.randint(0-len(self.extras), 9)
        else:
            raise ValueError("Parameter type_of_value takes only 'hex', 'char' or 'int'. Unsupported type '" + str(self.type_of_value) + "'")
        if(sub_atom_val_code >= 10 and sub_atom_val_code <= 35):
            if(self.capital == 'none'):
                starting_letter = 'a'
            elif(self.capital == 'all'):
                starting_letter = 'A'
            elif(self.capital == 'mix'):
                starting_letter = random.choice(['a', 'A'])
            else:
                raise ValueError("Parameter capital takes only 'none', 'all' or 'mix'. Unsupported type '" + str(self.capital) + "'")
            sub_atom_val = chr(ord(starting_letter) + sub_atom_val_code - 10)
        elif(sub_atom_val_code >= 0 and sub_atom_val_code <= 9):
            sub_atom_val = str(sub_atom_val_code)
        elif(sub_atom_val_code < 0):
            sub_atom_val = self.extras[abs(sub_atom_val_code) - 1]
        elif(sub_atom_val_code > 35):
            sub_atom_val = self.extras[sub_atom_val_code - 36]
        return str(sub_atom_val)
    def __gen_rand_atom_val(self):
        num_of_sub_atom = random.randint(self.min_atom_len, self.max_atom_len)
        atom_val = str()
        for _ in range(num_of_sub_atom):
            atom_val += self.__gen_rand_sub_atom_val()
        return atom_val
    def __gen_key(self):
        random.seed(self.seed)
        if(self.min_atom_len > self.max_atom_len):
            raise Exception("min_sub_atom_len cannot be greater than max_sub_atom_len")
        gen_val = str()
        for _ in range(self.num_of_atom - 1):
            gen_val += self.__gen_rand_atom_val()
            if(type(self.separator) == list):
                gen_val += random.choice(self.separator)
            else:
                gen_val += self.separator
        gen_val += self.__gen_rand_atom_val()
        return gen_val
    def get_key(self):
        return self.key
