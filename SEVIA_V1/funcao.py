import numpy as np

#DRAC
def drac(vel, dista):
  DRAC = (vel**2)/(2*dista)
  return DRAC

#MTTC
def mttc(var_vel, vel, var_ace, dist):
  MTTC = (- var_vel - (np.sqrt(vel**2) + 2 * var_ace * dist))/var_ace
  return MTTC

# A função dist permite Calcular a Distância (em metros) a partir das coords. geográficas Latitude e longitude p/ 2 pontos
def dist(lat1, lon1, lat2, lon2):
  #Convrsão de latitude
  clat1 = lat1*110.574657
  clat2 = lat2*110.574657

  #Conversão de longitude
  clon1 = lon1*111.319892
  clon2 = lon2*111.319892

  #Cálculo de distância
  plat = clat2 - clat1
  plon = clon2 - clon1

  plat2 = plat ** 2
  plon2 = plon ** 2
  out = np.sqrt(plon2 + plat2)
  return out*1000 #Retorna saída em metros