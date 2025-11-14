clear;
format compact;

main()
function main

    % ex10();
    function ex10
        
        L = 1;
        S = 100;
        N = S + 1;
        dx = L/S;
        p = 0.1;
        x = 0:dx:L;
        c0 = 1;
        c1 = 0;

        u_exact = c0 + (c1-c0) * (1-exp(p*x/dx))/(1-exp(S*p));

        A = zeros(N, N);
        A(1, 1) = 1;
        A(N, N) = 1;
        for a = 2 : S
            A(a, a-1) = 1+p;
            A(a, a) = -(2+p);
            A(a, a+1) = 1;
        end

        % u = zeros(N, 1);
        b = zeros(N, 1);
        b(1) = c0;
        b(N) = c1;

        u = A \ b;

        h1 = figure;
        plot(x, u, 'o')
        hold on;
        plot(x, u_exact, '-')
        grid on;
        title("Wanted solution");
        hold off;
        waitfor(h1);

    end

    % ex11()
    function ex11(A, S)
        
        L = 1;
        N = S + 1;
        dx = L/S;
        p = 0.1;
        x = 0:dx:L;
        c0 = 1;
        c1 = 0;

        u_exact = c0 + (c1-c0) * (1-exp(p*x/dx))/(1-exp(S*p));

        % u = zeros(N, 1);
        b = zeros(N, 1);
        b(1) = c0;
        b(N) = c1;

        u = A \ b;

        h1 = figure;
        plot(x, u, 'o')
        hold on;
        plot(x, u_exact, '-')
        grid on;
        title("Wanted solution");
        hold off;
        waitfor(h1);

    end
        
    ex12()
    function ex12
        S = 100;
        p = 1.9;

        A = diagonal_matrix(S, 1, -2+p, 1-p);

        ex11(A, S)

    end

end
