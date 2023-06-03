from huggingface_hub import from_pretrained_keras


class CganCols:
    def __init__(self):
        self.model_0 = from_pretrained_keras('SupawitMarayat/pimthaigans-cgan-0010')
        self.model_1 = from_pretrained_keras('SupawitMarayat/pimthaigans-cgan-1121')
        self.model_2 = from_pretrained_keras('SupawitMarayat/pimthaigans-cgan-2232')
        self.model_3 = from_pretrained_keras('SupawitMarayat/pimthaigans-cgan-3343')
        self.model_4 = from_pretrained_keras('SupawitMarayat/pimthaigans-cgan-4454')
        self.model_5 = from_pretrained_keras('SupawitMarayat/pimthaigans-cgan-5565')
        self.model_6 = from_pretrained_keras('SupawitMarayat/pimthaigans-cgan-6676')
        self.model_7 = from_pretrained_keras('SupawitMarayat/pimthaigans-cgan-7787')

        self.model_cols = [self.model_0, self.model_1, self.model_2, self.model_3, self.model_4, self.model_5,
                           self.model_6, self.model_7]


def get_model(index: int):
    """
    Returns the model based on the given index.

    Index ranges and corresponding model values:
    0-10   ->  0
    11-21  ->  1
    22-32  ->  2
    33-43  ->  3
    44-54  ->  4
    55-65  ->  5
    66-76  ->  6
    77-87  ->  7

    :param index: The index value.
    :return: The corresponding model value.
    """
    if 0 <= index <= 10:
        return 0
    elif 11 <= index <= 21:
        return 1
    elif 22 <= index <= 32:
        return 2
    elif 33 <= index <= 43:
        return 3
    elif 44 <= index <= 54:
        return 4
    elif 55 <= index <= 65:
        return 5
    elif 66 <= index <= 76:
        return 6
    elif 77 <= index <= 87:
        return 7
