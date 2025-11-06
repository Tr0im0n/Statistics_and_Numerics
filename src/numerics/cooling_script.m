clear;

t_interval = [0 100];
N_steps    = 100;

T_initial = 90.;

% Integrand
k = 0.25;
T_a = 20.;
f = @(t, T) -k*(T - T_a);

[t, T] = rk4(t_interval, N_steps, T_initial, f);

plot(t, T, 'o', t, cos(t), '-');

T_exact = T_a + (T_initial - T_a)*exp(-k*t);

plot(t, T_exact, '-', t, T, 'o'); %ylim([0 T_initial]);
