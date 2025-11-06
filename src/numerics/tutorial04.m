
clear;

format compact

main()
function main

    % ex6();
    function ex6
        % assignment 2
        x1 = 1;
        % v1 = 0;
        t1 = 0;
        % a1 = 0;

        steps = 100;
        t_max = 10;

        dt = (t_max-t1)/steps; % 0.1
        t = t1:dt:t_max;

        % a = zeros(1, steps+1);
        v = zeros(1, steps+1);
        x = zeros(1, steps+1);

        x(1) = x1;

        f_a = @(x) -x;

        for n = 1:steps
            % a(n+1) = a(n) - x(n) * dt;
            % v(n+1) = v(n) + 0.5*(a(n) + a(n+1))*dt;

            x(n+1) = x(n) + v(n)*dt + 0.5*f_a(x(n))*dt*dt;
            v(n+1) = v(n) + 0.5*(f_a(x(n)) + f_a(x(n+1)))*dt;
        end

        x_analytical = cos(t);

        h1 = figure;
        plot(t, x, 'o')
        hold on;
        plot(t, x_analytical, '-')
        grid on;
        title("Wanted solution");
        hold off;
        waitfor(h1);

    end

    % ex7();
    function ex7
        % my method
        x1 = 1;
        % v1 = 0;
        t1 = 0;
        % a1 = 0;

        steps = 100;
        t_max = 10;

        dt = (t_max-t1)/steps; % 0.1
        t = t1:dt:t_max;

        a = zeros(1, steps+1);
        v = zeros(1, steps+1);
        x = zeros(1, steps+1);

        x(1) = x1;

        f_a = @(x) -x;

        for n = 1:steps
            a(n+1) = f_a(x(n));
            v(n+1) = v(n) + a(n+1)*dt;
            x(n+1) = x(n) + v(n+1)*dt;
        end

        x_analytical = cos(t);

        h2 = figure;
        plot(t, x, 'o')
        hold on;
        plot(t, x_analytical, '-')
        grid on;
        title("Isn't this easier?");
        hold off;
        waitfor(h2);

    end

    ex8() 
    function ex8
        % runge kutta
        t_interval = [0 100];
        N_steps = 100;
        u_initial = 90;

        Ta = 20;
        k = 0.025;

        f = @(t, T) -k*(T-Ta);

        [t, u] = rk4(t_interval, N_steps, u_initial, f);

        u_exact = Ta + (u_initial-Ta) * exp(-k*t);

        plot(t, u, 'o')
        hold on
        plot(t, u_exact, '-')
        grid on;
        hold off
        
    end

end
