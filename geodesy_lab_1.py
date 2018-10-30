from math import *

def ToDoubleDegree(angle, minutes, seconds):
    d_angle = angle + minutes/60 + seconds/3600
    return d_angle


def ToRadian(d_angle):
    r_angle = pi * d_angle/180
    return r_angle



    
variant = 19
# Большая полуось
a_m = 6378245
alpha = 1/298.3
p = 180/pi * 3600


B_1 = ToDoubleDegree(53, 35, 22.352) + ToDoubleDegree(0, 2 * variant, 0.125  * variant)
B_2 = ToDoubleDegree(58, 30, 12.135) + ToDoubleDegree(0, 2 * variant, 0.125  * variant)
L_1 = ToDoubleDegree(26, 35, 32.135) + ToDoubleDegree(0, 2 * variant, 0.125  * variant)
L_2 = ToDoubleDegree(29, 30, 51.415) + ToDoubleDegree(0, 2 * variant, 0.125  * variant)
delta_L = L_2 - L_1
delta_B = B_2 - B_1
B_parallel = ToDoubleDegree(51, 45, 35) - ToDoubleDegree(variant, 0, 0)

e = sqrt(2 * alpha - pow(alpha, 2))

e_touch = sqrt((2.0 * alpha - pow(alpha, 2.0))/(pow((1.0 - alpha), 2.0)))
c = a_m/sqrt(1.0 - pow(e, 2.0))
n_1 = c * (1.0 - 3.0/4.0 * pow(e_touch, 2.0) + 45.0/64.0 * pow(e_touch, 4.0) - 175.0/256.0 * pow(e_touch, 6.0) + 11025.0/16384.0 * pow(e_touch, 8.0))
n_2 = 3.0/8.0 * c * pow(e_touch, 2.0) * (1.0 - 5.0/4.0 * pow(e_touch, 2.0) + 175.0/128.0 * pow(e_touch, 4.0) - 105.0/64.0 * pow(e_touch, 6.0))
n_3 = 15.0/256.0 * c * pow(e_touch, 4.0) * (1.0 - 7.0/4.0 * pow(e_touch, 2.0) + 147.0/64.0 * pow(e_touch, 4.0))
n_4 = 35.0/3072.0 * c * pow(e_touch, 6.0) * (1.0 - 9.0/4.0 * pow(e_touch, 2.0))

s_1 = n_1 * (ToRadian(B_1) - 0) - n_2 * sin((ToRadian(B_1) - 0) * 2.0) + n_3 * sin((ToRadian(B_1) - 0) * 4.0) - n_4 * sin((ToRadian(B_1) - 0) * 6.0)
s_2 = n_1 * (ToRadian(B_2) - 0) - n_2 * sin((ToRadian(B_2) - 0) * 2.0) + n_3 * sin((ToRadian(B_2) - 0) * 4.0) - n_4 * sin((ToRadian(B_2) - 0) * 6.0)
# delta_s = n_1 * (ToRadian(B_2) - ToRadian(B_1)) - n_2 * sin((ToRadian(B_2) - ToRadian(B_1)) * 2.0) + n_3 * sin((ToRadian(B_2) - ToRadian(B_1)) * 4.0) - n_4 * sin((ToRadian(B_2) - ToRadian(B_1)) * 6.0)
delta_s = s_2 - s_1


X1 = 6367558.4969 * ToRadian(B_1) - sin(ToRadian(B_1)) * cos(ToRadian(B_1)) * (32005.7801 + (133.9213 + 0.7032 * pow(sin(ToRadian(B_1)), 2)) * pow(sin(ToRadian(B_1)), 2))
X2 = 6367558.4969 * ToRadian(B_2) - sin(ToRadian(B_2)) * cos(ToRadian(B_2)) * (32005.7801 + (133.9213 + 0.7032 * pow(sin(ToRadian(B_2)), 2)) * pow(sin(ToRadian(B_2)), 2))



delta_X_1 = X2 - X1
B_m = (B_1 + B_2)/2

V_m = sqrt(1.0 + pow((e_touch * cos(ToRadian(B_m))), 2.0))
V = sqrt(1.0 + pow((e_touch * cos(ToRadian(B_parallel))), 2.0))
V_1 = sqrt(1.0 + pow((e_touch * cos(ToRadian(B_1))), 2.0))
V_2 = sqrt(1.0 + pow((e_touch * cos(ToRadian(B_2))), 2.0))
delta_X_2 = c/pow(V_m, 3.0) * 1.0/p * (B_2 - B_1) * 3600.0



