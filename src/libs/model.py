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