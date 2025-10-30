
clear;

format compact

%{
One file can only have 1 function. 
But 1 function can apperantly have multiple functions inside of it. 
This makes it so i can do all my work in 1 file, which i prefer. 
I can make a function, call it above the function, and comment out the
function call whenn I am done with it.

ex2 and ex3 are earler excercises from the tutorial. 
ex4 is the graded excercise. 
I have function to calculate certain things.
Initially I made them using loops. 
Later I have made functions, just dot producting the arrays and taking the
sum. 

%}

main()
function main()

    % ex2()
    function ex2()
        n = 8;
        v = [0.5, 2, 3,4,6,8,10,11];
        p = [336.0, 294.4, 266.4, 260.8, 260.5, 249.6, 193.6, 165.6];
        dv = v(2:end) - v(1:end-1);

        total = 0.0;

        for i = 1 : n-1
            temp = 0.5 * (p(i) + p(i+1)) * dv(i);
            total = total + temp;
        end

        disp(total);

    end

    % ex3()
    function ex3()
        v = [0.5, 2, 3,4,6,8,10,11];
        p = [336.0, 294.4, 266.4, 260.8, 260.5, 249.6, 193.6, 165.6];

        total = trapezoid(v, p);

        disp(total);

    end

    function total = trapezoidLoop(t, f)
        n = size(t, 2);
        dt = t(2:end) - t(1:end-1);
        f_pairs = f(2:end) + f(1:end-1);
        total = 0.0;

        for i = 1 : n-1
            temp = 0.5 * f_pairs(i) * dt(i);
            total = total + temp;
        end
    end

    function total = trapezoid(t, f)
        n = size(t, 2);
        dt = t(2:end) - t(1:end-1);
        f_pairs = f(2:end) + f(1:end-1);

        array = 0.5 * dt.*f_pairs;
        total = sum(array) ;
    end

    function result = lineOfActionLoop(heights, forces, forceResultant)
        n = size(heights, 2);
        dh = heights(2:end) - heights(1:end-1);
        forcePairs = forces(2:end) + forces(1:end-1);
        heightPairs = heights(2:end) + heights(1:end-1);
        
        total = 0;

        for i = 1 : n-1
            temp = 0.25 * forcePairs(i) * heightPairs(i) * dh(i);
            total = total + temp;
        end
        result = total / forceResultant;
    end


    function result = lineOfAction(heights, forces, forceResultant)
        dh = heights(2:end) - heights(1:end-1);
        forcePairs = forces(2:end) + forces(1:end-1);
        heightPairs = heights(2:end) + heights(1:end-1);
        
        array = 0.25 * forcePairs * heightPairs * dh;
        total = sum(array);
        result = total / forceResultant;
    end

    ex4()
    function ex4()
        forces = [0 30 40 40 50 50 60 80 100];
        heights = [0 50 100 150 225 300 375 450 600];

        forceResultant = trapezoid(heights, forces)
        myLineOfAction = lineOfAction(heights, forces, forceResultant)

    end



end

