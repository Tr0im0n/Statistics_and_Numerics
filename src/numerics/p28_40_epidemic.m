% Chapra & Canale: problem 28.40 page 851
clear;

t_interval = [0 30];
N_steps = 1000;
dt = (t_interval(2) - t_interval(1))/N_steps;

S = zeros(1, N_steps + 1);
I = zeros(1, N_steps + 1);
R = zeros(1, N_steps + 1);

S(1) = 999;
I(1) = 1;
R(1) = 0;

% functions
a = 1.002/7;
r = 0.15;
f_S = @(S, I) -a*S*I;
f_R = @(I) r*I;
f_I = @(S, I) a*S*I -r*I;


for i = 1 : N_steps
    S(i+1) = S(i) + f_S(S(i), I(i)) * dt;
    I(i+1) = I(i) + f_I(I(i), I(i)) * dt;
    R(i+1) = R(i) + f_R(R(i), I(i)) * dt;
end
