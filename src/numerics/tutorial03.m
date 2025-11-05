
clear;

format compact

main()
function main

    ex5();
    function ex5
        dt = 1;
        steps = 100;
        t = 0:100:dt;
        Ta = 20;
        T0 = 90;
        k = 0.025;

        f = @(t, T) -k*(T-Ta);

        T = zeros(1, steps + 1);
        T(1) = T0;

        for i = 1 : steps
            T(i+1) = T(i) + f(t(i), T(i)) * dt;
        end

        T_exact = Ta + (T0-Ta) * exp(-k*t);

        plot(t, T, '-')
        hold on
        plot(t, T_exact, 'o')
        hold off

    end

end
