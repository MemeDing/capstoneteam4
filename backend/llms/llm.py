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
    load_in_4bit=True
)

model = torch.compile(model)

torch.set_num_threads(2)

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**inputs, do_sample=True)
    return tokenizer.decode(output[0], skip_special_tokens=True)