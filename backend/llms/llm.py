from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# TODO: Insert Open-LLaMa model
model_name = "openlm-research/open_llama_3b"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load model on CPU (no quantization needed)
#model = AutoModelForCausalLM.from_pretrained(model_name, device_map="cpu", torch_dtype=torch.float16)

# QLoRA model (4-bit quantized for limited VRAM)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
).to("cuda:0")

#model = torch.compile(model)

#torch.set_num_threads(2)

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", max_length=2048, truncation=True).to("cuda:0")
    output = model.generate(**inputs, max_length=2048)
    return tokenizer.decode(output[0], skip_special_tokens=True)