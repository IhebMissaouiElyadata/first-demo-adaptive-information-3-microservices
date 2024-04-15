from transformers import pipeline
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import BitsAndBytesConfig
import torch

nf4_config = BitsAndBytesConfig(
   load_in_4bit=True,
   bnb_4bit_quant_type="nf4",
   bnb_4bit_use_double_quant=True,
   bnb_4bit_compute_dtype=torch.bfloat16
)
# Specify GPU device (replace with specific GPU index if using multiple GPUs)
device = "cuda:0" if torch.cuda.is_available() else "cpu"

# Model and tokenizer names (replace with desired model ID)
model_name = "unsloth/OpenHermes-2.5-Mistral-7B-bnb-4bit"
tokenizer_name = model_name

# Download model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True,
    quantization_config=nf4_config,  # Include quantization config if using nf4
    device_map="auto",  # Removed for explicit GPU assignment
)
model.to(device)