# double delta_X = M_m/p * (B_2 - B_1)

# double r = N * cos(B)

# double r = c/V * cos(B)

delta_Y = c/V * cos(ToRadian(B_parallel)) * (L_2 - L_1) * 3600.0/p


print("X1 (1.9) от экватора до B1, м = " , X1 , '\n')
print("X2 (1.9) от экватора до B2, м = ", X2 , '\n')
print("ΔХ = X2 - X1 (1.9),  Первый вариант = " ,delta_X_1 , '\n')
print("S1 (1.1) от экватора до B1, м = " , s_1 , '\n')
print("S2 (1.1) от экватора до B2, м = " , s_2 , '\n')
print("ΔS = S2 - S1 (1.1), м = " , delta_s , '\n')
print("ΔХ = X2 - X1 (1.9), Второй вариант = " , delta_X_2 , '\n')
print("Дуга пар. ΔY (1.14), м = " , delta_Y ,'\n')





# часть вторая

m = 1000000;
M = 1000000;


S_cm = c/pow(V_m, 3) * (B_2 - B_1)/180 * 100/m * pi
S_1_cm = c/V_1 * (L_2 - L_1) * cos(ToRadian(B_1)) * 100/m * pi
S_2_cm = c/V_2 * (L_2 - L_1) * cos(ToRadian(B_2)) * 100/m * pi


k = 1/(6 * p)
M_1 = (a_m * (1 - pow(e, 2)))/(sqrt(pow((1 - pow(e, 2) * (pow(sin(B_1 * pi/180), 2))), 3)))
M_2 = (a_m * (1 - pow(e, 2)))/(sqrt(pow((1 - pow(e, 2) * (pow(sin(B_2 * pi/180), 2))), 3)))
M_m = (a_m * (1 - pow(e, 2)))/(sqrt(pow((1 - pow(e, 2) * (pow(sin(B_m * pi/180), 2))), 3)))
c_m = k * (M_1 + 4 * M_m + M_2) + delta_B * 3600

print(c)
c_cm_M = c_m * 100/M

a_cm_M = a_m * 100/M

r_1 = (a_cm_M * cos(B_1 * pi/180))/(sqrt(1 - pow(e, 2) * pow((sin(B_1 * pi/180)), 2)))
r_2 = (a_cm_M * cos(B_2 * pi/180))/(sqrt(1 - pow(e, 2) * pow((sin(B_2 * pi/180)), 2)))

A_south = pi * r_1 * delta_L/180
A_north = pi * r_2 * delta_L/180


A_touch = 1 + 1/2 * pow(e, 2) + 3/8 * pow(e, 4) + 5/16 * pow(e, 6) + 35/128 * pow(e, 8)
B_touch = 1/6 * pow(e, 2) + 3/16 * pow(e, 4) + 3/16 * pow(e, 6) + 35/192 * pow(e, 8)
C_touch = 3/80 * pow(e, 4) + 1/16 * pow(e, 6) + 5/64 * pow(e, 8)
D_touch = 1/112 * pow(e, 6) + 5/256 * pow(e, 8)
E_touch = 5/2304 * pow(e, 8)
A1 = A_touch * sin(1/2 * delta_B * pi/180) * cos(B_m * pi/180)
B1 = B_touch * sin(3/2 * delta_B * pi/180) * cos(3 * B_m * pi/180)
C1 = C_touch * sin(5/2 * delta_B * pi/180) * cos(5 * B_m * pi/180)
D1 = D_touch * sin(7/2 * delta_B * pi/180) * cos(7 * B_m * pi/180)
E1 = E_touch * sin(9/2 * delta_B * pi/180) * cos(9 * B_m * pi/180)

b = a_m * sqrt(1 - pow(e, 2))
S_m_2 = delta_L/360 * 4 * pi * pow(b, 2) * (A1 - B1 + C1 - D1 + E1)


S_km_2 = S_m_2/1000000
S_cm_2_M = S_m_2/pow((M * 100), 2)

# print("S мер (1.15), см =", S_cm , '\n')
# print("S юж.пар. (1.15), см =", S_1_cm , '\n')
# print("S сев.пар. (1.15), см =", S_2_cm , '\n')
# print("S мер (1.23), см =", c_cm_M, '\n')
    