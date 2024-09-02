import os
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# 微分方程式の定義
def coupled_oscillation_eq(t, y, M1, M2, K1, K2, K3):
    x1, x2, v1, v2 = y
    dx1dt = v1
    dx2dt = v2
    dv1dt = -(K1 + K2) / M1 * x1 + K2 / M1 * x2
    dv2dt = K2 / M2 * x1 - (K2 + K3) / M2 * x2
    return [dx1dt, dx2dt, dv1dt, dv2dt]

def main():
    # パラメータ設定
    M1 = 3.2
    M2 = 1.8
    K1 = 10.0
    K2 = 2.0
    K3 = 6.6

    # 初期条件: x1, x2, x1', x2'
    y0 = [-0.5, 4.0, 0.0, 0.0]

    t_span = (0.0, 100.0)

    sol = solve_ivp(coupled_oscillation_eq, t_span, y0, args=(M1, M2, K1, K2, K3), method='RK45', rtol=1e-10, atol=1e-5)

    plt.figure(figsize=(10, 6))
    plt.plot(sol.t, sol.y[0], label='x1 (M1)', color='blue')
    plt.plot(sol.t, sol.y[1], label='x2 (M2)', color='red')
    plt.grid(True)

    plt.xlabel('Time [s]')
    plt.ylabel('Position [m]')
    plt.legend()

    plt.figtext(0.5, 0.01, 'Coupled Oscillations', ha='center', fontsize=12)

    output_dir = "./coupled_oscillation/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file_path = os.path.join(output_dir, 'coupled_oscillation.png')
    plt.savefig(output_file_path, bbox_inches='tight')

if __name__ == "__main__":
    main()
