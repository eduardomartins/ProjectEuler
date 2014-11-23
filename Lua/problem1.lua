
function sum_number(a1, an, n)
    return ((a1 + an) * n)/2
end

function last_multiple (num, max)
    if max >= num then
        if max % num == 0 then
            return max
        else
            return last_multiple(num, max - 1)
        end
    else
        return num
    end
end

function main()
    n1, n2, n3, max = 3, 5, 15, 999
    l1, l2, l3 = last_multiple(n1, max), last_multiple(n2, max), last_multiple(n3, max)
    print("Result: ", sum_number(n1, l1, l1/n1) + sum_number(n2, l2, l2/n2) - sum_number(n3, l3, l3/n3))
end

main()