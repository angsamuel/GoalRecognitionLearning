maximize
0.25V(0,1) + 0.75V(0,2)
subject to
V(5,1) - 1F(5,1) - 0F(5,2) - V(4,1) <= 0
V(5,2) - 0F(5,1) - 1F(5,2) - V(4,2) <= 0
V(1,1) = 0
V(1,2) - 0F(1,1) - 1F(1,2) - V(3,2) <= 0
V(6,1) - 1F(6,1) - 0F(6,2) - V(7,1) <= 0
V(6,2) - 0F(6,1) - 1F(6,2) - V(7,2) <= 0
V(8,1) - 1F(8,1) - 0F(8,2) - V(2,1) <= 0
V(8,2) - 0F(8,1) - 1F(8,2) - V(2,2) <= 0
V(5,1) - 1F(5,1) - 0F(5,2) - V(6,1) <= 0
V(5,2) - 0F(5,1) - 1F(5,2) - V(6,2) <= 0
V(3,1) - 1F(3,1) - 0F(3,2) - V(4,1) <= 0
V(3,2) - 0F(3,1) - 1F(3,2) - V(4,2) <= 0
V(7,1) - 1F(7,1) - 0F(7,2) - V(6,1) <= 0
V(7,2) - 0F(7,1) - 1F(7,2) - V(6,2) <= 0
V(3,1) - 1F(3,1) - 0F(3,2) - V(1,1) <= 0
V(3,2) - 0F(3,1) - 1F(3,2) - V(1,2) <= 0
V(6,1) - 1F(6,1) - 0F(6,2) - V(0,1) <= 0
V(6,2) - 0F(6,1) - 1F(6,2) - V(0,2) <= 0
V(0,1) - 1F(0,1) - 0F(0,2) - V(6,1) <= 0
V(0,2) - 0F(0,1) - 1F(0,2) - V(6,2) <= 0
V(4,1) - 1F(4,1) - 0F(4,2) - V(3,1) <= 0
V(4,2) - 0F(4,1) - 1F(4,2) - V(3,2) <= 0
V(2,1) - 1F(2,1) - 0F(2,2) - V(8,1) <= 0
V(2,2) = 0
V(4,1) - 1F(4,1) - 0F(4,2) - V(5,1) <= 0
V(4,2) - 0F(4,1) - 1F(4,2) - V(5,2) <= 0
V(7,1) - 1F(7,1) - 0F(7,2) - V(8,1) <= 0
V(7,2) - 0F(7,1) - 1F(7,2) - V(8,2) <= 0
V(6,1) - 1F(6,1) - 0F(6,2) - V(5,1) <= 0
V(6,2) - 0F(6,1) - 1F(6,2) - V(5,2) <= 0
V(8,1) - 1F(8,1) - 0F(8,2) - V(7,1) <= 0
V(8,2) - 0F(8,1) - 1F(8,2) - V(7,2) <= 0
F(0,1) + F(0,2) = 1 
F(1,1) + F(1,2) = 1 
F(2,1) + F(2,2) = 1 
F(3,1) + F(3,2) = 1 
F(4,1) + F(4,2) = 1 
F(5,1) + F(5,2) = 1 
F(6,1) + F(6,2) = 1 
F(7,1) + F(7,2) = 1 
F(8,1) + F(8,2) = 1 
bounds
V(4,2)  free 
F(8,2)  >= 0
F(1,2)  >= 0
V(8,1)  free 
V(0,2)  free 
V(5,2)  free 
V(2,2)  free 
V(3,2)  free 
F(S0,2)  >= 0
F(0,2)  >= 0
F(S0,1)  >= 0
F(2,1)  >= 0
V(6,1)  free 
V(5,1)  free 
F(3,1)  >= 0
F(6,2)  >= 0
F(7,2)  >= 0
V(1,2)  free 
F(5,1)  >= 0
V(0,1)  free 
F(1,1)  >= 0
V(7,1)  free 
V(2,1)  free 
F(0,1)  >= 0
V(4,1)  free 
F(8,1)  >= 0
V(3,1)  free 
F(5,2)  >= 0
F(2,2)  >= 0
F(7,1)  >= 0
V(6,2)  free 
F(3,2)  >= 0
V(7,2)  free 
F(4,2)  >= 0
V(8,2)  free 
F(6,1)  >= 0
V(1,1)  free 
F(4,1)  >= 0
