--
-- Created by IntelliJ IDEA.
-- User: Eduardo Sant' Anna Martins
-- Date: 04/01/15
-- Time: 21:27
-- To change this template use File | Settings | File Templates.
--

function sum_number(n)
    return ((1 + n) * n)/2
end

function sum_squares(n)
    return (n * (n + 1) * (2 * n + 1))/6
end

function main()
    last = 100
    sum1 = sum_squares(last)
    sum2 = sum_number(last)
    sum2 = sum2 * sum2
    print(sum2, " - ", sum1, " = ", sum2 - sum1)
end

main()
