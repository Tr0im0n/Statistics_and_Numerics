function [t, u] = rk4(t_interval, N_steps, u_initial, f)

   dt = (t_interval(2) - t_interval(1)) / N_steps;
   t = t_interval(1) : dt : t_interval(2);

   u = zeros(1, N_steps + 1);
   u(1) = u_initial;

   for n = 1 : N_steps

      k1 = f(t(n), u(n));
      k2 = f(t(n) + 0.5*dt, u(n) + 0.5*k1*dt);
      k3 = f(t(n) + 0.5*dt, u(n) + 0.5*k2*dt);
      k4 = f(t(n) + dt, u(n) + k3*dt);

      mean_slope = (k1 + 2*k2 + 2*k3 + k4)/6;

      u(n+1) = u(n) + mean_slope * dt;

   end

end
