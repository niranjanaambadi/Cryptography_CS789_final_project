#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 18:51:17 2021

@author: niranjanaambadi
"""

"""
This file is the main driver file of the project. The user has the freedom to choose 
1)his/her role (Alice/Eve/Bob)
2)the encryption algorithm : ElGamal/RSA

"""

import random

import find_primitive #custom py to find primitive root
import generate_prime #custom py to generate a large prime number
import fast_exponentiation #fast exponentiation algorithm custom py
import pollard_rho #custom py for pollard's rho algorithm for factorisation


def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1




from math import ceil,sqrt

"""
Baby step- Giant step algorithm to compute discrete log

@param g -> the base of the logarithm 
@param h -> the value from the logarithm
@param p ->  mod of the prime residual class group 
"""
def bsgs(g, h, p):
    '''
    Solve for x in h = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(g, i, p): i for i in range(N)}

    # Precompute via Fermat's Little Theorem
    c = pow(g, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]

    # Solution not found
    return None

"""
ElGamal Users are Alice,Bob
RSA users are RSA_Alice, RSA_Bob,RSA_Eve
"""
'''
ElGamal
'''
class Alice:
    def __init__(self,message):
        self.msg=message
        self.group=generate_prime.getprime(10)
        
    def getreadyAlice(self):
        
        b=find_primitive.findPrimitive(self.group)
    
        self.r = random.randint(2, self.group)  #random secret number
    
        b_power_r=fast_exponentiation.fast_exp(b, self.r, self.group)
        return b,b_power_r
    
    def sendAlice(self,b,b_power_l):
        temp=(fast_exponentiation.fast_exp(b_power_l,self.r,self.group))#%self.group
        encrypted_msg=(temp*self.msg)%self.group
        return encrypted_msg
        
        
        
class Bob:
    def __init__(self,group,b_,br_):
        self.group=group
        self.b_=b_
        self.br_=br_
        self.inv=1
    
  

    def getreadyBob(self):
        
        l=random.randint(2, self.group)
        b_power_l=(fast_exponentiation.fast_exp(self.b_, l, self.group))#%self.group
        temp=fast_exponentiation.fast_exp(self.br_, l, self.group)
        
        self.inv=modInverse(temp,self.group)
        return self.b_,b_power_l
    
    def receiveBob(self,X):
        decrypted_msg=(X*self.inv)%self.group
        return decrypted_msg
        

    
'''
RSA
'''

class RSA_Alice:
    def __init__(self,message):
        self.msg=message
        self.p=generate_prime.getprime(10)
        self.q=generate_prime.getprime(5)
        if self.p==self.q:
             self.q=generate_prime.getprime(10)
    def coprimes(self,a,phi=1):
        l = []
        for x in range(2, a):
            if gcd(a, x) == 1 and modInverse(x,phi) != None:
                l.append(x)
        for x in l:
            if x == modInverse(x,phi):
                l.remove(x)
        return l  
      
    def getreadyAlice(self):
        self.n=self.p*self.q
        #print("n = p * q = " + str(self.n) + "\n")
        phi=(self.p-1)*(self.q-1)
        #print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")
        
        coprime=self.coprimes(phi,phi)
        self.e=random.choice(coprime)
        #print(self.e)
        
        d=modInverse(self.e, phi)
        
        print("Alice public key (n,e):",self.n,self.e)
        self.privatekey=d
        
    def sendAlice(self,n_bob,e_bob):
        enc_msg=fast_exponentiation.fast_exp(self.msg, e_bob, n_bob)
        
        return enc_msg
        
class RSA_Bob:
    def __init__(self):
        #self.msg=message
        self.p=generate_prime.getprime(10)
        self.q=generate_prime.getprime(5)
        if self.p==self.q:
             self.q=generate_prime.getprime(10)
    
    def coprimes(self,a,phi=1):
        l = []
        for x in range(2, a):
            if gcd(a, x) == 1 and modInverse(x,phi) != None:
                l.append(x)
        for x in l:
            if x == modInverse(x,phi):
                l.remove(x)
        return l  
      
    def getreadyBob(self):
        self.n=self.p*self.q
        #print("n = p * q = " + str(self.n) + "\n")
        phi=(self.p-1)*(self.q-1)
        #print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")
        
        coprime=self.coprimes(phi,phi)
        self.e=random.choice(coprime)
        print(self.e)
        
        d=modInverse(self.e, phi)
        
        print("Bob public key (n,e):",self.n,self.e)
        self.privatekey=d
            
    def receiveBob(self,rcd_msg):
        dec_msg=fast_exponentiation.fast_exp(rcd_msg, self.privatekey, self.n)
        return dec_msg
    
    
class RSA_Eve:
    def __init__(self):
        self.n=int(input("Enter n of the receiver: "))
        self.e=int(input("Enter e of the receiver: "))
        self.msg=int(input("Enter the encrypted message from sender: "))
        
    def eavesdrop(self):
        p=pollard_rho.PollardRho(self.n)
        q=self.n/p
        phi=int((p-1)*(q-1))
        d=modInverse(self.e, phi)
        print(d)
        
        dec_msg=fast_exponentiation.fast_exp(self.msg,d, self.n)
        return dec_msg
'''
ElGamal
1) Alice decided the group and message to be sent. She posts public key.
2) Bob posts public key
3)Alice sends encrypted message
4)  Bob decrypts it
5)Eve tries to break it using receiver's public key, finding its private key using bsgs algorithm.
'''
    

'''
RSA
1) Alice decides group and message to be sent. She posts her public key
2)Bob posts public keys
3)Alice encodes using Bb's key
4)Eve breaks using pollard's rho factoring the n of Bob's key.
5)Bob decrypts the message using his private key.
'''
   
def main():
    role = input("Who are you?:\n Alice-->Sender; Eve-->eavesdropper; Bob-->Receiver\n")
    algo=input("Enter the encryption algorithm E for ElGamal, R for RSA:\n")
    
    
    if algo=='E':
        if role=="Alice":
            msg = int(input("Give the message to be encrypted:\n"))
            print("Original Message :", msg)
            
            A=Alice(msg)
            
            print("Group chosen: ",A.group)
            
            pubkey_alice=A.getreadyAlice()
            print("Alice public key: ", pubkey_alice)
            
            bk1=int(input("Enter bob key 1:"))
            bk2=int(input("Enter bob key 2: "))
            
            encrypted=A.sendAlice(bk1,bk2)
            print("Encrypted message: ",encrypted)
            
            
        elif role=="Bob":
            
            
            group=int(input("Enter group: "))
            ak1=int(input("Enter Alice key 1: "))
            ak2=int(input("Enter Alice key 2: "))
            
            B=Bob(group,ak1,ak2)
            
            pubkey_Bob=B.getreadyBob()
            print("Bob public key: ", pubkey_Bob)
            
            en_msg=int(input("Enter the encoded message from Alice:\n"))
            print("Decrypted message: ", B.receiveBob(en_msg))
        elif role=='Eve':
            g=int(input("Enter group: "))
            key1=int(input("Enter receiver's public key,b: "))
            key2=int(input("Enter receiver's public key,bpow_l: "))
            en_msg=int(input("Enter encrypted message: "))
            rxr_privatekey=bsgs(key1,key2,g)
            print(rxr_privatekey)
            sender_key2=int(input("sender's public key, b_pow r:"))
            print(sender_key2,-rxr_privatekey,g)
            temp=fast_exponentiation.fast_exp(sender_key2, rxr_privatekey, g)
            print(temp)
            decry_msg=en_msg*modInverse(temp,g)
            
            print("Decrypted message is: ",decry_msg%g)
      
                  
        else:
            print("Incorrect choice entered. Choose (Alice/Bob/Eve)!! Run Again..")
    elif algo=='R':
        if role=="Alice":
            msg = int(input("Give the message to be encrypted:\n"))
            print("Original Message :", msg)
            A=RSA_Alice(msg)
            A.getreadyAlice()
            
            n_b=int(input("Enter Bob public key (n):"))
            e_b=int(input("Enter Bob public key (e):"))
            
            encrypted=A.sendAlice(n_b, e_b)
            print("Encrypted message: ",encrypted)
            
        elif role=="Bob":
            B=RSA_Bob()
            B.getreadyBob()
            en_msg=int(input("Enter the encoded message from Alice:\n"))
            print("Decrypted message: ", B.receiveBob(en_msg))
            
        elif role=="Eve":
            E=RSA_Eve()
            message_heard=E.eavesdrop()
            print("Decrypted message by Eve: ", message_heard)
            
        else:
            print("Incorrect choice entered. Choose (Alice/Bob/Eve)!! Run Again..")
    
            
    else:
        print("Incorrect choice entered. Choose (E/R)!! Run Again..")
            
            
            
            
            
            
            
    
            
            
            


if __name__ == '__main__':
    main()