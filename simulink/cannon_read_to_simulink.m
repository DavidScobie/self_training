%This opens simulink and runs cannon7 using initial parameters defined in
%this MATLAB script

%Input parameters
theta = 35; %elevation angle in degrees
g = -9.81; %gravity
mass = 10; %cannonball mass
drag_coef = -0.02; %coefficient of drag from air resistance
u = 100; %initial speed of cannonball

u_vec = u * [cosd(theta) sind(theta)]; %initial velocity vector [x,y] of cannonball

s = sim('cannon7','StopTime','25','MaxStep','0.01'); %run simulink model
r = s.get('simout'); %get results of simulink into matlab
x = r.Data(:,1); 
y = r.Data(:,2); 
plot(x,y) 
axis([0 400 -10 200])
xlabel('x')
ylabel('y')
title('cannonball trajectory')