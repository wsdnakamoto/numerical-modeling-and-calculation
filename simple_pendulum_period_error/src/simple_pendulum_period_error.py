import os
import numpy as np
from scipy.integrate import solve_ivp

# 微分方程式の定義
def pendulum_eq(t, y, G, L):
    theta, omega = y
    dydt = [omega, -(G / L) * np.sin(theta)]
    return dydt

# 周期の誤差を計算する関数
def calc_period_error(initial_deg, G, L, file):
    t_span = [0, 100.0]
    y0 = [np.radians(initial_deg), 0.0]

    sol = solve_ivp(pendulum_eq, t_span, y0, args=(G, L), method='RK45', rtol=1e-10, atol=1e-5)

    cycles = 5
    cycle_count = 0
    period_sum = 0.0
    period_start = -1.0

    for i in range(1, len(sol.t)):
        if sol.y[0, i-1] < 0 <= sol.y[0, i] and sol.y[1, i] > 0:
            if period_start < 0:
                period_start = sol.t[i]
            else:
                period = sol.t[i] - period_start
                period_sum += period
                cycle_count += 1
                period_start = sol.t[i]

            if cycle_count >= cycles:
                break

    if cycle_count > 0:
        average_period = period_sum / cycle_count
        approximate_period = 2 * np.pi * np.sqrt(L / G)
        error_percentage = abs((average_period - approximate_period) / approximate_period) * 100.0
        file.write(f"{initial_deg:5}°{error_percentage:20.4f} %\n")
    else:
        file.write(f"{initial_deg:5}°   計算に失敗\n")

def main():
    G = 9.80665
    L = 2.00000

    output_dir = "./simple_pendulum_period_error/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file_path = os.path.join(output_dir, 'simple_pendulum_period_error_result.txt')
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write("振出角度 [deg] 周期Tの誤差 [%]\n")
        for initial_deg in range(15, 91, 15):
            calc_period_error(initial_deg, G, L, file)

if __name__ == "__main__":
    main()
