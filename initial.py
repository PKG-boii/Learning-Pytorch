import torch
# print(f"PyTorch Version: {torch.__version__}")
# print(f"CUDA Available: {torch.cuda.is_available()}")
# if torch.cuda.is_available():
#     print(f"CUDA Version: {torch.version.cuda}")
#     print(f"GPU Name: {torch.cuda.get_device_name(0)}")
# vector = torch.tensor([1, 2, 3])
# matrix = torch.tensor([[1,2,3],
#                        [4,5,6]])
# print(matrix)
random_tensor = torch.rand(2, 4, 3)

print(random_tensor)
start_end_tensor = torch.arange(0, 101, 2)
print(start_end_tensor)
tensor_dtype = torch.tensor([1.2,2.2,3.1])
print(tensor_dtype.dtype)
