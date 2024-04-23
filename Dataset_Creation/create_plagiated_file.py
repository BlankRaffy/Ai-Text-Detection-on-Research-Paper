import torch
from transformers import BartForConditionalGeneration, BartTokenizer

input_sentence = """This paper presents an experimental study and the lessons 
learned from the observation of the attackers when logged on a 
compromised machine. The results are based on a six months 
period during which a controlled experiment has been run with 
a high interaction honeypot. We correlate our findings with 
those obtained with a worldwide distributed system of low-
interaction honeypots. """

model = BartForConditionalGeneration.from_pretrained('eugenesiow/bart-paraphrase')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
tokenizer = BartTokenizer.from_pretrained('eugenesiow/bart-paraphrase')

# Set max_length parameter for generation
max_length = 300  # You can adjust this value as needed

# Tokenize input sentence
batch = tokenizer(input_sentence, return_tensors='pt')

# Generate paraphrased text with specified max_length
generated_ids = model.generate(batch['input_ids'], max_length=max_length)

# Decode generated paraphrased text
generated_sentence = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)

print(generated_sentence[0])
