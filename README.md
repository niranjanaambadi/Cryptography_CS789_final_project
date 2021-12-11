# Cryptography_CS789_final_project
Implementation of **ElGamal** and **RSA** algorithms with eavesdropping.

Alice: Sender
Bob: Receiver
Eve: Eavesdropper


##THEORY

The ElGamal and  RSA are two algorithms for public key encryption.
1) Security of the RSA depends on the (presumed) difficulty of factoring large integers.
2) Security of the ElGamal algorithm depends on the (presumed) difficulty of computing discrete logs in a
large prime modulus.

ElGamal has the disadvantage that the ciphertext is twice as
long as the plaintext. It has the advantage that the same plaintext gives a different
ciphertext (with near certainty) each time it is encrypted. 

