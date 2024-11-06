# coupled_oscillation(2体連成振動)

- ## 条件
    固定壁間で2つの質点が3本のばねで連結された2体連成振動の運動を調べる. 運動方程式は以下の2式になる.
    ```math
    m_1\ddot{x}_1 = -k_1 x_1 + k_2 (x_2 - x_1)
    ```
    ```math
    m_2\ddot{x}_2 = -k_3 x_2 - k_2 (x_2 - x_1)
    ```

- ## タイプ/数値解法
    xの時間微分を別の変数でそれぞれ置くことで2元2階常微分方程式から4元1階常微分方程式になる.
    埋め込み型Runge-Kutta法(RK45)  

# equilibrium_composition(平衡組成)

- ## 条件
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

- ## 条件
    式(1)の単振り子の運動の周期を数値計算と式(2)の近似による計算で求め, その誤差を求める. 振出角度を15°から90°まで15°刻みで変化させ各振出角度で求めることで誤差の変化を確認する.
    ```math
    ml\ddot{\theta} = -mg\sin\theta \quad \text{...(1)}
    ```
    ```math
    \sin\theta = \theta \quad \text{...(2)}
    ```

- ## タイプ/数値解法
    θをωと置くことで2階常微分方程式から2元1階常微分方程式になる.  
    埋め込み型Runge-Kutta法(RK45)

# semi_infinite_solid_heat_conduction(半無限体の非定常熱伝導)

- ## 条件
  建物のコンクリート壁が日射によって熱せられ, その内部が55 ℃(=328.15 K)で均一.
  その後20 ℃(=293.15 K)の雨が1時間にわたって降った.
  壁面から0.05 mの位置の温度はいくつか.  
  ディクリレ条件で考える. 壁面の温度は20 ℃.
  各物性値はコードを参照.  
  温度分布の時間変化を調べる為の1次元の非定常熱伝導方程式は式(1)であり, 中心差分により右辺の項はそれぞれ式(2)になり式(1)は式(3)になる. これをRunge-Kutta法で数値計算する.  
  もう一方で, 壁を半無限体と仮定しガウスの誤差関数を用いて温度を求める(式(4)).
  ```math
  \frac{\partial T}{\partial t} = \alpha \left( \frac{\partial^2 T}{\partial x^2} \right) \quad \text{...(1)}
  ```
  ```math
  \frac{\partial^2 T}{\partial x^2} \approx \frac{T_{i+1} - 2T_{i} + T_{i-1}}{\Delta x^2} \quad \text{...(2)}
  ```
  ```math 
  \frac{\partial T}{\partial t} = \alpha \left( \frac{T_{i+1} - 2T_{i} + T_{i-1}}{\Delta x^2} \right) \quad \text{...(3)}
  ```
  ```math
  \frac{T - T_0}{T_i - T_0} = \frac{2}{\sqrt{\pi}} \int_0^{\frac{x}{2\sqrt{\alpha t}}} e^{-\eta^2} \, \mathrm{d}\eta = \text{erf} \left( \frac{x}{2\sqrt{\alpha t}} \right) \quad \text{...(4)}
  ```
- ## タイプ/数値解法
  2階偏微分方程式(1次元の非定常熱伝導方程式)/中心差分とRunge-Kutta法  
  半無限体と仮定しガウスの誤差関数で温度を調べる.  

# transient_heat_conduction_2d(2次元の非定常熱伝導)

- ## 条件
  境界の温度が298.15 Kで固定, 内部の温度が373.15 Kで一様の金属(縦0.2 m, 横0.1 m)における温度分布の時間変化について調べる.
  温度分布の時間変化を調べる為の2次元の非定常熱伝導方程式は式(1)であり, 中心差分により右辺の項はそれぞれ式(2), (3)になり式(1)は式(4)になる. これをRunge-Kutta法で数値計算する.
  ```math
  \frac{\partial T}{\partial t} = \alpha \left( \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} \right) \quad \text{...(1)}
  ```
  ```math
  \frac{\partial^2 T}{\partial x^2} \approx \frac{T_{i+1,j} - 2T_{i,j} + T_{i-1,j}}{\Delta x^2} \quad \text{...(2)}
  ```
  ```math
  \frac{\partial^2 T}{\partial y^2} \approx \frac{T_{i,j+1} - 2T_{i,j} + T_{i,j-1}}{\Delta y^2} \quad \text{...(3)}
  ```
  ```math 
  \frac{\partial T}{\partial t} = \alpha \left( \frac{T_{i+1,j} - 2T_{i,j} + T_{i-1,j}}{\Delta x^2} + \frac{T_{i,j+1} - 2T_{i,j} + T_{i,j-1}}{\Delta y^2} \right) \quad \text{...(4)}
  ```
    
- ## タイプ/数値解法
  2階偏微分方程式(2次元の非定常熱伝導方程式)/中心差分とRunge-Kutta法  
