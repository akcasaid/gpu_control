import torch


if torch.cuda.is_available():
    print("GPU is available.")
    device = torch.device("cuda")  # CUDA cihazını tanımla
    print(f"GPU Name: {torch.cuda.get_device_name(device)}")
    print(f"Total memory: {torch.cuda.get_device_properties(device).total_memory / (1024 ** 3):.2f} GB")
else:
    print("GPU is not available.")
