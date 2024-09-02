# equilibrium_composition(平衡組成)

- ## 問題
    メタンの水蒸気改質反応(S/C比 = 2)の平衡組成を各温度条件で求める.  
    温度Tは373.15 Kから1273.15 Kまで50.00 K刻み.  
    全圧P = 1 atmで定圧.  
    メタン1 molの転化率をxとする.  
    化学反応式:
    ```math
    \text{CH}_4 + 2\text{H}_2\text{O}(g) \rightleftharpoons 4\text{H}_2 + \text{CO}_2
    ```
    平衡定数と分圧の関係:
    ```math
    K_p = \frac{(P_{\text{H}_2})^4 \cdot P_{\text{CO}_2}}{P_{\text{CH}_4} \cdot (P_{\text{H}_2\text{O}})^2}
    ```
    温度ごとの平衡定数:
    ```math
    \ln(K_p) = 5.367841 \cdot \ln(T) - \frac{1.810169 \times 10^4}{T} - 16.46319 + 3.280842 \times 10^{-3} \cdot T - 2.894601 \times 10^{-6} \cdot T^2 + 6.645154 \times 10^{-10} \cdot T^3
    ```

- ## タイプ/数値解法
    非線形の一次元球根問題/Newton–Raphson法  

# simple_pendulum_period_error(単振り子の周期の誤差)

- ## 問題
    式(1)の単振り子の運動の周期を数値計算と式(2)の近似による計算で求め, その誤差を求める. 振出角度を15°から90°まで15°刻みで変化させ各振出角度で求めることで誤差の変化を確認する.
    ```math
    ml\ddot{\theta} = -mg\sin\theta \quad \text{...(1)}
    ```
    ```math
    \sin\theta = \theta \quad \text{...(2)}
    ```

- ## タイプ/数値解法
    θをωと置くことで2階常微分方程式から2元1階常微分方程式になる  
    埋め込み型Runge-Kutta法(RK45)  
