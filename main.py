class Noutbook:
    #Характеристики
    prosessor = 0
    operate_memory = 0
    view_map= 0
    hdd = 0
    matherboard = bool
    screen_size = 0

    def __init__(self,name,type):
        self.name = name
        self.type = type
        if self.type == 'acer':
            self.prosessor = 'Intel® Core™ i5-12400F 6-ядерный 2,50 ГГц'
            self.operate_memory = '8GB'
            self.view_map = '256mb'
            self.hdd = 'FHD DOS черный'
            self.matherboard = 'DA0ZRPMB6D0 Rev:D Acer Aspire V5-551 CPU AMD A8-4555M 1,6GHz.'
            self.screen_size = '(16:9)'

        elif self.type == 'asus':
            self.prosessor = ''
            self.operate_memory = '8GB'
            self.view_map = '256mb'
            self.hdd = 'Aura Sync lighting'
            self.matherboard = '3 PCIe 4.0 x16,'
            self.screen_size = '1920x1080'
        else:
            print('it is makbook')


acer = Noutbook('acers', 'acer')
print(acer.__dict__)
asus = Noutbook('asuss', 'asus')
print(asus.__dict__)
