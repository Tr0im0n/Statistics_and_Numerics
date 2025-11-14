function A = diagonal_matrix(S, lower_diag, main_diag, upper_diag)
    N = S + 1;

    A = zeros(N, N);
    A(1, 1) = 1;
    A(N, N) = 1;
    for a = 2 : S
        A(a, a-1) = lower_diag;
        A(a, a) = main_diag;
        A(a, a+1) = upper_diag;
    end

end

