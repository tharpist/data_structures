"""
Bloom Filters are lightweight versions of 
a has table. Efficient insertions and lookups

They are more space efficient than a has table
but this comes at the cost of having false positives
for entry lookup

They should be used when fast lookups and insertions
are needed. I care about how much space the structure uses
and i don't care if it indicates if an item is there or if it
is not

EG: I run website and want to keep track of IP
addresses that are blocked. I dont care if a blocked IP
is occasionally able to access my website, but I do care if someone not 
on the blocked list is unable to access the site

bit_vector is list of bits
"""
import pyhash

bit_vector = [0] * 20

#Non Cryptographic hash functions (murmer and FNV)
fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

#Calculate the output of FNV and Murmur hash functions for Pikachu and Charmander
fnv_pika = fnv("Pikachu") % 20
fnv_char = fnv("Charmander") % 20

murmur_pika = murmur("Pikachu") % 20
murmur_char = murmur("Charmander") % 20

bit_vector[fnv_pika] = 1
bit_vector[murmur_pika] = 1

bit_vector[fnv_char] = 1
bit_vector[murmur_char] = 1

#print(fnv_pika)
#print(fnv_char)
#print(murmur_pika)
#print(murmur_char)

# A WILD BULBASAUR APPEAR
fnv_bulb = fnv("Bulbasaur") % 20
murmur_bulb = murmur("Bulbasaur") % 20

print(bit_vector[fnv_bulb])
print(bit_vector[murmur_bulb])

