import torch

ten_x = torch.tensor([[1,2],[3,4]],dtype=torch.long)

ten_y = torch.tensor([[2,4],[6,8]],dtype=torch.long)

sum_tensor = ten_x + ten_y

print(sum_tensor)

ten_z = torch.tensor([[1,1],[1,1]],dtype=torch.long)

print(sum(ten_x, ten_z))