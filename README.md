# Cryptography_CS789_final_project
Implementation of **ElGamal** and **RSA** algorithms with eavesdropping.

Alice: Sender
Bob: Receiver
Eve: Eavesdropper


## THEORY

The ElGamal and  RSA are two algorithms for public key encryption.

1) Security of the ElGamal algorithm depends on the (presumed) difficulty of computing discrete logs in a
large prime modulus.
2) Security of the RSA depends on the (presumed) difficulty of factoring large integers.


ElGamal has the disadvantage that the ciphertext is twice as
long as the plaintext. It has the advantage that the same plaintext gives a different
ciphertext (with near certainty) each time it is encrypted.   

The entire ElGamal algorithm  is wonderfully explained here:
http://homepages.math.uic.edu/~leon/mcs425-s08/handouts/el-gamal.pdf

In order to eavesdrop, Eve has to find d_A using the baby-step giant step algorithm to compute discrete log.

RSA algorithm is based on the fact that there is no known way to factor n as pq in
any reasonable amount of time, where p and q are two large primes and n their product. The RSA cryptosystem is wonderfully explained in the following handout:http://homepages.math.uic.edu/~leon/mcs425-s08/handouts/RSA.pdf

This still doesnot make RSA totally immune to eavesdropping. If one of the primes is significantly smaller than the other, it is possible to break RSA using Pollard's rho algorithm which is beautifully explained here: https://www.geeksforgeeks.org/pollards-rho-algorithm-prime-factorization/

##  How to execute?

I have implemented a driver.py file which should be run after downloading the repository.
This would prompt the user to select 
1. Algorithm (RSA/ElGamal) 
2. Role he/she plays (Alice/Bob/Eve)

Do as directed and you get the system working!

