# Write a function to calculate the Mean Difference of nth Root Error:


def md_nre(y, y_hat, n, p):
    return (y**(1/n) - y_hat**(1/n))**p


examples = [
    (100, 99.5),
    (50, 49.5),
    (20, 19.5),
    (5.5, 5.0),
    (1.0, 0.5),
    (0.6, 0.1)
]
n = 2
p = 1
for y, y_hat in examples:
    result = md_nre(y, y_hat, n, p)
    print(f"MD_nRE(y={y}, y_hat={y_hat}, n={n}, p={p}) = {result}")
