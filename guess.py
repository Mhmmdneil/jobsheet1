class  Guess:
    def __init__(self,jawaban,tebakan):
        self.jawaban= " "
        self.tebakan= " "

def cek(tebakan,jawaban):
    if tebakan == jawaban:
        return True
    return False
    