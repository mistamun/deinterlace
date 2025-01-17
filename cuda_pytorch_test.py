import torch

if torch.cuda.is_available():
    print('CUDA Available') 
    print(f'Device ID: {torch.cuda.current_device()} Device Name: {torch.cuda.get_device_name(torch.cuda.current_device())}')
else:
    print('CUDA Unavailable')
