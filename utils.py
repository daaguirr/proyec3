import numpy as np
from numba import cuda
from mpmath import mpf
from mpmath import mp

mp.dps = 300

N = 15
NN = 16
BITS = 32
w = np.uint64(1 << 32)
ones = np.uint32(w - 1)
T = 1024
# x0 = -0.7600189058857350
# y0 = -0.0799516080512771
# x0 = np.float128(-1.7400623825793399052208441670658256382966417204361718668798624184611829)
# y0 = np.float128(-0.0281753397792110489924115211443195096875390767429906085704013095958801)
x0 = mpf('-1.740062382579339905220844167065825638296641720436171866879862418461182919644153056054840718339483225743450008259172138785492983677893366503417299549623738838303346465461290768441055486136870719850559269507357211790243666940134793753068611574745943820712885258222629105433648695946003865')
y0 = mpf('-0.0281753397792110489924115211443195096875390767429906085704013095958801743240920186385400814658560553615695084486774077000669037710191665338060418999324320867147028768983704831316527873719459264592084600433150333362859318102017032958074799966721030307082150171994798478089798638258639934')

BLOCK_SIZE = 64
log2T = int(np.log2(T) + 0.5)


@cuda.jit(device=True)
def fill_zeros(a):
    for i in range(N + 1):
        a[i] = 0


@cuda.jit(device=True)
def copy(source, target):
    for i in range(N + 1):
        target[i] = source[i]
