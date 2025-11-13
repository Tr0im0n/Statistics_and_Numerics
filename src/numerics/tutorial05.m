clear;
format compact;

main()
function main

    ex9();
    function ex9
        H = 1;
        S = 100;
        N = S + 1;
        dy = H/S;
        f = -1;
        y = 0:dy:H;
        u_bottom = 0;
        u_top = 0;

        u_exact = 0.5 * f * H *(y.^2 - y);

        A = get_matrix1(N);

        u = zeros(N, 1);
        b = ones(N, 1) * f * dy*dy;

        b(1) = u_bottom;
        b(N) = u_top;

        u = A \ b;

        h1 = figure;
        plot(u, y, 'o')
        hold on;
        plot(u_exact, y, '-')
        grid on;
        title("Wanted solution");
        hold off;
        waitfor(h1);


    end





    function A = get_matrix1(N)

        A = zeros(N, N);

        for i = 2 : N-1
        %     % A(i, i-1) = 1;
        %     % A(i, i) = -2;
        %     % A(i, i+1) = 1;
            A(i, i-1:i+1) = [1, -2, 1];
        end

        % A = A + diag(ones(N-1, 1), -1);
        % A = A + diag(-2 * ones(N, 1), 0);
        % A = A + diag(ones(N-1, 1), 1);

        A(1, 1) = 1;
        A(N, N) = 1;
    end




end
