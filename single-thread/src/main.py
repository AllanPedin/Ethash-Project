from mine import *
from cache import get_full_size, get_cache_size, mkcache
from dataset import calc_dataset
from block import get_block_header, number, difficulty

SEED = 1010101010

block_number = number #most recent block nov 7

full_size = get_full_size(block_number)
cache_size =  get_cache_size(block_number)
cache = mkcache(cache_size, SEED)
dataset = calc_dataset(full_size, cache) 
header = get_block_header()

nonce = mine(full_size, dataset, header, difficulty)