from cornell_gpt import GPTLanguageModel
import torch
import torch.nn as nn
from torch.nn import functional as F

print("wtf")
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Load the model
print("hi")
model = GPTLanguageModel()
print("hi2")
model.load_state_dict(torch.load('cornell_gpt.pth'))
print("hi3")
model.to(device)
model.eval()

# read data set
with open('./archive/movie_lines.tsv', 'r', encoding='utf-8') as f:
    text = f.read()

# here are all the unique characters that occur in this text
chars = sorted(list(set(text)))
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s] # encoder: take a string, output a list of integers
decode = lambda l: ''.join([itos[i] for i in l]) # decoder: take a list of integers, output a string

print("inference")
input = "wow"
data = torch.tensor(encode(input), dtype=torch.long, device=device)
data = data.reshape(len(input),1)
print(data.shape)
print(decode(model.generate(data,max_new_tokens=200)[0].tolist()))
print(model)

##  ssh -L5999:/tmp/dcs-tmp.u2101112/.vnc-socket u2101112@remote-12.dcs.warwick.ac.uk