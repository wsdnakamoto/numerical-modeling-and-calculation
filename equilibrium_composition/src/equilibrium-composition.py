import numpy as np
from scipy.optimize import newton
import os

output_dir = "./equilibrium_composition/output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_file_path = os.path.join(output_dir, "equilibrium_composition_result.txt")

# 平衡定数K_pを計算する関数
def calculate_equilibrium_constant(T):
    return np.exp(5.367841 * np.log(T) - (1.810169e4) / T - 1.646319e1 + 3.280842e-3 * T - 2.894601e-6 * T**2 + 6.645154e-10 * T**3)

# メタン水蒸気改質反応の平衡式
def reforming_equation(x, K_p):
    return 64 * x**5 + K_p * (4 * x**5 - 15 * x**3 + 5 * x**2 + 15 * x - 9)

# 導関数の定義
def reforming_equation_derivative(x, K_p):
    return 320 * x**4 + K_p * (20 * x**4 - 45 * x**2 + 10 * x + 15)

# 温度範囲とステップの設定
T_min = 373.15
T_max = 1273.15
T_step = 50.0

# 出力ファイルを開いて書き込み
with open(output_file_path, "w") as f:
    # 解析を行う温度範囲でループ
    for T in np.arange(T_min, T_max + T_step, T_step):
        K_p = calculate_equilibrium_constant(T)

        f.write(f"Temperature: {T:.2f} K\n")
        f.write(f"Equilibrium constant: {K_p:.2e}\n")

        # Newton-Raphson法で解を求める
        initial_conversion = 0.4  # 初期値
        methane_conversion = newton(reforming_equation, initial_conversion, fprime=reforming_equation_derivative, args=(K_p,), tol=1e-7, maxiter=100)

        # 平衡組成の計算
        m_H2 = 4 * methane_conversion / (3 + 2 * methane_conversion) * 100
        m_CO2 = methane_conversion / (3 + 2 * methane_conversion) * 100
        m_CH4 = (1 - methane_conversion) / (3 + 2 * methane_conversion) * 100
        m_H2O = (2 - 2 * methane_conversion) / (3 + 2 * methane_conversion) * 100

        f.write("Converged:\n")
        f.write(f"Methane Conversion (x): {methane_conversion:.4f}\n")
        f.write(f"m_H2: {m_H2:.2f}%, m_CO2: {m_CO2:.2f}%, m_CH4: {m_CH4:.2f}%, m_H2O: {m_H2O:.2f}%\n")
        f.write("----------------------------------------------------------\n")
