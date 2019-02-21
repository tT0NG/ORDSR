from __future__ import print_function
from numpy import *
from matplotlib.pyplot import *
import os.path
import utility as ut


print('>> Generating DCT basis')
N = 8
if os.path.isfile('./DCTbasis/D_py.npy'):
    print('>>Load DCT transform matrix D:')
    D = np.load('./DCTbasis/D_py.npy')
    print('     ...Finished')
else:
    print('>>Save DCT transform matrix D:')
    D = ut.dctmtx(N)
    np.save('./DCTbasis/D_py.npy', D)
    print('     ...Finished')

# print('The %d DCT-II base is: ' % N)
# np.set_printoptions(precision=3)
# print(D)

B = np.empty([N, N, N, N])

# print('Empty array B'+str(B.shape))
# Save basis for validation

# f = open('DEMO_basis.txt', 'ab')
# if os.stat("DEMO_basis.txt").st_size == 0:
#     SAVE_B = True
# else:
#     SAVE_B = False

for i in range(N):
    for j in range(N):
        Temp = np.outer(D[:, i], D[:, j])
        B[:, :, i, j] = Temp
        # print('B %s = D%d%s * D%d%s Range=%f' % (str(B[:, :, i, j].shape),
        #                                 i, str(D[:, i].shape),
        #                                 j, str(np.transpose(D[:, i]).shape), np.ptp(Temp)))
        # print('The (%i,%i) basis is:' % (i, j))
        # np.set_printoptions(precision=3, suppress=True)
        # print(B[:, :, i, j])
        # if SAVE_B:
        #     np.savetxt(f, B[:, :, i, j], '%10.5f', newline='\n', header='('+str(i)+','+str(j)+')')


# if SAVE_B:
#     f.close()
#     print('>>Save basis (B) Completed.')
# else:
#     print('>>Save basis (B) already Completed.')

if os.path.isfile('./DCTbasis/Bz.npy'):
    print('>>Load ZigZag basis functions Bz:')
    Bz = np.load('./DCTbasis/Bz.npy')
    print('     ...Finished')
else:
    print('>>Save ZigZag basis functions Bz:')
    ZZ = ut.zigzag(N)
    Bz = np.empty([N, N, 1, N * N])
    for i in range(N):
        for j in range(N):
            idx = ZZ[i][j]
            print('B[%i, %i] -> Bz[%i]' % (i, j, idx))
            Bz[:, :, 0, idx] = np.float32(B[:, :, i, j])
    np.save('./DCTbasis/Bz.npy', Bz)
    print('     ...Finished')
