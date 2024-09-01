# equilibrium_composition
- ## problem
    メタンの水蒸気改質反応(S/C比 = 2)の平衡組成を各温度条件で求める.  
    温度Tは373.15 Kから1273.15 Kまで50.00 K刻み.  
    全圧P = 1 atmで定圧.  
    メタン1 molの転化率をxとする.  
    化学反応式
    $$
    \text{CH}_4 + 2\text{H}_2\text{O}(g) \rightleftharpoons 4\text{H}_2 + \text{CO}_2
    $$
    平衡定数と分圧の関係
    $$
    K_p = \frac{(P_{\text{H}_2})^4 \cdot P_{\text{CO}_2}}{P_{\text{CH}_4} \cdot (P_{\text{H}_2\text{O}})^2}
    $$
    温度ごとの平衡定数
    $$
    \ln(K_p) = 5.367841 \cdot \ln(T) - \frac{1.810169 \times 10^4}{T} - 16.46319 + 3.280842 \times 10^{-3} \cdot T - 2.894601 \times 10^{-6} \cdot T^2 + 6.645154 \times 10^{-10} \cdot T^3
    $$

- ## method
    非線形の一次元球根問題であるためNewton–Raphson method
