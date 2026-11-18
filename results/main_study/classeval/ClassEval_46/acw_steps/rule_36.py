class Interpolation:
    def __init__(self):
        pass

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        y_interp = []
        for xi in x_interp:
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i+1]:
                    yi = y[i] + (y[i+1] - y[i]) * (xi - x[i]) / (x[i+1] - x[i])
                    y_interp.append(yi)
                    break
        return y_interp
    
    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        z_interp = []
        for xi, yi in zip(x_interp, y_interp):
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i+1]:
                    for j in range(len(y) - 1):
                        if y[j] <= yi <= y[1+j]:
                            z00 = z[i][j]
                            z01 = z[i][1+j]
                            z10 = z[i+1][j]
                            z11 = z[i+1][1+j]
                            zi = (z00 * (x[i+1] - xi) * (y[1+j] - yi) +
                                  z10 * (xi - x[i]) * (y[1+j] - yi) +
                                  z01 * (x[i+1] - xi) * (yi - y[j]) +
                                  z11 * (xi - x[i]) * (yi - y[j])) / ((x[i+1] - x[i]) * (y[1+j] - y[j]))
                            z_interp.append(zi)
                            break
                    break
        return z_interp