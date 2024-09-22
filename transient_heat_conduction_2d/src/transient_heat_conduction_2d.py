import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import os

# 材料特性
k = 45 # 熱伝導率 [W/m·K]
cp = 470 # 比熱容量 [J/kg·K]
rho = 7850 # 密度 [kg/m³]
alpha = k / (rho * cp) # 熱拡散率 [m²/s]

# 計算領域
Lx = 0.1 # x方向の長さ [m]
Ly = 0.2 # y方向の長さ [m]
Nx = 51 # x方向のメッシュ数
Ny = 101 # y方向のメッシュ数
dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)

# 時間設定
dt = 0.1 # 時間刻み [s]
t_max = 100.0  # シミュレーション時間 [s]
nt = int(t_max / dt)

x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

T_initial = 373.15  # 初期温度 100℃ = 373.15 K
T_boundary = 298.15  # 境界温度 25℃ = 298.15 K

T = np.full((Ny, Nx), T_initial)

# 境界条件の適用関数
def apply_boundary_conditions(T):
    T[0, :] = T_boundary    # y=0 (下側境界)
    T[-1, :] = T_boundary   # y=Ly (上側境界)
    T[:, 0] = T_boundary    # x=0 (左側境界)
    T[:, -1] = T_boundary   # x=Lx (右側境界)
    return T

T = apply_boundary_conditions(T)

# 各時間ステップごとの温度分布を保存
T_list = [T.copy()]

# 結果を保存する間隔を設定(ここで指定したステップごとに保存)
save_interval = 1

def RK4_step(T, dt):
    Tn = T.copy()
    i_start = 1
    i_end = Ny - 1
    j_start = 1
    j_end = Nx - 1

    # k1
    T_xx = (Tn[i_start:i_end, j_start+1:j_end+1] - 2*Tn[i_start:i_end, j_start:j_end] +
            Tn[i_start:i_end, j_start-1:j_end-1]) / dx**2
    T_yy = (Tn[i_start+1:i_end+1, j_start:j_end] - 2*Tn[i_start:i_end, j_start:j_end] +
            Tn[i_start-1:i_end-1, j_start:j_end]) / dy**2
    k1 = alpha * (T_xx + T_yy)

    # T1 = Tn + 0.5 * dt * k1
    T1 = Tn.copy()
    T1[i_start:i_end, j_start:j_end] += 0.5 * dt * k1
    T1 = apply_boundary_conditions(T1)

    # k2
    T_xx = (T1[i_start:i_end, j_start+1:j_end+1] - 2*T1[i_start:i_end, j_start:j_end] +
            T1[i_start:i_end, j_start-1:j_end-1]) / dx**2
    T_yy = (T1[i_start+1:i_end+1, j_start:j_end] - 2*T1[i_start:i_end, j_start:j_end] +
            T1[i_start-1:i_end-1, j_start:j_end]) / dy**2
    k2 = alpha * (T_xx + T_yy)

    # T2 = Tn + 0.5 * dt * k2
    T2 = Tn.copy()
    T2[i_start:i_end, j_start:j_end] += 0.5 * dt * k2
    T2 = apply_boundary_conditions(T2)

    # k3
    T_xx = (T2[i_start:i_end, j_start+1:j_end+1] - 2*T2[i_start:i_end, j_start:j_end] +
            T2[i_start:i_end, j_start-1:j_end-1]) / dx**2
    T_yy = (T2[i_start+1:i_end+1, j_start:j_end] - 2*T2[i_start:i_end, j_start:j_end] +
            T2[i_start-1:i_end-1, j_start:j_end]) / dy**2
    k3 = alpha * (T_xx + T_yy)

    # T3 = Tn + dt * k3
    T3 = Tn.copy()
    T3[i_start:i_end, j_start:j_end] += dt * k3
    T3 = apply_boundary_conditions(T3)

    # k4
    T_xx = (T3[i_start:i_end, j_start+1:j_end+1] - 2*T3[i_start:i_end, j_start:j_end] +
            T3[i_start:i_end, j_start-1:j_end-1]) / dx**2
    T_yy = (T3[i_start+1:i_end+1, j_start:j_end] - 2*T3[i_start:i_end, j_start:j_end] +
            T3[i_start-1:i_end-1, j_start:j_end]) / dy**2
    k4 = alpha * (T_xx + T_yy)

    # 次の時間ステップの温度計算
    T_next = Tn.copy()
    T_next[i_start:i_end, j_start:j_end] += (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

    # 境界条件の適用
    T_next = apply_boundary_conditions(T_next)

    return T_next

# 時間ループ
for n in range(nt):
    T = RK4_step(T, dt)

    # 結果の保存
    if (n + 1) % save_interval == 0:
        T_list.append(T.copy())

# gifのフレーム数
num_frames = len(T_list)

# 図のサイズを正方形に設定
fig_size = 12
fig, ax = plt.subplots(figsize=(fig_size, fig_size))

# カラーマップの設定
cmap = plt.get_cmap('jet')

# カラーバーの範囲を設定
vmin = T_boundary # 298.15 K
vmax = T_initial # 373.15 K

# 初期の温度分布を表示
im = ax.imshow(T_list[0], extent=[0, Lx, 0, Ly], origin='lower', cmap=cmap, vmin=vmin, vmax=vmax)

ax.set_aspect('equal')

# 図のアスペクト比
data_aspect = Ly / Lx

axes_height = 0.9
axes_width = axes_height / data_aspect

# 左右の余白を計算
left = (1.0 - axes_width) / 2.0
bottom = (1.0 - axes_height) / 2.0

ax.set_position([left, bottom, axes_width, axes_height])

cbar = fig.colorbar(im, ax=ax)
cbar.set_label('Temperature [K]', fontsize=12)

ax.set_xlabel('x [m]', fontsize=12)
ax.set_ylabel('y [m]', fontsize=12)
ax.set_title('Time = 0.00 s', fontsize=14)

def update_plot(frame):
    T_data = T_list[frame]
    im.set_data(T_data)
    current_time = frame * dt
    ax.set_title(f'Time = {current_time:.2f} s', fontsize=14)
    return im,

ani = animation.FuncAnimation(fig, update_plot, frames=num_frames, interval=1000/30, blit=False)

output_dir = './transient_heat_conduction_2d/output'
os.makedirs(output_dir, exist_ok=True)

save_path = os.path.join(output_dir, 'transient_heat_conduction_2d.gif')

ani.save(save_path, writer='pillow', fps=30)
