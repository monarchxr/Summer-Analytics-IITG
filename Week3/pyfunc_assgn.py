def slope_estimation(count, sum_x, sum_y, sum_x_y, sum_x_square):
    # we need to compute a and b
    # a = slope
    # b = intercept
    # y = ax + b

    if count < 1:
        return(None, None)
    
    mean_x = sum_x/count
    expected_sum_sq = count*mean_x*mean_x

    if abs(sum_x_square - expected_sum_sq) < 1e-8:
        return(None, None)
    
    denom = count*sum_x_square - (sum_x*sum_x)

    a = (count*sum_x_y - sum_x*sum_y)/denom
    b = (sum_y - a*sum_x)/count

    return(round(a,8), round(b,8))