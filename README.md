# Cryptography_CS789_final_project
Implementation of **ElGamal** and **RSA** algorithms with eavesdropping.

Alice: Sender
Bob: Receiver
Eve: Eavesdropper


##THEORY

The ElGamal and  RSA are two algorithms for public key encryption.

1) Security of the ElGamal algorithm depends on the (presumed) difficulty of computing discrete logs in a
large prime modulus.
2) 1) Security of the RSA depends on the (presumed) difficulty of factoring large integers.


ElGamal has the disadvantage that the ciphertext is twice as
long as the plaintext. It has the advantage that the same plaintext gives a different
ciphertext (with near certainty) each time it is encrypted.   

The entire ElGamal algorithm  is wonderfully explained here:
http://homepages.math.uic.edu/~leon/mcs425-s08/handouts/el-gamal.pdf

In order to eavesdrop, Eve has to find d_A using the baby-step giant step algorithm to compute discrete log.
