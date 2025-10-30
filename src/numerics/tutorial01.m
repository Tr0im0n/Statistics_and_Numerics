
clear;

format compact

main()
function main()
    
    % ex1()
    function ex1()
        S = 4;
        N = S + 1;
        
        t_1 = 0.;
        t_N = 1.;
        dt = (t_N - t_1)/S;
        t = t_1 : dt : t_N;
        
        f = t.^4;
        
        L_slice = zeros(1, S);
        L_total = 0.;
        
        for n = 1 : S
            L_slice(n) = f(n) * dt;
            L_total = L_total + L_slice(n);
        end
        
        disp(L_total)
    end


end


% path
