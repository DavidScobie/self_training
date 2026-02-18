%make sure to enter theta=x (where 0<x<90) in the command line first
%This opens simulink and runs cannon6 model with parameters defined in the
%model
s = sim('cannon6','StopTime','25','MaxStep','0.01'); %run simulink model
r = s.get('simout'); %get results of simulink into matlab
x = r.Data(:,1); 
y = r.Data(:,2); 
plot(x,y) 
axis([0 400 -10 200])
xlabel('x')
ylabel('y')
title('cannonball trajectory')